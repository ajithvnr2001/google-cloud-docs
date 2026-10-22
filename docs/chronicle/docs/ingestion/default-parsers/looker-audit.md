---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/looker-audit/
title: Collect Google Cloud Looker audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:02.302278+00:00
---

# Collect Google Cloud Looker audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/looker-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Google Cloud Looker audit logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Google Cloud Looker audit logs to Google Security Operations using Google Cloud Storage or Amazon S3.

Looker is a business intelligence and data analytics platform that enables organizations to explore, analyze, and share real-time business insights. Looker's System Activity model tracks user authentication events, query execution history, dashboard and Look access, content creation and modification, download events, API calls, scheduled delivery events, and permission changes.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Looker instance with admin access or the `see_system_activity` permission
  * Looker API credentials (Client ID and Client Secret)
  * For GCS path: A GCP project with Cloud Storage, Cloud Run, Pub/Sub, and Cloud Scheduler APIs enabled
  * For S3 path: Privileged access to **AWS** (S3, IAM)



## Configure Looker API credentials

To enable Google SecOps to retrieve System Activity audit data, you need to create API credentials in Looker and configure a service account with the required permissions.

### Create a Looker service account for API access

  1. Sign in to your **Looker instance** as an admin.
  2. Go to **Admin > Users**.
  3. Click **Add Users**.
  4. In the **Email** field, enter a service account email (for example, `chronicle-integration@yourcompany.com`).
  5. Under **Roles** , select a role that includes the `see_system_activity` permission.

**Note:** The `see_system_activity` permission is required to access the Event and History System Activity Explores. Looker admins have this permission by default.
  6. Click **Save**.




### Generate API3 credentials

  1. Go to **Admin > Users**.
  2. Find the service account user you created and click **Edit**.
  3. Scroll down to the **API Keys** section.
  4. Click **New API Key**.
  5. Copy and save the following values in a secure location:

     * **Client ID** : The public identifier for API authentication
     * **Client Secret** : The private key for API authentication
**Note:** The Client Secret is displayed only once. If you lose it, you must delete the key and create a new one.



### Identify your Looker API base URL

  * Your Looker API base URL follows this format:
        
        https://<instance_name>.cloud.looker.com
        




For Looker instances hosted on Google Cloud, Microsoft Azure, and instances hosted on AWS created on or after 07/07/2020, the API uses port 443 (default HTTPS). For older AWS-hosted instances, the API may use port 19999.

You can find the API Host URL by navigating to **Admin > API** in your Looker instance.

### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        LOOKER_BASE_URL="https://your-instance.cloud.looker.com"
        CLIENT_ID="your-client-id"
        CLIENT_SECRET="your-client-secret"
        
        # Obtain access token
        TOKEN=$(curl -s -X POST "${LOOKER_BASE_URL}/api/4.0/login" \
            -d "client_id=${CLIENT_ID}&client_secret=${CLIENT_SECRET}" \
            | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")
        
        # Test System Activity access
        curl -s -H "Authorization: token ${TOKEN}" \
            "${LOOKER_BASE_URL}/api/4.0/queries/run/json" \
            -X POST \
            -H "Content-Type: application/json" \
            -d '{"model":"system__activity","view":"event","fields":["event.name","event.created_time"],"limit":"5","sorts":["event.created_time desc"]}' \
            | python3 -m json.tool
        




A successful response returns a JSON array of recent Looker events.

## Option A: Configure ingestion using Google Cloud Storage

This option uses a Cloud Run function to poll the Looker API for System Activity audit events and write them to a GCS bucket for ingestion by Google SecOps.

### Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `looker-audit-logs-gcs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




### Create service account for Cloud Run function

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `looker-audit-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Looker audit logs`
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
  2. Click on your bucket name (`looker-audit-logs-gcs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`looker-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



### Create Pub/Sub topic

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `looker-audit-trigger`
     * Leave other settings as default
  4. Click **Create**.



### Create Cloud Run function to collect logs

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `looker-audit-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `looker-audit-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `looker-audit-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `looker-audit-logs-gcs` | GCS bucket name  
`GCS_PREFIX` | `looker-audit` | Prefix for log files  
`STATE_KEY` | `looker-audit/state.json` | State file path  
`LOOKER_BASE_URL` | `https://your-instance.cloud.looker.com` | Looker API base URL  
`LOOKER_CLIENT_ID` | `your-client-id` | Looker API Client ID  
`LOOKER_CLIENT_SECRET` | `your-client-secret` | Looker API Client Secret  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
`PAGE_SIZE` | `5000` | Records per API page  
`MAX_PAGES` | `20` | Max pages per query  
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
        import urllib.parse
        from datetime import datetime, timezone, timedelta
        
        http = urllib3.PoolManager(
            timeout=urllib3.Timeout(connect=10.0, read=60.0),
            retries=False,
        )
        
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        
        GCS_BUCKET = os.environ.get('GCS_BUCKET')
        GCS_PREFIX = os.environ.get('GCS_PREFIX', 'looker-audit')
        STATE_KEY = os.environ.get('STATE_KEY', 'looker-audit/state.json')
        LOOKER_BASE_URL = os.environ.get('LOOKER_BASE_URL', '').rstrip('/')
        CLIENT_ID = os.environ.get('LOOKER_CLIENT_ID')
        CLIENT_SECRET = os.environ.get('LOOKER_CLIENT_SECRET')
        LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
        PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '5000'))
        MAX_PAGES = int(os.environ.get('MAX_PAGES', '20'))
        
        @functions_framework.cloud_event
        def main(cloud_event):
            if not all([GCS_BUCKET, LOOKER_BASE_URL, CLIENT_ID, CLIENT_SECRET]):
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
        
                print(f"Fetching events from {last_time.isoformat()} to {now.isoformat()}")
        
                token = get_access_token()
        
                events = fetch_system_activity(
                    token, 'event',
                    [
                        'event.id', 'event.name', 'event.category',
                        'event.created_time', 'event.is_api_call',
                        'event.is_admin', 'event.is_looker_employee',
                        'user.id', 'user.name', 'user.email'
                    ],
                    'event.created_time', last_time, now
                )
        
                history = fetch_system_activity(
                    token, 'history',
                    [
                        'history.id', 'history.created_time',
                        'history.completed_time', 'history.status',
                        'history.source', 'history.issuer_source',
                        'history.runtime', 'history.message',
                        'query.id', 'query.model', 'query.view',
                        'user.id', 'user.name', 'user.email',
                        'dashboard.id', 'dashboard.title',
                        'look.id', 'look.title'
                    ],
                    'history.created_time', last_time, now
                )
        
                all_records = []
                for e in events:
                    e['_looker_record_type'] = 'event'
                    all_records.append(e)
                for h in history:
                    h['_looker_record_type'] = 'history'
                    all_records.append(h)
        
                if not all_records:
                    print("No new records found.")
                    save_state(bucket, now.isoformat())
                    return
        
                timestamp = now.strftime('%Y%m%d_%H%M%S')
                object_key = f"{GCS_PREFIX}/looker_audit_{timestamp}.ndjson"
                blob = bucket.blob(object_key)
        
                ndjson = '\n'.join(
                    [json.dumps(r, ensure_ascii=False, default=str) for r in all_records]
                ) + '\n'
                blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
        
                print(f"Wrote {len(all_records)} records to gs://{GCS_BUCKET}/{object_key}")
        
                newest = find_newest_time(events, history)
                save_state(bucket, newest if newest else now.isoformat())
        
                print(f"Successfully processed {len(all_records)} records "
                      f"(events: {len(events)}, history: {len(history)})")
        
            except Exception as e:
                print(f'Error processing logs: {str(e)}')
                raise
        
        def get_access_token():
            url = f"{LOOKER_BASE_URL}/api/4.0/login"
            encoded_body = urllib.parse.urlencode({
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET
            }).encode('utf-8')
        
            response = http.request(
                'POST', url,
                body=encoded_body,
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )
        
            if response.status != 200:
                raise Exception(
                    f"Looker login failed: {response.status} - "
                    f"{response.data.decode('utf-8')}"
                )
        
            data = json.loads(response.data.decode('utf-8'))
            token = data.get('access_token')
            if not token:
                raise Exception("No access_token in login response")
        
            print("Successfully obtained Looker API access token")
            return token
        
        def fetch_system_activity(token, view, fields, time_field, start_time, end_time):
            start_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
            end_str = end_time.strftime('%Y-%m-%d %H:%M:%S')
        
            all_records = []
            offset = 0
        
            for page in range(MAX_PAGES):
                query_body = {
                    "model": "system__activity",
                    "view": view,
                    "fields": fields,
                    "filters": {
                        time_field: f"{start_str} to {end_str}"
                    },
                    "sorts": [f"{time_field} asc"],
                    "limit": str(PAGE_SIZE),
                    "offset": str(offset)
                }
        
                url = f"{LOOKER_BASE_URL}/api/4.0/queries/run/json"
                response = http.request(
                    'POST', url,
                    body=json.dumps(query_body).encode('utf-8'),
                    headers={
                        'Authorization': f'token {token}',
                        'Content-Type': 'application/json'
                    }
                )
        
                if response.status == 429:
                    print(f"Rate limited on {view} query. Stopping pagination.")
                    break
        
                if response.status != 200:
                    print(f"{view} query failed: {response.status} - "
                          f"{response.data.decode('utf-8')}")
                    break
        
                page_results = json.loads(response.data.decode('utf-8'))
        
                if not page_results:
                    break
        
                all_records.extend(page_results)
                print(f"{view} page {page + 1}: {len(page_results)} records "
                      f"(total: {len(all_records)})")
        
                if len(page_results) < PAGE_SIZE:
                    break
        
                offset += PAGE_SIZE
        
            print(f"Total {view} records fetched: {len(all_records)}")
            return all_records
        
        def find_newest_time(events, history):
            newest = None
            for e in events:
                t = e.get('event.created_time')
                if t and (newest is None or t > newest):
                    newest = t
            for h in history:
                t = h.get('history.created_time')
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
        



  1. Click **Deploy** to save and deploy the function.
  2. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



