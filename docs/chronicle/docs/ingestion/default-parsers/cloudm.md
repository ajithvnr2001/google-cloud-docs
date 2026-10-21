---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudm/
title: Collect CloudM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:44:02.205102+00:00
---

# Collect CloudM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CloudM logs

**Parser Version:** 6.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest CloudM logs into Google Security Operations using Google Cloud Storage V2.

CloudM is a SaaS platform for Google Workspace and Microsoft 365 that provides workflow automation for user onboarding and offboarding, data backup, archival, and migration. CloudM Automate generates a full audit log of all actions performed across your domain, including user management events, offboarding workflow steps, configuration changes, and security-related operations. Audit log data from the last year is preserved.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage Cloud Storage buckets
  * Permissions to manage Identity and Access Management (IAM) policies on Cloud Storage buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Administrator access to your CloudM Automate instance with the **Edit Global Settings** permission
  * Your CloudM Automate instance URL (for example, `yourcompany.cloudm.io`)
  * Your CloudM domain ID



## Collect CloudM Automate credentials

### Create a custom role for API log access

  1. Sign in to your **CloudM Automate** instance.
  2. Go to **Settings > Roles**.
  3. Click **Add Role** to create a new role.
  4. In the **Role Name** field, enter a descriptive name (for example, `Google SecOps Log Reader`).
  5. In the permissions list, enable the following permission:

     * **View Logs** : Grants the ability to view all application logs.
  6. Save the role.

**Note:** The **View Logs** permission provides access to the full audit logs. Don't enable **View Own Logs** , as it only provides access to the service account's own actions, which don't include the domain-wide audit events needed for SIEM ingestion.



### Create a service account and assign the role

  1. In **CloudM Automate** , go to **Settings > Roles**.
  2. Create or identify a service account to be used for API access.
  3. Assign the **Google SecOps Log Reader** role to the service account.
  4. Ensure the role is assigned with **global** scope so the service account can access logs across the entire domain.



### Obtain the service account access token

  1. Generate an access token for the service account.
  2. The access token is used as a Bearer token in the `Authorization` header when making API requests to the CloudM Logs API.
  3. Record the following values:

     * **Automate Instance URL** : Your CloudM Automate instance URL (for example, `yourcompany.cloudm.io`)
     * **Domain ID** : Your CloudM domain identifier
     * **Service Account Access Token** : The Bearer token for API authentication



### Verify permissions

To verify that the account has the required permissions:

  1. Sign in to **CloudM Automate**.
  2. Go to **Settings > Roles**.
  3. Verify the service account has the **View Logs** permission assigned with global scope.
  4. If you cannot see this option, contact your administrator to grant the **Edit Global Settings** and **View Logs** permissions.



### Test API access

  * Test your credentials before you proceed with the integration:
        
        # Replace with your actual credentials
        CLOUDM_INSTANCE="yourcompany.cloudm.io"
        DOMAIN_ID="your-domain-id"
        ACCESS_TOKEN="your-access-token"
        
        # Test API access
        curl -v -H "Authorization: Bearer ${ACCESS_TOKEN}" \
          "https://${CLOUDM_INSTANCE}/_ah/api/events/v1/${DOMAIN_ID}?from=$(date -u +%Y-%m-%d)&to=$(date -u +%Y-%m-%d)"
        

A successful response returns a JSON array of audit log events.




## Required API permissions

  * The service account requires the following permission:

