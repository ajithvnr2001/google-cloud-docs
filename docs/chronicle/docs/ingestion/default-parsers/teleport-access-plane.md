---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/teleport-access-plane/
title: Collect Teleport Access Plane logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:21.638793+00:00
---

# Collect Teleport Access Plane logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/teleport-access-plane/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Teleport Access Plane logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Teleport Access Plane logs to Google Security Operations using Google Cloud Storage V2.

Teleport Access Plane (now Teleport Access Platform) is a zero-trust access platform that provides secure access to SSH servers, Kubernetes clusters, databases, and web applications with built-in session recording, identity-based access controls, and comprehensive audit logging. Audit events can be collected via the Teleport Events API.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * A running Teleport cluster with administrator access
  * Teleport identity files or machine ID credentials for API access



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `teleport-audit-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Teleport Access Plane API credentials

### Generate identity file for API access

Teleport uses identity-based authentication for API access. Generate an identity file or use Machine ID for automated access.

#### Option A: Generate identity file using tctl

  1. Sign in to a machine with `tctl` access to your Teleport cluster.
  2. Create a bot user for the integration:
         
         tctl bots add secops-collector --roles=auditor --logins=root
         

  3. Generate an identity file:
         
         tctl auth sign --user=secops-collector --out=secops-collector-identity --ttl=8760h
         

  4. The identity file `secops-collector-identity` contains the TLS certificate, key, and CA certificates required for API authentication.

**Note:** The `--ttl=8760h` flag creates credentials valid for one year. Rotate credentials before they expire.



#### Option B: Use Machine ID (recommended for production)

  1. Install `tbot` on the machine that will run the collector.
  2. Configure Machine ID:
         
         tctl bots add secops-collector --roles=auditor
         

  3. Start the bot to continuously renew credentials:
         
         tbot start \
           --destination-dir=/opt/teleport/certs \
           --token=secops-collector-token \
           --auth-server=teleport.yourcompany.com:443
         




### Determine Teleport proxy address

  1. Note your Teleport proxy address (for example, `teleport.yourcompany.com:443`).
  2. The API endpoint is the same as the proxy address.

**Note:** If your Teleport cluster uses a separate auth server, use the auth server address instead.



### Verify permissions

To verify the bot user has the required permissions:

  1. Sign in to the Teleport Web UI.
  2. Go to **Management > Users**.
  3. Verify the bot user `secops-collector` exists and has the `auditor` role.
  4. The `auditor` role provides read access to audit events and session recordings.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual values
        TELEPORT_PROXY="teleport.yourcompany.com:443"
        IDENTITY_FILE="/path/to/secops-collector-identity"
        
        # Test API access using tsh
        tsh --proxy=${TELEPORT_PROXY} -i ${IDENTITY_FILE} \
          events ls --last=1h --format=json | head -5
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `teleport-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Teleport Access Plane logs`
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
  2. Click on your bucket name (for example, `teleport-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `teleport-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `teleport-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch audit events from Teleport Events API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `teleport-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `teleport-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `teleport-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `teleport-audit-logs` | GCS bucket name  
`GCS_PREFIX` | `teleport-logs` | Prefix for log files  
`STATE_KEY` | `teleport-logs/state.json` | State file path  
`TELEPORT_PROXY` | `teleport.yourcompany.com:443` | Teleport proxy address  
`TELEPORT_IDENTITY` | `base64-encoded-identity-file` | Base64-encoded identity file content  
`MAX_RECORDS` | `10000` | Max records per run  
`PAGE_SIZE` | `1000` | Records per page  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
  10. In the **Variables & Secrets** section, scroll down to **Requests** :

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

     * **main.py:**
    
    import functions_framework
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import json
    import os
    import urllib3
    from datetime import datetime, timezone, timedelta
    import time
    import base64
    import tempfile
    import ssl
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    # Environment variables
    GCS_BUCKET = os.environ.get('GCS_BUCKET')
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'teleport-logs')
    STATE_KEY = os.environ.get('STATE_KEY', 'teleport-logs/state.json')
    TELEPORT_PROXY = os.environ.get('TELEPORT_PROXY')
    TELEPORT_IDENTITY = os.environ.get('TELEPORT_IDENTITY')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
    def parse_datetime(value: str) -> datetime:
      """Parse ISO datetime string to datetime object."""
      if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
        value = value[:-1] + "+00:00"
      return datetime.fromisoformat(value)
    
    def create_http_client():
      """
      Create an HTTP client with TLS client certificate
      authentication from the Teleport identity file.
      """
      identity_data = base64.b64decode(TELEPORT_IDENTITY).decode('utf-8')
    
      # Parse identity file into cert, key, and CA
      cert_file = tempfile.NamedTemporaryFile(mode='w', suffix='.pem', delete=False)
      key_file = tempfile.NamedTemporaryFile(mode='w', suffix='.pem', delete=False)
      ca_file = tempfile.NamedTemporaryFile(mode='w', suffix='.pem', delete=False)
    
      current_section = None
      cert_data = []
      key_data = []
      ca_data = []
    
      for line in identity_data.split('\n'):
        if 'BEGIN CERTIFICATE' in line and not cert_data:
          current_section = 'cert'
        elif 'BEGIN CERTIFICATE' in line:
          current_section = 'ca'
        elif 'BEGIN' in line and 'KEY' in line:
          current_section = 'key'
        elif 'END CERTIFICATE' in line:
          if current_section == 'cert':
            cert_data.append(line)
          elif current_section == 'ca':
            ca_data.append(line)
          current_section = None
        elif 'END' in line and 'KEY' in line:
          key_data.append(line)
          current_section = None
    
        if current_section == 'cert':
          cert_data.append(line)
        elif current_section == 'key':
          key_data.append(line)
        elif current_section == 'ca':
          ca_data.append(line)
    
      cert_file.write('\n'.join(cert_data))
      cert_file.close()
      key_file.write('\n'.join(key_data))
      key_file.close()
      ca_file.write('\n'.join(ca_data))
      ca_file.close()
    
      http = urllib3.PoolManager(
        cert_file=cert_file.name,
        key_file=key_file.name,
        ca_certs=ca_file.name,
        timeout=urllib3.Timeout(connect=10.0, read=60.0),
        retries=False,
      )
    
      return http
    
    @functions_framework.cloud_event
    def main(cloud_event):
      """
      Cloud Run function triggered by Pub/Sub to fetch Teleport
      audit events and write to GCS.
    
      Args:
        cloud_event: CloudEvent object containing Pub/Sub message
      """
    
      if not all([GCS_BUCKET, TELEPORT_PROXY, TELEPORT_IDENTITY]):
        print('Error: Missing required environment variables')
        return
    
      try:
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
    
        # Load state
        state = load_state(bucket, STATE_KEY)
    
        # Determine time window
        now = datetime.now(timezone.utc)
        last_time = None
    
        if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_event_time"):
          try:
            last_time = parse_datetime(state["last_event_time"])
            # Overlap by 2 minutes to catch any delayed events
            last_time = last_time - timedelta(minutes=2)
          except Exception as e:
            print(f"Warning: Could not parse last_event_time: {e}")
    
        if last_time is None:
          last_time = now - timedelta(hours=LOOKBACK_HOURS)
    
        print(f"Fetching logs from {last_time.isoformat()} to {now.isoformat()}")
    
        # Create HTTP client with TLS auth
        http = create_http_client()
    
        # Fetch logs
        records, newest_event_time = fetch_logs(
          http=http,
          start_time=last_time,
          end_time=now,
          page_size=PAGE_SIZE,
          max_records=MAX_RECORDS,
        )
    
        if not records:
          print("No new log records found.")
          save_state(bucket, STATE_KEY, now.isoformat())
          return
    
        # Write to GCS as NDJSON
        timestamp = now.strftime('%Y%m%d_%H%M%S')
        object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
        blob = bucket.blob(object_key)
    
        ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in records]) + '\n'
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
    
        print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
    
        # Update state with newest event time
        if newest_event_time:
          save_state(bucket, STATE_KEY, newest_event_time)
        else:
          save_state(bucket, STATE_KEY, now.isoformat())
    
        print(f"Successfully processed {len(records)} records")
    
      except Exception as e:
        print(f'Error processing logs: {str(e)}')
        raise
    
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
    
    def save_state(bucket, key, last_event_time_iso: str):
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
    
    def fetch_logs(http, start_time: datetime, end_time: datetime, page_size: int, max_records: int):
      """
      Fetch audit events from Teleport Events API with pagination
      and rate limiting.
    
      Args:
        http: urllib3 PoolManager with TLS client certificates
        start_time: Start time for log query
        end_time: End time for log query
        page_size: Number of records per page
        max_records: Maximum total records to fetch
    
      Returns:
        Tuple of (records list, newest_event_time ISO string)
      """
      proxy_host = TELEPORT_PROXY.rstrip('/')
      if not proxy_host.startswith('https://'):
        proxy_host = f"https://{proxy_host}"
    
      endpoint = f"{proxy_host}/v1/events"
    
      records = []
      newest_time = None
      page_num = 0
      backoff = 1.0
      cursor = ""
    
      start_str = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
      end_str = end_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    
      while True:
        page_num += 1
    
        if len(records) >= max_records:
          print(f"Reached max_records limit ({max_records})")
          break
    
        url = (
          f"{endpoint}"
          f"?from={start_str}"
          f"&to={end_str}"
          f"&limit={min(page_size, max_records - len(records))}"
        )
        if cursor:
          url += f"&startKey={cursor}"
    
        try:
          response = http.request('GET', url)
    
          # Handle rate limiting with exponential backoff
          if response.status == 429:
            retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
            print(f"Rate limited (429). Retrying after {retry_after}s...")
            time.sleep(retry_after)
            backoff = min(backoff * 2, 30.0)
            continue
    
          backoff = 1.0
    
          if response.status != 200:
            print(f"HTTP Error: {response.status}")
            response_text = response.data.decode('utf-8')
            print(f"Response body: {response_text}")
            return [], None
    
          data = json.loads(response.data.decode('utf-8'))
    
          page_results = data.get('items', data.get('events', []))
    
          if not page_results:
            print(f"No more results (empty page)")
            break
    
          print(f"Page {page_num}: Retrieved {len(page_results)} events")
          records.extend(page_results)
    
          # Track newest event time
          for event in page_results:
            try:
              event_time = event.get('time') or event.get('ei', {}).get('time')
              if event_time:
                if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                  newest_time = event_time
            except Exception as e:
              print(f"Warning: Could not parse event time: {e}")
    
          # Check for more results using cursor
          cursor = data.get('startKey', '')
          if not cursor:
            print("No more pages (no startKey cursor)")
            break
    
        except Exception as e:
          print(f"Error fetching logs: {e}")
          return [], None
    
      print(f"Retrieved {len(records)} total records from {page_num} pages")
      return records, newest_time
    

     * **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

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
**Name** | `teleport-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `teleport-logs-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `teleport-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://teleport-audit-logs/teleport-logs/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`teleport-audit-logs`).

  10. Navigate to the `teleport-logs/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401/403** : Check identity file is valid and not expired; verify bot user has `auditor` role
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **TLS errors** : Verify the identity file is correctly base64-encoded and contains cert, key, and CA
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest Teleport Access Plane logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Teleport Access Plane Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Teleport Access Plane** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://teleport-audit-logs/teleport-logs/
           

       * Replace: 
         * `teleport-audit-logs`: Your GCS bucket name.
         * `teleport-logs`: Optional prefix/folder path where logs are stored (leave empty for root).
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
  2. Click on your bucket name.
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
addr_local | principal.ip, principal.asset.ip | Source IP address of the connection  
addr_remote | target.ip | Destination IP address of the connection  
addr_remote1 | principal.ip, principal.asset.ip | Source IP address of the connection  
argv | target.process.command_line | Command line arguments of the process  
bot_instance_id | principal.asset.product_object_id | Product-specific identifier for the asset  
bot_name | principal.application | Name of the application involved  
caller | principal.resource.attribute.labels | Key-value pairs of attributes for the resource  
cgroup_id | metadata.ingestion_labels | Key-value pairs of labels for ingestion metadata  
cluster_name, fields.cluster_name | target.resource.name | Name of the target resource  
code | additional.fields | Additional key-value pairs of event data  
component | metadata.product_event_type | Product-specific event type  
dst_ip | target.ip | Destination IP address of the connection  
dst_port | target.port | Destination port number of the connection  
ei | additional.fields | Additional key-value pairs of event data  
event | metadata.product_event_type | Product-specific event type  
event _type_ | principal.resource.attribute.labels | Key-value pairs of attributes for the resource  
fields.addr.local | principal.ip, principal.asset.ip | Source IP address of the connection  
fields.addr.remote | principal.ip, principal.asset.ip | Source IP address of the connection  
fields.attributes.Account | principal.resource.id | Identifier for the resource  
fields.attributes.Arn | principal.resource.attribute.labels | Key-value pairs of attributes for the resource  
fields.cluster_name | target.resource.name | Name of the target resource  
fields.code | additional.fields | Additional key-value pairs of event data  
fields.host_id | target.resource.id | Identifier for the target resource  
fields.uid | principal.user.userid | User ID of the principal  
id_id | metadata.product_log_id | Product-specific log identifier  
impersonator | principal.resource.attribute.labels | Key-value pairs of attributes for the resource  
level | security_result.severity | Severity level of the security result  
login | principal.user.user_display_name | Display name of the user  
namespace | principal.namespace | Namespace of the principal  
path | target.file.full_path | Full path of the target file  
pid | target.process.pid | Process ID  
ppid | target.process.parent_process.pid | Parent process ID  
private_key_policy | additional.fields | Additional key-value pairs of event data  
program | target.application | Name of the target application  
role | principal.resource.attribute.labels | Key-value pairs of attributes for the resource  
server_hostname | principal.hostname, principal.asset.hostname | Hostname of the principal asset  
server_id | target.resource.product_object_id, metadata.ingestion_labels | Product-specific identifier for the resource  
server_labels.Environment | target.asset.attribute.labels | Key-value pairs of attributes for the asset  
server_labels.OS | target.asset.attribute.labels | Key-value pairs of attributes for the asset  
server_labels.Role | target.user.attribute.roles | Roles associated with the user  
server_labels.Uptime | additional.fields | Additional key-value pairs of event data  
server_labels.Version | target.asset.attribute.labels | Key-value pairs of attributes for the asset  
server_labels.aws_Name | target.asset.attribute.labels | Key-value pairs of attributes for the asset  
server_labels.aws_application | target.application | Name of the target application  
server_labels.aws_backup | target.asset.attribute.labels | Key-value pairs of attributes for the asset  
server_labels.aws_cost_center | target.asset.attribute.labels | Key-value pairs of attributes for the asset  
server_labels.aws_environment | target.asset.attribute.labels | Key-value pairs of attributes for the asset  
server_labels.aws_role | target.asset.attribute.labels | Key-value pairs of attributes for the asset  
server_labels.aws_terraform | target.asset.attribute.labels | Key-value pairs of attributes for the asset  
server_labels.aws_tier | target.asset.attribute.labels | Key-value pairs of attributes for the asset  
server_labels.aws_zone | target.asset.attribute.labels | Key-value pairs of attributes for the asset  
server_version | additional.fields | Additional key-value pairs of event data  
session_id | network.session_id | Session identifier for network connections  
severity | security_result.severity | Severity level of the security result  
sid | network.session_id | Session identifier for network connections  
src_ip | principal.ip | Source IP address of the connection  
src_port | principal.port | Source port number of the connection  
sr_summary | security_result.summary | Summary of the security result  
systemRoles | principal.resource.attribute.labels | Key-value pairs of attributes for the resource  
type | metadata.product_event_type | Product-specific event type  
type1 | metadata.product_event_type | Product-specific event type  
uid | principal.user.userid, target.user.userid | User ID of the principal or target user  
user | principal.user.attribute.labels, target.user.user_display_name | Display name of the user  
user_kind | additional.fields | Additional key-value pairs of event data  
working_directory | metadata.ingestion_labels | Key-value pairs of labels for ingestion metadata  
| additional.fields | Additional key-value pairs of event data  
| metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
| metadata.ingestion_labels | Key-value pairs of labels for ingestion metadata  
| metadata.product_name | Name of the product generating the event  
| metadata.vendor_name | Name of the vendor of the product  
| network.session_id | Session identifier for network connections  
| principal.asset.attribute.labels | Key-value pairs of attributes for the asset  
| principal.resource.attribute.labels | Key-value pairs of attributes for the resource  
| principal.user.attribute.labels | Key-value pairs of attributes for the user  
| security_result | Security-related result or action  
| target.asset.attribute.labels | Key-value pairs of attributes for the asset  
| target.process.parent_process.pid | Parent process ID  
| target.user.attribute.roles | Roles associated with the user  
`code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ei` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`orig_log_filename` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`app_name` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`app_public_addr` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`app_uri` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`method` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`status_code` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`path` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`bot_name` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`cluster_name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`server_hostname` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`server_hostname` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`server_id` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`event` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`login` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`namespace` | `event.idm.read_only_udm.principal.namespace` | Mapped from changelog  
`sid` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`server_labels.Role` | `event.idm.read_only_udm.target.user.attribute.roles` | Mapped from changelog  
`server_labels.aws_application` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`user` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`impersonator` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`server_id` | `event.idm.read_only_udm.metadata.ingestion_labels` | Mapped from changelog  
`server_labels.Environment` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`server_labels.OS` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`server_labels.Version` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`server_labels.aws_backup` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`server_labels.aws_cost_center` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`server_labels.aws_environment` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`server_labels.aws_role` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`server_labels.aws_terraform` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`server_labels.aws_tier` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`server_labels.aws_zone` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`server_labels.aws_name` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`private_key_policy` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`server_labels.Uptime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_kind` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`server_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`remote_addr` | `target.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/teleport-access-plane-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