### Create Cloud Scheduler job

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `looker-audit-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `looker-audit-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Test the integration

  1. In the **Cloud Scheduler** console, find your job (`looker-audit-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `looker-audit-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching events from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Successfully obtained Looker API access token
         event page 1: X records (total: X)
         history page 1: X records (total: X)
         Wrote X records to gs://looker-audit-logs-gcs/looker-audit/looker_audit_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records (events: X, history: X)
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on `looker-audit-logs-gcs`.

  10. Navigate to the `looker-audit/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Verify the `LOOKER_CLIENT_ID` and `LOOKER_CLIENT_SECRET` environment variables are correct
  * **HTTP 403** : Verify the Looker user has the `see_system_activity` permission
  * **HTTP 429** : Rate limiting — the function will stop pagination and resume on the next scheduled run
  * **Missing environment variables** : Verify all required variables are set in the Cloud Run function configuration



### Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Looker Audit Logs GCS`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Looker Audit** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://looker-audit-logs-gcs/looker-audit/
           

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




### Grant IAM permissions to the Google SecOps service account

  1. Go to **Cloud Storage > Buckets**.
  2. Click on `looker-audit-logs-gcs`.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Option B: Configure ingestion using Amazon S3

This option uses an AWS Lambda function to poll the Looker API for System Activity audit events and write them to an S3 bucket for ingestion by Google SecOps.

### Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `looker-audit-logs`).
  3. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**.
  5. Select **Security credentials** tab.
  6. Click **Create Access Key** in section **Access Keys**.
  7. Select **Third-party service** as **Use case**.
  8. Click **Next**.
  9. Optional: Add description tag.
  10. Click **Create access key**.
  11. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  12. Click **Done**.
  13. Select **Permissions** tab.
  14. Click **Add permissions** in section **Permissions policies**.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**.
  17. Search for **AmazonS3FullAccess** policy.
  18. Select the policy.
  19. Click **Next**.
  20. Click **Add permissions**.



### Configure the IAM policy and role for S3 uploads

  1. In the AWS console, go to **IAM > Policies > Create policy > JSON tab**.
  2. Copy and paste the policy below.
  3. **Policy JSON** (replace `looker-audit-logs` if you entered a different bucket name):
         
         {
                 "Version": "2012-10-17",
                 "Statement": [
                         {
                                 "Sid": "AllowPutObjects",
                                 "Effect": "Allow",
                                 "Action": "s3:PutObject",
                                 "Resource": "arn:aws:s3:::looker-audit-logs/*"
                         },
                         {
                                 "Sid": "AllowGetStateObject",
                                 "Effect": "Allow",
                                 "Action": "s3:GetObject",
                                 "Resource": "arn:aws:s3:::looker-audit-logs/looker-audit/state.json"
                         }
                 ]
         }
         

  4. Click **Next > Create policy**.

  5. Go to **IAM > Roles > Create role > AWS service > Lambda**.

  6. Attach the newly created policy.

  7. Name the role `LookerAuditCollectorRole` and click **Create role**.




### Create the Lambda function

  1. In the **AWS Console** , go to **Lambda > Functions > Create function**.
  2. Click **Author from scratch**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `LookerAuditCollector`  
**Runtime** | Python 3.13  
**Architecture** | x86_64  
**Execution role** | `LookerAuditCollectorRole`  
  4. After the function is created, open the **Code** tab, delete the stub and paste the code below (**LookerAuditCollector.py**).
         
         import urllib3
         import json
         import boto3
         import os
         from datetime import datetime, timezone, timedelta
         import logging
         import urllib.parse
         
         logger = logging.getLogger()
         logger.setLevel(logging.INFO)
         
         http = urllib3.PoolManager(
             timeout=urllib3.Timeout(connect=10.0, read=60.0),
             retries=False,
         )
         s3 = boto3.client('s3')
         
         BUCKET = os.environ['S3_BUCKET']
         PREFIX = os.environ['S3_PREFIX']
         STATE_KEY = os.environ['STATE_KEY']
         LOOKER_BASE_URL = os.environ['LOOKER_BASE_URL'].rstrip('/')
         CLIENT_ID = os.environ['LOOKER_CLIENT_ID']
         CLIENT_SECRET = os.environ['LOOKER_CLIENT_SECRET']
         LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
         PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '5000'))
         MAX_PAGES = int(os.environ.get('MAX_PAGES', '20'))
         
         def lambda_handler(event, context):
             try:
                 state = load_state()
                 now = datetime.now(timezone.utc)
         
                 if state and state.get('last_event_time'):
                     try:
                         last_time = datetime.fromisoformat(
                             state['last_event_time'].replace('Z', '+00:00')
                         )
                         last_time = last_time - timedelta(minutes=2)
                     except Exception as e:
                         logger.warning(f"Could not parse last_event_time: {e}")
                         last_time = now - timedelta(hours=LOOKBACK_HOURS)
                 else:
                     last_time = now - timedelta(hours=LOOKBACK_HOURS)
         
                 logger.info(f"Fetching events from {last_time.isoformat()} to {now.isoformat()}")
         
                 token = get_access_token()
         
                 events = fetch_events(token, last_time, now)
                 history = fetch_history(token, last_time, now)
         
                 all_records = []
                 for e in events:
                     e['_looker_record_type'] = 'event'
                     all_records.append(e)
                 for h in history:
                     h['_looker_record_type'] = 'history'
                     all_records.append(h)
         
                 if not all_records:
                     logger.info("No new records found.")
                     save_state(now.isoformat())
                     return {'statusCode': 200, 'body': json.dumps({'events': 0})}
         
                 timestamp = now.strftime('%Y%m%d_%H%M%S')
                 object_key = f"{PREFIX}/looker_audit_{timestamp}.ndjson"
         
                 ndjson = '\n'.join(
                     [json.dumps(r, ensure_ascii=False, default=str) for r in all_records]
                 ) + '\n'
         
                 s3.put_object(
                     Bucket=BUCKET,
                     Key=object_key,
                     Body=ndjson.encode('utf-8'),
                     ContentType='application/x-ndjson'
                 )
         
                 logger.info(f"Wrote {len(all_records)} records to s3://{BUCKET}/{object_key}")
         
                 newest_time = find_newest_time(events, history)
                 save_state(newest_time if newest_time else now.isoformat())
         
                 return {
                     'statusCode': 200,
                     'body': json.dumps({
                         'events': len(events),
                         'history': len(history),
                         'total': len(all_records)
                     })
                 }
         
             except Exception as e:
                 logger.error(f"Lambda execution failed: {str(e)}")
                 raise
         
         def get_access_token():
             url = f"{LOOKER_BASE_URL}/api/4.0/login"
             encoded_body = urllib.parse.urlencode({
                 'client_id': CLIENT_ID,
                 'client_secret': CLIENT_SECRET
             }).encode('utf-8')
         
             response = http.request(
                 'POST', url,
                 body=encoded_body,
                 headers={'Content-Type': 'application/x-www-form-urlencoded'}
             )
         
             if response.status != 200:
                 raise Exception(
                     f"Login failed with status {response.status}: "
                     f"{response.data.decode('utf-8')}"
                 )
         
             data = json.loads(response.data.decode('utf-8'))
             token = data.get('access_token')
             if not token:
                 raise Exception("No access_token in login response")
         
             logger.info("Successfully obtained Looker API access token")
             return token
         
         def fetch_events(token, start_time, end_time):
             start_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
             end_str = end_time.strftime('%Y-%m-%d %H:%M:%S')
         
             all_events = []
             offset = 0
         
             for page in range(MAX_PAGES):
                 query_body = {
                     "model": "system__activity",
                     "view": "event",
                     "fields": [
                         "event.id",
                         "event.name",
                         "event.category",
                         "event.created_time",
                         "event.is_api_call",
                         "event.is_admin",
                         "event.is_looker_employee",
                         "user.id",
                         "user.name",
                         "user.email"
                     ],
                     "filters": {
                         "event.created_time": f"{start_str} to {end_str}"
                     },
                     "sorts": ["event.created_time asc"],
                     "limit": str(PAGE_SIZE),
                     "offset": str(offset)
                 }
         
                 url = f"{LOOKER_BASE_URL}/api/4.0/queries/run/json"
                 response = http.request(
                     'POST', url,
                     body=json.dumps(query_body).encode('utf-8'),
                     headers={
                         'Authorization': f'token {token}',
                         'Content-Type': 'application/json'
                     }
                 )
         
                 if response.status == 429:
                     logger.warning("Rate limited on events query. Stopping pagination.")
                     break
         
                 if response.status != 200:
                     logger.error(
                         f"Events query failed: {response.status} - "
                         f"{response.data.decode('utf-8')}"
                     )
                     break
         
                 page_results = json.loads(response.data.decode('utf-8'))
         
                 if not page_results:
                     logger.info(f"Events: No more results at offset {offset}")
                     break
         
                 all_events.extend(page_results)
                 logger.info(
                     f"Events page {page + 1}: Retrieved {len(page_results)} records "
                     f"(total: {len(all_events)})"
                 )
         
                 if len(page_results) < PAGE_SIZE:
                     break
         
                 offset += PAGE_SIZE
         
             logger.info(f"Total events fetched: {len(all_events)}")
             return all_events
         
         def fetch_history(token, start_time, end_time):
             start_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
             end_str = end_time.strftime('%Y-%m-%d %H:%M:%S')
         
             all_history = []
             offset = 0
         
             for page in range(MAX_PAGES):
                 query_body = {
                     "model": "system__activity",
                     "view": "history",
                     "fields": [
                         "history.id",
                         "history.created_time",
                         "history.completed_time",
                         "history.status",
                         "history.source",
                         "history.issuer_source",
                         "history.runtime",
                         "history.message",
                         "query.id",
                         "query.model",
                         "query.view",
                         "user.id",
                         "user.name",
                         "user.email",
                         "dashboard.id",
                         "dashboard.title",
                         "look.id",
                         "look.title"
                     ],
                     "filters": {
                         "history.created_time": f"{start_str} to {end_str}"
                     },
                     "sorts": ["history.created_time asc"],
                     "limit": str(PAGE_SIZE),
                     "offset": str(offset)
                 }
         
                 url = f"{LOOKER_BASE_URL}/api/4.0/queries/run/json"
                 response = http.request(
                     'POST', url,
                     body=json.dumps(query_body).encode('utf-8'),
                     headers={
                         'Authorization': f'token {token}',
                         'Content-Type': 'application/json'
                     }
                 )
         
                 if response.status == 429:
                     logger.warning("Rate limited on history query. Stopping pagination.")
                     break
         
                 if response.status != 200:
                     logger.error(
                         f"History query failed: {response.status} - "
                         f"{response.data.decode('utf-8')}"
                     )
                     break
         
                 page_results = json.loads(response.data.decode('utf-8'))
         
                 if not page_results:
                     logger.info(f"History: No more results at offset {offset}")
                     break
         
                 all_history.extend(page_results)
                 logger.info(
                     f"History page {page + 1}: Retrieved {len(page_results)} records "
                     f"(total: {len(all_history)})"
                 )
         
                 if len(page_results) < PAGE_SIZE:
                     break
         
                 offset += PAGE_SIZE
         
             logger.info(f"Total history records fetched: {len(all_history)}")
             return all_history
         
         def find_newest_time(events, history):
             newest = None
             for e in events:
                 t = e.get('event.created_time')
                 if t and (newest is None or t > newest):
                     newest = t
             for h in history:
                 t = h.get('history.created_time')
                 if t and (newest is None or t > newest):
                     newest = t
             return newest
         
         def load_state():
             try:
                 obj = s3.get_object(Bucket=BUCKET, Key=STATE_KEY)
                 return json.loads(obj['Body'].read().decode('utf-8'))
             except s3.exceptions.NoSuchKey:
                 logger.info("No previous state found, starting fresh")
                 return None
             except Exception as e:
                 logger.warning(f"Could not load state: {e}")
                 return None
         
         def save_state(last_event_time):
             state = {
                 'last_event_time': last_event_time,
                 'last_run': datetime.now(timezone.utc).isoformat()
             }
             s3.put_object(
                 Bucket=BUCKET,
                 Key=STATE_KEY,
                 Body=json.dumps(state, indent=2).encode('utf-8'),
                 ContentType='application/json'
             )
             logger.info(f"Saved state: last_event_time={last_event_time}")
         

  5. Go to **Configuration > Environment variables > Edit > Add new environment variable**.

  6. Enter the environment variables provided below, replacing with your values.




