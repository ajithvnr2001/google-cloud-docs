---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/metabase/
title: Collect Metabase logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:40.489730+00:00
---

# Collect Metabase logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/metabase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Metabase logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Metabase logs to Google Security Operations using Google Cloud Storage V2.

Metabase is an open-source business intelligence and analytics platform that allows organizations to query databases, create visualizations, and build dashboards. On Pro and Enterprise plans, Metabase stores usage analytics and audit data in its application database, including activity logs, view logs, and query execution records. A Cloud Run function queries the Metabase API to retrieve this data and writes it to a GCS bucket for ingestion by Google SecOps.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage, Cloud Run, Pub/Sub, and Cloud Scheduler APIs enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Metabase Pro or Enterprise plan (usage analytics is not available on Open Source or Cloud Starter editions)
  * Metabase administrator access to create API keys
  * The Metabase application database added as a data source within Metabase (required for querying audit tables via API)



## Configure Metabase API access

To enable Google SecOps to retrieve usage analytics data, you need to create an API key in Metabase and add the application database as a queryable data source.

### Create an API key

  1. Sign in to your **Metabase instance** as an administrator.
  2. Click the **gear icon** in the upper right corner.
  3. Select **Admin settings**.
  4. Go to the **Settings** tab.
  5. Click on the **Authentication** tab in the left menu.
  6. Scroll to **API Keys** and click **Manage**.
  7. Click the **Create API Key** button.
  8. Provide the following configuration details: 
     * **Key name** : Enter a descriptive name (for example, `Google SecOps Integration`)
     * **Group** : Select a group with access to the Usage Analytics collection and query permissions for the application database
  9. Click **Create**.
  10. Copy and save the API key securely.

**Note:** Metabase displays the API key only once. If you lose it, you must regenerate a new key.



### Add the application database as a data source

To query audit tables via the API, you must add the Metabase application database as a data source within Metabase.

  1. In Metabase, click the **gear icon** in the upper right corner.
  2. Select **Admin settings**.
  3. Go to the **Databases** tab.
  4. Click **Add a database**.
  5. Configure the database connection: 
     * **Database type** : Select **PostgreSQL** or **MySQL** (depending on your application database)
     * **Name** : Enter `Metabase Application Database`
     * **Host** : Enter the hostname of your application database
     * **Port** : Enter the database port (default: `5432` for PostgreSQL, `3306` for MySQL)
     * **Database name** : Enter the application database name (for example, `metabase`)
     * **Username** : Enter a database user with SELECT permissions on the `audit_log`, `view_log`, and `query_execution` tables
     * **Password** : Enter the database password
  6. Click **Save**.
  7. After saving, note the **Database ID** from the URL (for example, `https://metabase.example.com/admin/databases/5` means the database ID is `5`).



### Verify permissions

To verify the API key has the required permissions:

  1. Sign in to Metabase as an administrator.
  2. Click the **gear icon** > **Admin settings** > **People**.
  3. Find the group assigned to the API key.
  4. Verify the group has access to the **Usage Analytics** collection.
  5. Go to **Admin settings** > **Permissions** > **Data**.
  6. Verify the group has **Unrestricted** or **Query** access to the application database.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual values
        METABASE_URL="https://your-metabase-instance.com"
        API_KEY="mb_your_api_key_here"
        DATABASE_ID="5"
        
        # Test API key authentication
        curl -s -H "x-api-key: ${API_KEY}" \
          "${METABASE_URL}/api/database" \
          | python3 -m json.tool
        
        # Test querying the application database for audit_log records
        curl -s -X POST "${METABASE_URL}/api/dataset/json" \
          -H "x-api-key: ${API_KEY}" \
          -H "Content-Type: application/json" \
          -d "{\"database\": ${DATABASE_ID}, \"type\": \"native\", \"native\": {\"query\": \"SELECT * FROM audit_log ORDER BY id DESC LIMIT 5\", \"template-tags\": {}}, \"parameters\": []}" \
          | python3 -m json.tool
        