Permission | Access Level | Purpose  
---|---|---  
**View Logs** | Global | Retrieve all audit log events from CloudM Automate  
**Note:** Using least-privilege access. Only the **View Logs** read permission is required. Write or administrative permissions are not needed for log ingestion.



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `cloudm-audit-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to the Cloud Storage bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **Google Cloud Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `cloudm-audit-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect CloudM audit logs`
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

     * **Storage Object Admin** : Write logs to Cloud Storage bucket and manage state files
     * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function
     * **Cloud Functions Invoker** : Allow function invocation



### Grant IAM permissions on Cloud Storage bucket

Grant the service account write permissions on the Cloud Storage bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (`cloudm-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details:

     * **Add principals** : Enter the service account email (`cloudm-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.




## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **Google Cloud Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details:

     * **Topic ID** : Enter `cloudm-audit-trigger`
     * Leave other settings as default
  4. Click **Create**.




## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the CloudM Automate Logs API and write them to Cloud Storage.

  1. In the **Google Cloud Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `cloudm-audit-collector`  
**Region** | Select region matching your Cloud Storage bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `cloudm-audit-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `cloudm-audit-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:

Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `cloudm-audit-logs` | Cloud Storage bucket name  
`GCS_PREFIX` | `cloudm-audit` | Prefix for log files  
`STATE_KEY` | `cloudm-audit/state.json` | State file path  
`CLOUDM_INSTANCE_URL` | `yourcompany.cloudm.io` | CloudM Automate instance URL  
`CLOUDM_DOMAIN_ID` | `your-domain-id` | CloudM domain identifier  
`CLOUDM_ACCESS_TOKEN` | `your-access-token` | CloudM service account Bearer token  
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
           
           http = urllib3.PoolManager(
             timeout=urllib3.Timeout(connect=10.0, read=60.0),
             retries=False,
           )
           
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'cloudm-audit')
           STATE_KEY = os.environ.get('STATE_KEY', 'cloudm-audit/state.json')
           CLOUDM_INSTANCE_URL = os.environ.get('CLOUDM_INSTANCE_URL', '').rstrip('/')
           CLOUDM_DOMAIN_ID = os.environ.get('CLOUDM_DOMAIN_ID')
           CLOUDM_ACCESS_TOKEN = os.environ.get('CLOUDM_ACCESS_TOKEN')
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           @functions_framework.cloud_event
           def main(cloud_event):
             if not all([GCS_BUCKET, CLOUDM_INSTANCE_URL, CLOUDM_DOMAIN_ID, CLOUDM_ACCESS_TOKEN]):
               print('Error: Missing required environment variables')
               return
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
               state = load_state(bucket)
               now = datetime.now(timezone.utc)
           
               if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_event_date'):
                 try:
                   last_date = state['last_event_date']
                   last_time = datetime.strptime(last_date, '%Y-%m-%d').replace(tzinfo=timezone.utc)
                 except Exception as e:
                   print(f"Warning: Could not parse last_event_date: {e}")
                   last_time = now - timedelta(hours=LOOKBACK_HOURS)
               else:
                 last_time = now - timedelta(hours=LOOKBACK_HOURS)
           
               from_date = last_time.strftime('%Y-%m-%d')
               to_date = now.strftime('%Y-%m-%d')
           
               print(f"Fetching logs from {from_date} to {to_date}")
           
               records = fetch_logs(from_date, to_date)
           
               if not records:
                 print("No new log records found.")
                 save_state(bucket, to_date)
                 return
           
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/cloudm_audit_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join(
                 [json.dumps(record, ensure_ascii=False, default=str) for record in records]
               ) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
               print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
           
               save_state(bucket, to_date)
           
               print(f"Successfully processed {len(records)} records")
           
             except Exception as e:
               print(f'Error processing logs: {str(e)}')
               raise
           
           def fetch_logs(from_date, to_date):
             instance = CLOUDM_INSTANCE_URL
             if not instance.startswith('https://'):
               instance = f"https://{instance}"
           
             endpoint = f"{instance}/_ah/api/events/v1/{CLOUDM_DOMAIN_ID}"
           
             headers = {
               'Authorization': f'Bearer {CLOUDM_ACCESS_TOKEN}',
               'Accept': 'application/json',
               'User-Agent': 'GoogleSecOps-CloudMCollector/1.0'
             }
           
             url = f"{endpoint}?from={from_date}&to={to_date}"
           
             try:
               response = http.request('GET', url, headers=headers)
           
               if response.status == 429:
                 retry_after = int(response.headers.get('Retry-After', '60'))
                 print(f"Rate limited (429). Retry after {retry_after}s.")
                 return []
           
               if response.status != 200:
                 print(f"HTTP Error: {response.status}")
                 response_text = response.data.decode('utf-8')
                 print(f"Response body: {response_text}")
                 return []
           
               data = json.loads(response.data.decode('utf-8'))
           
               if isinstance(data, list):
                 records = data
               elif isinstance(data, dict):
                 records = data.get('items', data.get('events', [data]))
               else:
                 records = []
           
               print(f"Retrieved {len(records)} events")
               return records
           
             except Exception as e:
               print(f"Error fetching logs: {e}")
               return []
           
           def load_state(bucket):
             try:
               blob = bucket.blob(STATE_KEY)
               if blob.exists():
                 return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
             except Exception as e:
               print(f"Warning: Could not load state: {e}")
             return {}
           
           def save_state(bucket, last_event_date):
             try:
               state = {
                 'last_event_date': last_event_date,
                 'last_run': datetime.now(timezone.utc).isoformat()
               }
               blob = bucket.blob(STATE_KEY)
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 json.dumps(state, indent=2),
                 content_type='application/json'
               )
               print(f"Saved state: last_event_date={last_event_date}")
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

  1. In the **Google Cloud Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `cloudm-audit-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `cloudm-audit-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Test the integration

  1. In the **Cloud Scheduler** console, find your job (`cloudm-audit-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `cloudm-audit-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DD to YYYY-MM-DD
         Retrieved X events
         Wrote X records to gs://cloudm-audit-logs/cloudm-audit/cloudm_audit_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on `cloudm-audit-logs`.

  10. Navigate to the `cloudm-audit/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Verify that the `CLOUDM_ACCESS_TOKEN` environment variable is correct.
  * **HTTP 403** : Verify that the service account has the **View Logs** permission with global scope.
  * **HTTP 429** : Rate limiting—the function will stop and resume on the next scheduled run.
  * **Missing environment variables** : Verify all required variables are set in the Cloud Run function configuration



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your Cloud Storage bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `CloudM Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **CloudM** as the **Log type**.
  7. Click **Get Service Account**. 

A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
           
           gs://cloudm-audit-logs/cloudm-audit/
           

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of **Storage Object Viewer**. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your Cloud Storage bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on `cloudm-audit-logs`.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details:

     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of **Storage Object Viewer**.



## CloudM Logs API parameters

The CloudM Logs API supports the following query parameters for filtering log events:

Parameter | Format | Description  
---|---|---  
**byUser** | Email address | Filter events by the user who performed the action (analogous to **User** in the CloudM UI)  
**from** | `yyyy-MM-dd` | Start date for the date range filter  
**to** | `yyyy-MM-dd` | End date for the date range filter  
**contextType** | String | Filter by context type (for example, profile, group, OU)  
**contextName** | String | Filter by the target of an action (for example, a specific user being offboarded)  
**operation** | String | Filter by operation type (for example, assign alias, suspend user)  
**country** | Country code | Filter by geolocation country code  
  
## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
about | about | Value copied directly  
Context_Name | about.labels | Merged as key-value pairs from about_Context_Name, about_Context_Type, labels0  
Context_Type | about.labels |   
Login_Type | about.labels |   
Issuer | additional.fields | Merged from additional_field0, additional_field1, additional_field2  
SAML_code | additional.fields |   
SAML_ACS_Url | additional.fields |   
Operation | extensions.auth.type | Set to SSO if Operation matches SSORequest, AUTHTYPE_UNSPECIFIED if Context_Type is LoginUser  
Context_Type | extensions.auth.type |   
Timestamp | metadata.event_timestamp | Extracted datetime and timezone from Timestamp, timezone converted to offset, concatenated and parsed as timestamp  
Operation | metadata.event_type | Set to USER_UNCATEGORIZED if Operation matches Update/Delete/SuspendUser/UnsuspendUser/Create, USER_LOGIN if Operation matches SSORequest/SSORequestFail or Context_Type is LoginUser, STATUS_UPDATE if IP not empty, else GENERIC_EVENT  
Context_Type | metadata.event_type |   
User_Agent | network.http.user_agent | Value copied directly  
principal | principal | Renamed from principal if Context_Type != LoginUser, else from target  
target | principal |   
Organization_Unit | principal.administrative_domain | Value copied directly  
IP | principal.ip | Value copied directly  
City | principal.location.city | Value copied directly  
Country | principal.location.country_or_region | Value copied directly  
Geolocation | principal.location.region_latitude | Extracted latitude from Geolocation using grok  
Geolocation | principal.location.region_longitude | Extracted longitude from Geolocation using grok  
Region | principal.location.state | Value copied directly  
Actor | principal.user.attribute.roles | Set to role.name if Actor not email and not empty, then merged  
Actor | principal.user.email_addresses | Value copied directly if Actor matches email regex  
Message | principal.user.userid | Extracted username from Message using grok  
security_result | security_result | Merged the security_result object  
SAML_code | security_result.action | Set to ALLOW if SAML_code matches Success, BLOCK if RequestDenied  
Message | security_result.description | Value copied directly  
Severity | security_result.severity | Set to uppercase if Error/Critical, INFORMATIONAL if Info, MEDIUM if Warning, else UNKNOWN_SEVERITY  
Operation | security_result.summary | Value copied directly  
target | target | Renamed from target if Context_Type != LoginUser, else from principal  
principal | target |   
metadata.product_name | metadata.product_name | Set to "CLOUDM"  
metadata.vendor_name | metadata.vendor_name | Set to "CLOUDM"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudm-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