**Environment variables**

Key | Example value  
---|---  
`S3_BUCKET` | `looker-audit-logs`  
`S3_PREFIX` | `looker-audit/`  
`STATE_KEY` | `looker-audit/state.json`  
`LOOKER_BASE_URL` | `https://your-instance.cloud.looker.com`  
`LOOKER_CLIENT_ID` | `your-looker-client-id`  
`LOOKER_CLIENT_SECRET` | `your-looker-client-secret`  
`LOOKBACK_HOURS` | `24`  
`PAGE_SIZE` | `5000`  
`MAX_PAGES` | `20`  
  
  1. After the function is created, stay on its page (or open **Lambda > Functions > your-function**).
  2. Select the **Configuration** tab.
  3. In the **General configuration** panel click **Edit**.
  4. Change **Timeout** to **5 minutes (300 seconds)** and click **Save**.

**Note:** Timeout is a hard upper limit, meaning if the function is still running when the timer hits 5 minutes, AWS Lambda will terminate it. Any shorter execution just finishes normally; you are billed only for the actual run time.



### Create an EventBridge schedule

  1. Go to **Amazon EventBridge > Scheduler > Create schedule**.
  2. Provide the following configuration details: 
     * **Recurring schedule** : **Rate** (`1 hour`)
     * **Target** : Your Lambda function `LookerAuditCollector`
     * **Name** : `LookerAuditCollector-1h`
  3. Click **Create schedule**.