A successful response returns a JSON array of recent audit log records.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `metabase-audit-logs`)  
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
     * **Service account name** : Enter `metabase-audit-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Metabase audit logs`
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
  2. Click on your bucket name (`metabase-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`metabase-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `metabase-audit-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch audit data from the Metabase API and write it to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `metabase-audit-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `metabase-audit-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `metabase-audit-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `metabase-audit-logs` | GCS bucket name  
`GCS_PREFIX` | `metabase-audit` | Prefix for log files  
`STATE_KEY` | `metabase-audit/state.json` | State file path  
`METABASE_URL` | `https://metabase.yourcompany.com` | Metabase instance base URL  
`METABASE_API_KEY` | `mb_your_api_key_here` | Metabase API key  
`DATABASE_ID` | `5` | Application database ID  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
`PAGE_SIZE` | `2000` | Records per API query  
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
           
           http = urllib3.PoolManager(
             timeout=urllib3.Timeout(connect=10.0, read=60.0),
             retries=False,
           )
           
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'metabase-audit')
           STATE_KEY = os.environ.get('STATE_KEY', 'metabase-audit/state.json')
           METABASE_URL = os.environ.get('METABASE_URL', '').rstrip('/')
           API_KEY = os.environ.get('METABASE_API_KEY')
           DATABASE_ID = int(os.environ.get('DATABASE_ID', '1'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '2000'))
           
           TABLES = ['audit_log', 'view_log', 'query_execution']
           
           TABLE_TIME_COLUMNS = {
             'audit_log': 'timestamp',
             'view_log': 'timestamp',
             'query_execution': 'started_at',
           }
           
           @functions_framework.cloud_event
           def main(cloud_event):
             if not all([GCS_BUCKET, METABASE_URL, API_KEY]):
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
           
               all_records = []
               newest_time = None
           
               for table in TABLES:
                 time_col = TABLE_TIME_COLUMNS[table]
                 records = fetch_table(table, time_col, last_time, now)
                 for r in records:
                   r['_metabase_table'] = table
                   t = r.get(time_col)
                   if t and (newest_time is None or str(t) > str(newest_time)):
                     newest_time = t
                 all_records.extend(records)
                 print(f"Table {table}: fetched {len(records)} records")
           
               if not all_records:
                 print("No new records found.")
                 save_state(bucket, now.isoformat())
                 return
           
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/metabase_audit_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join(
                 [json.dumps(r, ensure_ascii=False, default=str) for r in all_records]
               ) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
               print(f"Wrote {len(all_records)} records to gs://{GCS_BUCKET}/{object_key}")
           
               save_state(bucket, str(newest_time) if newest_time else now.isoformat())
           
               print(f"Successfully processed {len(all_records)} records")
           
             except Exception as e:
               print(f'Error processing logs: {str(e)}')
               raise
           
           def fetch_table(table, time_col, start_time, end_time):
             start_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
             end_str = end_time.strftime('%Y-%m-%d %H:%M:%S')
           
             all_records = []
             offset = 0
             max_pages = 50
           
             for page in range(max_pages):
               sql = (
                 f"SELECT * FROM {table} "
                 f"WHERE {time_col} >= '{start_str}' "
                 f"AND {time_col} < '{end_str}' "
                 f"ORDER BY {time_col} ASC "
                 f"LIMIT {PAGE_SIZE} OFFSET {offset}"
               )
           
               query_body = {
                 "database": DATABASE_ID,
                 "type": "native",
                 "native": {
                   "query": sql,
                   "template-tags": {}
                 },
                 "parameters": []
               }
           
               url = f"{METABASE_URL}/api/dataset/json"
               response = http.request(
                 'POST', url,
                 body=json.dumps(query_body).encode('utf-8'),
                 headers={
                   'x-api-key': API_KEY,
                   'Content-Type': 'application/json'
                 }
               )
           
               if response.status == 429:
                 print(f"Rate limited on {table} query. Stopping pagination.")
                 break
           
               if response.status != 200:
                 print(f"{table} query failed: {response.status} - "
                     f"{response.data.decode('utf-8')}")
                 break
           
               page_results = json.loads(response.data.decode('utf-8'))
           
               if not page_results:
                 break
           
               all_records.extend(page_results)
               print(f"{table} page {page + 1}: {len(page_results)} records "
                   f"(total: {len(all_records)})")
           
               if len(page_results) < PAGE_SIZE:
                 break
           
               offset += PAGE_SIZE
           
             return all_records
           
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
**Name** | `metabase-audit-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `metabase-audit-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (`metabase-audit-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `metabase-audit-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Table audit_log: fetched X records
         Table view_log: fetched X records
         Table query_execution: fetched X records
         Wrote X records to gs://metabase-audit-logs/metabase-audit/metabase_audit_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on `metabase-audit-logs`.

  10. Navigate to the `metabase-audit/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Verify the `METABASE_API_KEY` environment variable is correct and the key has not been deleted or regenerated
  * **HTTP 403** : Verify the API key's group has query permissions for the application database
  * **HTTP 429** : Rate limiting -- the function will stop pagination and resume on the next scheduled run
  * **Missing environment variables** : Verify all required variables are set in the Cloud Run function configuration
  * **Empty results** : Verify the `DATABASE_ID` is correct, the application database is added as a data source, and you are using Metabase Pro or Enterprise



## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Metabase Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **METABASE** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://metabase-audit-logs/metabase-audit/
           

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
  2. Click on `metabase-audit-logs`.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Usage analytics tables

The Cloud Run function queries the following tables from the Metabase application database:

Table Name | Description  
---|---  
**audit_log** | Records of configuration changes, user actions, and system events  
**view_log** | Tracks views of cards (questions/models), dashboards, and tables  
**query_execution** | Information about all queries executed across all dashboards  
**Note:** These tables are only populated on Metabase Pro and Enterprise plans. Open Source and Cloud Starter editions do not write activity and view log data.

## Data retention

By default, Metabase retains usage analytics data for 720 days (approximately 2 years). Twice daily, Metabase automatically deletes rows older than this threshold. To change the retention period, set the environment variable `MB_AUDIT_MAX_RETENTION_DAYS` when running Metabase.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
additional | additional | Renamed from additional  
locale | additional.fields | Merged with respective labels (e.g., locale_label for locale, is_active_label for is_active, etc.)  
is_active | additional.fields |   
is_qbnewb | additional.fields |   
group_ids | additional.fields |   
is_superuser | additional.fields |   
login_attributes | additional.fields |   
id | additional.fields |   
sso_source | additional.fields |   
personal_collection_id | additional.fields |   
metadata | metadata | Renamed from metadata  
updated_at | metadata.event_timestamp | Date parsed from updated_at using ISO8601, RFC 3339, or yyyy-MM-ddTHH:mm:ss.SSSSSSZ  
has_userid | metadata.event_type | Set to "USER_UNCATEGORIZED" if has_userid == "true", else "GENERIC_EVENT"  
principal | principal | Renamed from principal  
metabase_host | principal.url | Value copied directly  
date_joined | principal.user.attribute.creation_time | Date parsed from date_joined using ISO8601, RFC 3339, or yyyy-MM-ddTHH:mm:ss.SSSSSSZ  
email | principal.user.email_addresses | Merged from email  
first_name | principal.user.first_name | Value copied directly  
last_login | principal.user.last_login_time | Date parsed from last_login using ISO8601, RFC 3339, or yyyy-MM-ddTHH:mm:ss.SSSSSSZ  
last_name | principal.user.last_name | Value copied directly  
common_name | principal.user.user_display_name | Value copied directly  
email | principal.user.userid | Value copied directly from email  
security_result | security_result | Merged from security_result  
target | target | Renamed from target  
metadata.product_name | metadata.product_name | Set to "METABASE"  
metadata.vendor_name | metadata.vendor_name | Set to "METABASE"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/metabase-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
