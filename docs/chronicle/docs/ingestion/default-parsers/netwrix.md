---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netwrix/
title: Collect Netwrix Auditor logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:20:27.451494+00:00
---

# Collect Netwrix Auditor logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netwrix/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Netwrix Auditor logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest Netwrix Auditor logs to Google Security Operations using Google Cloud Storage V2.

Netwrix Auditor is a visibility platform for user behavior analysis and risk mitigation that enables control over changes, configurations and access in hybrid IT environments. The platform provides security analytics to detect anomalies in user behavior and investigate threat patterns before a data breach occurs. Empowered with a RESTful Integration API, the platform delivers visibility and control across all of your on-premises or cloud-based IT systems in a unified way.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage, Cloud Run, Pub/Sub, and Cloud Scheduler APIs enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Administrative access to Netwrix Auditor Server
  * A Windows domain account with appropriate permissions for API access
  * Netwrix Auditor Server with Integration API enabled (enabled by default)
  * Audit Database configured in Netwrix Auditor
  * Network connectivity from the Cloud Run function to Netwrix Auditor Server on port 9699 (default)



## Configure Netwrix Auditor API access

To enable the Cloud Run function to retrieve activity records, you need to verify that the Integration API is enabled and create a Windows domain account with the appropriate role in Netwrix Auditor.

### Verify Integration API is enabled

  1. On the computer where Netwrix Auditor Server is installed, launch **Netwrix Auditor**.
  2. Navigate to **Settings > Integrations**.
  3. Verify that the **Leverage Integration API** option is enabled.
  4. Note the **Port** number (default is `9699`).
  5. If you need to change the port:

     1. Click **Modify** under the **API settings** section.
     2. Specify a new port number.
     3. Click **OK**.
**Note:** Netwrix Auditor Integration API is enabled by default and communicates through port 9699 over HTTPS using an automatically generated certificate.



### Create a service account for API access

  1. On your Windows domain controller, open **Active Directory Users and Computers**.
  2. Navigate to the organizational unit where you want to create the service account.
  3. Right-click the organizational unit > **New > User**.
  4. In the **First name** field, enter `Chronicle Integration`.
  5. In the **User logon name** field, enter `chronicle-api` (or your preferred username).
  6. Click **Next**.
  7. Enter a strong password and configure password settings according to your organization's policy.
  8. Clear the **User must change password at next logon** checkbox.
  9. Select **Password never expires** (recommended for service accounts).
  10. Click **Next** > **Finish**.



### Assign Global reviewer role

  1. In the Netwrix Auditor main window, navigate to **Monitoring Plans**.
  2. In the monitoring plans tree, select **All monitoring plans** (the root folder).
  3. Click **Delegate**.
  4. In the **Delegation** dialog, click **Add User**.
  5. In the **Select User or Group** dialog: 
     1. Click **Browse**.
     2. In the **Enter the object name to select** field, enter the username `chronicle-api`.
     3. Click **Check Names** to verify the account.
     4. Click **OK**.
  6. In the **Role** dropdown, select **Global reviewer**.
  7. Click **OK**.
  8. Click **Save**.

**Note:** The Global reviewer role provides read-only access to all activity records collected by Netwrix Auditor. This role is the minimum required for retrieving activity records through the Integration API.



### Record API credentials

Record the following information for configuring the Cloud Run function environment variables:

  * **Username** : The domain account in the format `DOMAIN\username` (for example, `ENTERPRISE\chronicle-api`)
  * **Password** : The password for the service account
  * **Hostname** : The fully qualified domain name (FQDN) or IP address of the Netwrix Auditor Server (for example, `auditor.enterprise.local` or `172.28.6.15`)
  * **Port** : The Integration API port (default is `9699`)

**Note:** If NTLM authentication is disabled through a group policy, you will not be able to address Netwrix Auditor Server by its IP address. In this case, use the fully qualified domain name (FQDN) instead.



### Verify permissions