### Configure a feed in Google SecOps to ingest Looker audit logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name**.
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Looker Audit** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields:

     * **S3 URI** : `s3://looker-audit-logs/looker-audit/`
     * **Source deletion option** : Select the deletion option according to your preference
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Access Key ID** : User access key with access to the S3 bucket
     * **Secret Access Key** : User secret key with access to the S3 bucket
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
  9. Click **Next** and then click **Submit**.




## Looker System Activity data reference

The following table describes the key data available from Looker System Activity Explores that are collected by this integration:

Explore | Data Collected | Retention  
---|---|---  
**Event** | User authentication events, content creation and modification, permission changes, API calls, scheduled delivery events, download events | 90 days (default)  
**History** | Query execution history, dashboard and Look access, query runtime and status, source of query (UI, API, schedule) | 90 days (default)  
**Note:** System Activity data is retained for 90 days by default in Looker's internal database. The Lambda or Cloud Run function collects data incrementally on each run, so data older than 90 days cannot be retrieved retroactively.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
Group Edit Link | additional.fields.Group_Edit_Link_label.value.string_value | Value copied directly  
Group ID | additional.fields.Group_ID_label.value.string_value | Value copied directly  
History Most Recent Run Length in Seconds | additional.fields.History_Most_Recent_Run_Length_in_Seconds_label.value.string_value | Value copied directly  
History Slug | additional.fields.History_Slug_label.value.string_value | Value copied directly  
History Source | additional.fields.History_Source_label.value.string_value | Value copied directly  
History Status | additional.fields.History_Status_label.value.string_value | Value copied directly  
Look Link | additional.fields.Look_Link_label.value.string_value | Value copied directly  
Look Title | additional.fields.Look_Title_label.value.string_value | Value copied directly  
User Edit Link | additional.fields.User_Edit_Link_label.value.string_value | Value copied directly  
User Home Folder | additional.fields.User_Home_Folder_label.value.string_value | Value copied directly  
dashboard.link | additional.fields.dashboard_link_label.value.string_value | Value copied directly  
dashboard.title | additional.fields.dashboard_title_label.value.string_value | Value copied directly  
history.source | additional.fields.history_source_label.value.string_value | Value copied directly  
history.status | additional.fields.history_status_label.value.string_value | Value copied directly  
history.id | additional.fields.id_label.value.string_value | Converted to string  
history.connection_name | additional.fields.name_label.value.string_value | Value copied directly  
query.model | additional.fields.query_model_label.value.string_value | Value copied directly  
query.view | additional.fields.query_view_label.value.string_value | Value copied directly  
sql_text.text | additional.fields.sql_text_text_label.value.string_value | Value copied directly  
History Created Time | metadata.event_timestamp | Parsed using ISO8601, RFC 3339, or yyyy-MM-dd HH:mm:ss format  
has_principal_user | metadata.event_type | Set to "NETWORK_CONNECTION" if has_principal and has_target are true; "USER_UNCATEGORIZED" if has_principal_user is true; "STATUS_UPDATE" if has_principal is true; else "GENERIC_EVENT"  
has_principal | metadata.event_type |   
has_target | metadata.event_type |   
User Email | principal.email | Value from User Email if not empty, else user.email  
user.email | principal.email |   
Group Name | principal.group.group_display_name | Value copied directly  
User ID | principal.user.product_object_id | Value from User ID if not empty, else user.id  
user.id | principal.user.product_object_id |   
User Name | principal.user.userid | Value from User Name if not empty, else user.name  
user.name | principal.user.userid |   
Kevin Liu | security_result.category_details | Merged with "Kevin_Liu_label" if Kevin Liu not empty, "History_ID_label" if History ID not empty, "History_Created_Date_label" if History Created Date not empty  
History ID | security_result.category_details |   
History Created Date | security_result.category_details |   
Look Description | security_result.description | Value copied directly  
User Name sorted | target.hostname | Value copied if User Dev Branch Name is not empty  
`user.name` | `principal.user.user_display_name` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/looker-audit-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
