---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forgerock-openidm/
title: Collect PingIDM (formerly ForgeRock OpenIDM) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:06.521606+00:00
---

# Collect PingIDM (formerly ForgeRock OpenIDM) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forgerock-openidm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect PingIDM (formerly ForgeRock OpenIDM) logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest PingIDM (formerly known as ForgeRock OpenIDM) logs to Google Security Operations using Google Cloud Storage V2.

PingIDM is an identity management platform that provides user provisioning, synchronization, password management, and access governance. It logs identity lifecycle events, authentication attempts, reconciliation operations, and configuration changes to audit logs accessible over REST.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance.
  * A GCP project with the Cloud Storage API enabled.
  * Permissions to create and manage GCS buckets and IAM policies.
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs.
  * Privileged access to a ForgeRock OpenIDM or PingIDM instance with administrative credentials.



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage** > **Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (e.g., `forgerock-openidm-audit-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (e.g., `us-central1`)  
**Storage class** | **Standard** (recommended for frequently accessed logs)  
**Access control** | **Uniform** (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect ForgeRock OpenIDM credentials

### Get ForgeRock OpenIDM base URL

  1. Sign in to your ForgeRock OpenIDM or PingIDM instance.
  2. Note your base URL from the browser address bar. 
     * Format: `https://openidm.example.com`
     * Do not include trailing slashes or paths like `/admin`.



### Get administrative credentials

  1. Obtain administrative credentials for your ForgeRock OpenIDM instance.
  2. You will need: 
     * **Username** : Administrative username (e.g., `openidm-admin`)
     * **Password** : Administrative password

**Note:** The user account must have permissions to query audit logs via the REST API. The default `openidm-admin` user has these permissions.

### Verify permissions

  1. Sign in to ForgeRock OpenIDM.
  2. Go to **Configure** > **System Preferences** > **Audit**.
  3. If you can see audit configuration and topics, you have the required permissions.
  4. If you cannot see this option, contact your administrator to grant audit read permissions.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        OPENIDM_BASE_URL="[https://openidm.example.com](https://openidm.example.com)"
        OPENIDM_USERNAME="openidm-admin"
        OPENIDM_PASSWORD="your-admin-password"
        
        # Test API access to authentication audit topic
        curl -v \
            -H "X-OpenIDM-Username: ${OPENIDM_USERNAME}" \
            -H "X-OpenIDM-Password: ${OPENIDM_PASSWORD}" \
            -H "Accept-API-Version: resource=1.0" \
            -H "Accept: application/json" \
            "${OPENIDM_BASE_URL}/openidm/audit/authentication?_queryFilter=true&_pageSize=1"
        




**Expected response** : HTTP 200 with JSON containing audit events.

**Note:** The `/openidm/audit` REST query endpoint is deprecated in PingIDM 8.x and may be removed in future releases. Monitor PingIDM release notes for alternative export methods.

## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to the GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin** > **Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : `forgerock-openidm-collector-sa`
     * **Service account description** : `Service account for Cloud Run function to collect ForgeRock OpenIDM logs`
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section, add the following roles: 
     1. **Storage Object Admin** : To write logs to the GCS bucket and manage state files.
     2. **Cloud Run Invoker** : To allow Pub/Sub to invoke the function.
     3. **Cloud Functions Invoker** : To allow function invocation.
  6. Click **Continue** then **Done**.



### Grant IAM permissions on GCS bucket

  1. Go to **Cloud Storage** > **Buckets**.
  2. Click on your bucket name (e.g., `forgerock-openidm-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (e.g., `forgerock-openidm-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

  1. In the **GCP Console** , go to **Pub/Sub** > **Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : `forgerock-openidm-trigger`
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `forgerock-openidm-collector`  
**Region** | Select region matching your GCS bucket (e.g., `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `forgerock-openidm-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `forgerock-openidm-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `forgerock-openidm-audit-logs` | GCS bucket name  
`GCS_PREFIX` | `openidm` | Prefix for log files  
`STATE_KEY` | `openidm/state.json` | State file path  
`OPENIDM_BASE_URL` | `https://openidm.example.com` | OpenIDM base URL  
`OPENIDM_USERNAME` | `openidm-admin` | OpenIDM admin username  
`OPENIDM_PASSWORD` | `your-admin-password` | OpenIDM admin password  
`AUDIT_TOPICS` | `access,activity,authentication,config,sync` | Comma-separated topics  
`PAGE_SIZE` | `100` | Records per page  
`MAX_PAGES` | `50` | Max pages per topic  
  10. In the **Requests** section:

     * **Request timeout** : `600` seconds.
  11. Go to the **Settings** tab:

     * **Resources** : **512 MiB** memory, **1** CPU.
  12. Click **Create**. After the service is created, the **inline code editor** will open.




### Add function code

  1. Enter **main** in the **Entry point** field.
  2. Create two files in the editor:

     * **main.py:**
    
    import functions_framework
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import json
    import os
    import urllib3
    from datetime import datetime, timezone
    
    # Initialize HTTP client with timeouts
    http = urllib3.PoolManager(
        timeout=urllib3.Timeout(connect=5.0, read=30.0),
        retries=False,
    )
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    # Environment variables
    GCS_BUCKET = os.environ.get('GCS_BUCKET')
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'openidm')
    STATE_KEY = os.environ.get('STATE_KEY', 'openidm/state.json')
    OPENIDM_BASE_URL = os.environ.get('OPENIDM_BASE_URL')
    OPENIDM_USERNAME = os.environ.get('OPENIDM_USERNAME')
    OPENIDM_PASSWORD = os.environ.get('OPENIDM_PASSWORD')
    AUDIT_TOPICS = os.environ.get('AUDIT_TOPICS', 'access,activity,authentication,config,sync').split(',')
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '100'))
    MAX_PAGES = int(os.environ.get('MAX_PAGES', '50'))
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch ForgeRock OpenIDM logs and write to GCS.
        """
        if not all([GCS_BUCKET, OPENIDM_BASE_URL, OPENIDM_USERNAME, OPENIDM_PASSWORD]):
            print('Error: Missing required environment variables')
            return
    
        try:
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
            state = load_state(bucket, STATE_KEY)
    
            all_events = []
            for topic in AUDIT_TOPICS:
                topic = topic.strip()
                print(f"Fetching audit logs for topic: {topic}")
                events = fetch_audit_logs(topic, [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get(topic, {}))
                all_events.extend(events)
    
                if events:
                    latest_timestamp = max(e.get('timestamp', '') for e in events)
                    state[topic] = {
                        'last_timestamp': latest_timestamp,
                        'last_run': datetime.now(timezone.utc).isoformat(),
                        'events_count': len(events)
                    }
    
            if all_events:
                write_to_gcs(bucket, all_events)
                save_state(bucket, STATE_KEY, state)
                print(f"Successfully processed {len(all_events)} audit events")
            else:
                print("No new audit events to process")
    
        except Exception as e:
            print(f'Error processing logs: {str(e)}')
            raise
    
    def load_state(bucket, key):
        try:
            blob = bucket.blob(key)
            if blob.exists():
                return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
        except Exception as e:
            print(f"Warning: Could not load state: {e}")
        return {}
    
    def save_state(bucket, key, state):
        try:
            blob = bucket.blob(key)
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(json.dumps(state, indent=2), content_type='application/json')
        except Exception as e:
            print(f"Warning: Could not save state: {e}")
    
    def fetch_audit_logs(topic, topic_state):
        base_url = OPENIDM_BASE_URL.rstrip('/')
        all_events = []
        last_timestamp = topic_state.get('last_timestamp')
        query_filter = 'true' if not last_timestamp else f'timestamp gt "{last_timestamp}"'
        page_offset = 0
        page_count = 0
    
        while page_count < MAX_PAGES:
            try:
                url = f"{base_url}/openidm/audit/{topic}"
                params = {
                    '_queryFilter': query_filter,
                    '_pageSize': str(PAGE_SIZE),
                    '_pagedResultsOffset': str(page_offset),
                    '_sortKeys': 'timestamp'
                }
    
                headers = {
                    'X-OpenIDM-Username': OPENIDM_USERNAME,
                    'X-OpenIDM-Password': OPENIDM_PASSWORD,
                    'Accept-API-Version': 'resource=1.0',
                    'Accept': 'application/json'
                }
    
                response = http.request('GET', url, fields=params, headers=headers)
                if response.status != 200:
                    print(f"API error for topic {topic}: {response.status}")
                    break
    
                data = json.loads(response.data.decode('utf-8'))
                events = data.get('result', [])
                if not events:
                    break
    
                all_events.extend(events)
                page_offset += PAGE_SIZE
                page_count += 1
                if len(events) < PAGE_SIZE:
                    break
            except Exception as e:
                print(f"Error for topic {topic}: {str(e)}")
                break
        return all_events
    
    def write_to_gcs(bucket, events):
        timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
        filename = f"{GCS_PREFIX}/openidm_audit_{timestamp}.json"
        ndjson_content = '\n'.join([json.dumps(event) for event in events])
        bucket.blob(filename).[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson_content, content_type='application/x-ndjson')
    

     * **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy**. Deployment takes 2–3 minutes.




## Create Cloud Scheduler job

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `forgerock-openidm-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | **Pub/Sub**  
**Topic** | `forgerock-openidm-trigger`  
**Message body** | `{}`  
  4. Click **Create**.




### Schedule frequency options

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every hour | `0 * * * *` | Standard (recommended)  
Daily | `0 0 * * *` | Batch collection  
  
### Test the integration

  1. In **Cloud Scheduler** , click **Force run** on your job.
  2. Verify the run in **Cloud Run** logs. Look for: `Successfully processed X audit events`.
  3. Confirm a new `json` file exists in your **Cloud Storage** bucket under the `openidm/` folder.



## Retrieve the Google SecOps service account

### Configure a feed in Google SecOps

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed** > **Configure a single feed**.
  3. **Feed name** : `ForgeRock OpenIDM Audit Logs`.
  4. **Source type** : **Google Cloud Storage V2**.
  5. **Log type** : **FORGEROCK_OPENIDM**.
  6. Click **Get Service Account** and copy the email provided (e.g., `chronicle-12345...`).
  7. Click **Next**.
  8. **Storage bucket URL** : `gs://forgerock-openidm-audit-logs/openidm/`.
  9. **Source deletion option** : Select according to preference (e.g., **Never**).
  10. Click **Next** , review, and click **Submit**.



### Grant IAM permissions

  1. Go to **Cloud Storage** > **Buckets**.
  2. Select your bucket and click the **Permissions** tab.
  3. Click **Grant access**.
  4. **Add principals** : Paste the Google SecOps service account email.
  5. **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`fluenttag_label`, `topic_label`, `context_roles_label` | `additional.fields` | Key-value pairs for context.  
`Via` | `intermediary.hostname` | Hostname of the proxy/intermediary.  
`x_forwarded_ip`, `caller.callerIps` | `intermediary.ip` | IP of the intermediary.  
`timestamp` | `metadata.event_timestamp` | Event timestamp.  
`transactionId` | `metadata.product_deployment_id` | Unique transaction ID.  
`eventName` | `metadata.product_event_type` | Event name from ForgeRock.  
`_id` | `metadata.product_log_id` | Unique log identifier.  
`request_method` | `network.http.method` | HTTP method used.  
`response.statusCode` | `network.http.response_code` | HTTP status code.  
`user_agent` | `network.http.user_agent` | Full user agent string.  
`client.ip`, `context.ipAddress` | `principal.ip` | Source IP of the actor.  
`userId`, `principalData.0` | `principal.user.userid` | ID of the acting user.  
`security_action` | `security_result.action` | Security decision taken.  
`level` | `security_result.severity` | Mapped severity level.  
`server.ip` | `target.ip` | IP of the target system.  
`http.request.path` | `target.url` | Target URL/Path.  
N/A | `metadata.product_name` | Set to ForgeRock OpenIDM.  
N/A | `metadata.vendor_name` | Set to ForgeRock.  
`elapsed_time" and "X-Content-Type-Options` | `additional.fields` | Mapped from changelog  
`trackingIds.0` | `metadata.product_log_id` | Mapped from changelog  
`context.userRolesProperty", "context.authenticationId", and "context.authenticationIdProperty` | `principal.user.attribute.roles` | Mapped from changelog  
`context.component", "context.moduleId", and "context.queryId` | `principal.resource.attribute.labels` | Mapped from changelog  
`context.roles", "_normalized.fieldNames", and "_eventId` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forgerock-openidm-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