To verify the account has the required permissions:

  1. In **Netwrix Auditor** , navigate to **Monitoring Plans**.
  2. Select **All monitoring plans**.
  3. Click **Delegate**.
  4. Verify that the `chronicle-api` account appears with the **Global reviewer** role.
  5. If the account does not appear, follow the **Assign Global reviewer role** steps above.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual values
        NETWRIX_HOST="auditor.enterprise.local"
        NETWRIX_PORT="9699"
        NETWRIX_USER="ENTERPRISE\\chronicle-api"
        NETWRIX_PASS="your-password"
        
        # Test API access (retrieve first batch of activity records)
        curl -k --ntlm -u "${NETWRIX_USER}:${NETWRIX_PASS}" \
            "https://${NETWRIX_HOST}:${NETWRIX_PORT}/netwrix/api/v1/activity_records/enum" \
            -H "Content-Type: application/json" \
            -H "Accept: application/json"
        




A successful response returns a JSON object containing an array of activity records and a ContinuationMark for pagination.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `netwrix-auditor-logs`)  
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
     * **Service account name** : Enter `netwrix-audit-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Netwrix Auditor logs`
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
  2. Click on your bucket name (`netwrix-auditor-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`netwrix-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `netwrix-audit-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch activity records from the Netwrix Auditor Integration API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `netwrix-audit-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `netwrix-audit-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `netwrix-audit-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `netwrix-auditor-logs` | GCS bucket name  
`GCS_PREFIX` | `netwrix-audit` | Prefix for log files  
`STATE_KEY` | `netwrix-audit/state.json` | State file path  
`NETWRIX_HOST` | `auditor.enterprise.local` | Netwrix Auditor Server FQDN or IP  
`NETWRIX_PORT` | `9699` | Integration API port  
`NETWRIX_USER` | `ENTERPRISE\chronicle-api` | Domain account in DOMAIN\username format  
`NETWRIX_PASS` | `your-password` | Service account password  
`MAX_RECORDS` | `10000` | Max records per run  
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

**Note:** The Cloud Run function must have network connectivity to the Netwrix Auditor Server. If the Netwrix Auditor Server is on-premises, configure a VPC connector or Cloud VPN to allow the Cloud Run function to reach the server on port 9699.



### Add function code

  1. Enter **main** in the **Entry point** field.
  2. In the inline code editor, create two files:

     * **main.py:**
    
    import functions_framework
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import json
    import os
    import requests
    from requests_ntlm import HttpNtlmAuth
    from datetime import datetime, timezone, timedelta
    import time
    import urllib3
    
    # Suppress insecure HTTPS warnings for self-signed certificates
    urllib3.disable_warnings(urllib3.[exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html).InsecureRequestWarning)
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    # Environment variables
    GCS_BUCKET = os.environ.get('GCS_BUCKET')
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'netwrix-audit')
    STATE_KEY = os.environ.get('STATE_KEY', 'netwrix-audit/state.json')
    NETWRIX_HOST = os.environ.get('NETWRIX_HOST')
    NETWRIX_PORT = os.environ.get('NETWRIX_PORT', '9699')
    NETWRIX_USER = os.environ.get('NETWRIX_USER')
    NETWRIX_PASS = os.environ.get('NETWRIX_PASS')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
    def parse_datetime(value):
      """Parse ISO datetime string to datetime object."""
      if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
        value = value[:-1] + "+00:00"
      return datetime.fromisoformat(value)
    
    @functions_framework.cloud_event
    def main(cloud_event):
      """
      Cloud Run function triggered by Pub/Sub to fetch Netwrix Auditor
      activity records and write to GCS.
    
      Args:
        cloud_event: CloudEvent object containing Pub/Sub message
      """
    
      if not all([GCS_BUCKET, NETWRIX_HOST, NETWRIX_USER, NETWRIX_PASS]):
        print('Error: Missing required environment variables')
        return
    
      try:
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
        state = load_state(bucket)
        now = datetime.now(timezone.utc)
    
        if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_event_time'):
          try:
            last_time = parse_datetime(state['last_event_time'])
            last_time = last_time - timedelta(minutes=2)
          except Exception as e:
            print(f"Warning: Could not parse last_event_time: {e}")
            last_time = now - timedelta(hours=LOOKBACK_HOURS)
        else:
          last_time = now - timedelta(hours=LOOKBACK_HOURS)
    
        print(f"Fetching activity records from {last_time.isoformat()} "
            f"to {now.isoformat()}")
    
        records, newest_event_time = fetch_activity_records(
          last_time, now
        )
    
        if not records:
          print("No new activity records found.")
          save_state(bucket, now.isoformat())
          return
    
        timestamp = now.strftime('%Y%m%d_%H%M%S')
        object_key = (
          f"{GCS_PREFIX}/netwrix_audit_{timestamp}.ndjson"
        )
        blob = bucket.blob(object_key)
    
        ndjson = '\n'.join(
          [json.dumps(r, ensure_ascii=False, default=str)
          for r in records]
        ) + '\n'
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
          ndjson, content_type='application/x-ndjson'
        )
    
        print(f"Wrote {len(records)} records to "
            f"gs://{GCS_BUCKET}/{object_key}")
    
        if newest_event_time:
          save_state(bucket, newest_event_time)
        else:
          save_state(bucket, now.isoformat())
    
        print(f"Successfully processed {len(records)} records")
    
      except Exception as e:
        print(f'Error processing activity records: {str(e)}')
        raise
    
    def load_state(bucket):
      """Load state from GCS."""
      try:
        blob = bucket.blob(STATE_KEY)
        if blob.exists():
          return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
      except Exception as e:
        print(f"Warning: Could not load state: {e}")
      return {}
    
    def save_state(bucket, last_event_time_iso):
      """Save the last event timestamp to GCS state file."""
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
    
    def fetch_activity_records(start_time, end_time):
      """
      Fetch activity records from Netwrix Auditor Integration API
      using the enum endpoint with continuation mark pagination.
    
      The API returns up to 1000 records per request. Subsequent
      requests include the ContinuationMark from the previous
      response to retrieve the next batch.
    
      Args:
        start_time: Start time for filtering records
        end_time: End time for filtering records
    
      Returns:
        Tuple of (records list, newest_event_time ISO string)
      """
      base_url = (
        f"https://{NETWRIX_HOST}:{NETWRIX_PORT}"
        f"/netwrix/api/v1/activity_records/enum"
      )
      auth = HttpNtlmAuth(NETWRIX_USER, NETWRIX_PASS)
      session = requests.Session()
      session.auth = auth
      session.verify = False
      session.headers.update({
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'GoogleSecOps-NetwrixCollector/1.0'
      })
    
      all_records = []
      newest_time = None
      continuation_mark = None
      page_num = 0
      backoff = 1.0
    
      while True:
        page_num += 1
    
        if len(all_records) >= MAX_RECORDS:
          print(f"Reached max_records limit ({MAX_RECORDS})")
          break
    
        try:
          if continuation_mark:
            response = session.post(
              base_url,
              json={"ContinuationMark": continuation_mark},
              timeout=(10, 60)
            )
          else:
            response = session.get(
              base_url,
              timeout=(10, 60)
            )
    
          if response.status_code == 429:
            retry_after = int(
              response.headers.get(
                'Retry-After', str(int(backoff))
              )
            )
            print(f"Rate limited (429). Retrying after "
                f"{retry_after}s...")
            time.sleep(retry_after)
            backoff = min(backoff * 2, 30.0)
            continue
    
          backoff = 1.0
    
          if response.status_code != 200:
            print(f"HTTP Error: {response.status_code}")
            print(f"Response body: {response.text}")
            return all_records, newest_time
    
          data = response.json()
    
          page_results = data.get('ActivityRecordList', [])
          continuation_mark = data.get('ContinuationMark')
    
          if not page_results:
            print("No more activity records (empty page)")
            break
    
          # Filter records by time window
          filtered = []
          for record in page_results:
            when = record.get('When')
            if when:
              try:
                record_time = parse_datetime(when)
                if start_time <= record_time <= end_time:
                  filtered.append(record)
                if (newest_time is None or
                    record_time >
                    parse_datetime(newest_time)):
                  newest_time = when
              except Exception as e:
                print(f"Warning: Could not parse "
                    f"record time: {e}")
                filtered.append(record)
            else:
              filtered.append(record)
    
          print(f"Page {page_num}: Retrieved "
              f"{len(page_results)} records, "
              f"{len(filtered)} within time window")
          all_records.extend(filtered)
    
          if not continuation_mark:
            print("No more pages (no ContinuationMark)")
            break
    
        except requests.[exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html).Timeout:
          print(f"Request timeout on page {page_num}")
          return all_records, newest_time
        except Exception as e:
          print(f"Error fetching activity records: {e}")
          return all_records, newest_time
    
      print(f"Retrieved {len(all_records)} total records "
          f"from {page_num} pages")
      return all_records, newest_time
    

     * **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    requests>=2.31.0
    requests-ntlm>=1.2.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create Cloud Scheduler job

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `netwrix-audit-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `netwrix-audit-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (`netwrix-audit-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `netwrix-audit-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching activity records from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X records, X within time window
         Wrote X records to gs://netwrix-auditor-logs/netwrix-audit/netwrix_audit_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on `netwrix-auditor-logs`.

  10. Navigate to the `netwrix-audit/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Verify the `NETWRIX_USER` and `NETWRIX_PASS` environment variables are correct and use the `DOMAIN\username` format
  * **HTTP 403** : Verify the service account has the **Global reviewer** role in Netwrix Auditor
  * **HTTP 429** : Rate limiting -- the function will automatically retry with exponential backoff
  * **Connection timeout** : Verify network connectivity from Cloud Run to the Netwrix Auditor Server on port 9691. Ensure a VPC connector or Cloud VPN is configured if the server is on-premises
  * **Missing environment variables** : Verify all required variables are set in the Cloud Run function configuration



## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Netwrix Auditor Activity Records`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Netwrix** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed. For example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://netwrix-auditor-logs/netwrix-audit/
           

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of **Storage Object Viewer**. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  12. Click **Next**.

  13. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

  1. Go to **Cloud Storage > Buckets**.
  2. Click on `netwrix-auditor-logs`.
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
Opcode | about.labels | Labels associated with the about information  
Caption | about.resource.attribute.labels | Attribute labels for the resource in the about section  
Task | additional.fields | Additional fields containing extra information about the event  
What | additional.fields |   
Notice | additional.fields |   
Description | additional.fields |   
Added | additional.fields |   
Removed | additional.fields |   
service_type | additional.fields |   
Details | additional.fields |   
extensions.auth.type | extensions.auth.type | Type of authentication used  
EventReceivedTime | metadata.collected_timestamp | Timestamp when the event was collected by the system  
Message | metadata.description | Description of the event  
event_type | metadata.event_type | Type of event  
EventType | metadata.product_event_type | Product-specific event type  
EventID | metadata.product_log_id | Product-specific log identifier  
SourceModuleType | observer.application | Application that observed the event  
Hostname | principal.asset.hostname | Hostname of the asset associated with the principal  
Where | principal.asset.hostname |   
Workstation | principal.asset.hostname |   
device_name | principal.asset.hostname |   
Workstation | principal.hostname | Hostname of the principal  
device_name | principal.hostname |   
ProcessID | principal.process.pid | Process ID of the principal  
Name | principal.resource.name | Name of the resource associated with the principal  
Who | principal.user.user_display_name | Display name of the user  
SourceName | security_result.about.resource.attribute.labels | Resource attribute labels for the about in security result  
action | security_result.action | Action taken in the security result  
action_details | security_result.action_details | Details of the action in the security result  
backup_name | security_result.description | Description of the security result  
service_failed | security_result.description |   
Keywords | security_result.detection_fields | Fields used for detection in the security result  
RecordNumber | security_result.detection_fields |   
session_ID | security_result.detection_fields |   
allow_connection_with_desktop | security_result.detection_fields |   
service_account | security_result.detection_fields |   
Severity | security_result.severity | Severity level of the security result  
SeverityValue | security_result.severity |   
summary | security_result.summary | Summary of the security result  
application_name | target.application | Application on the target  
Hostname | target.asset.hostname | Hostname of the asset associated with the target  
Where | target.asset.hostname |   
file_path | target.file.full_path | Full path of the target file  
Size | target.file.size | Size of the target file  
Hostname | target.hostname | Hostname of the target  
Where | target.hostname |   
Type | target.resource.attribute.labels | Attribute labels for the target resource  
SourceModuleName | target.resource.name | Name of the target resource  
DataSource | metadata.product_name | Name of the product that generated the event  
metadata.vendor_name | metadata.vendor_name | Name of the vendor  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netwrix-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
