---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/censys/
title: Collect Censys ASM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:46.504181+00:00
---

# Collect Censys ASM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/censys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Censys ASM logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Censys logs to Google Security Operations using Google Cloud Storage V2.

Censys provides comprehensive attack surface management and internet intelligence through its API. This integration lets you collect host discovery events, risk events, and asset changes from Censys ASM and forward them to Google SecOps for analysis and monitoring.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Censys ASM



## Collect Censys API credentials

  1. Sign in to the Censys ASM Console at [app.censys.io](https://app.censys.io).
  2. Go to **Integrations** at the top of the page.
  3. Copy and save your **API Key** and **Organization ID**.
  4. Note the **API Base URL** : `https://api.platform.censys.io`



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `censys-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `censys-data-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Censys logs`.
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
  2. Click on your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `censys-data-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `censys-data-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Censys ASM API and writes them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `censys-data-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`censys-data-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     * Select **Require authentication**.
     * Check **Identity and Access Management (IAM)**.

**Note:** Pub/Sub automatically handles authentication when invoking the function.

  1. Scroll down and expand **Containers, Networking, Security**.
  2. Go to the **Security** tab: 
     * **Service account** : Select the service account (`censys-data-collector-sa`).
  3. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:

Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `censys-logs`  
`GCS_PREFIX` | `censys/`  
`STATE_KEY` | `censys/state.json`  
`CENSYS_API_KEY` | `your-censys-api-key`  
`CENSYS_ORG_ID` | `your-organization-id`  
`API_BASE` | `https://api.platform.censys.io`  
  4. Scroll down in the **Variables & Secrets** tab to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  5. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
     * Click **Done**.
  6. Scroll to **Execution environment** :

     * Select **Default** (recommended).
  7. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  8. Click **Create**.

  9. Wait for the service to be created (1-2 minutes).

  10. After the service is created, the **inline code editor** opens automatically.




### Add function code

  1. Enter **main** in **Function entry point**
  2. In the inline code editor, create two files:

     * First file: **main.py:**
    
    import functions_framework
    from google.cloud import storage
    import json
    import urllib3
    import gzip
    import os
    from datetime import datetime, timedelta, timezone
    from typing import Dict, List, Any, Optional
    from urllib.parse import urlencode
    
    # Initialize HTTP client with timeouts
    http = urllib3.PoolManager(
        timeout=urllib3.Timeout(connect=5.0, read=30.0),
        retries=False,
    )
    
    # Initialize Storage client
    storage_client = storage.Client()
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch logs from Censys ASM API and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        # Get environment variables
        bucket_name = os.environ.get('GCS_BUCKET')
        prefix = os.environ.get('GCS_PREFIX', 'censys/')
        state_key = os.environ.get('STATE_KEY', 'censys/state.json')
        censys_api_key = os.environ.get('CENSYS_API_KEY')
        censys_org_id = os.environ.get('CENSYS_ORG_ID')
        api_base = os.environ.get('API_BASE', 'https://api.platform.censys.io')
    
        if not all([bucket_name, censys_api_key, censys_org_id]):
            print('Error: Missing required environment variables')
            return
    
        try:
            collector = CensysCollector(
                bucket_name=bucket_name,
                prefix=prefix,
                state_key=state_key,
                api_key=censys_api_key,
                org_id=censys_org_id,
                api_base=api_base
            )
    
            # Get last collection time
            last_collection_time = collector.get_last_collection_time()
            current_time = datetime.now(timezone.utc)
    
            print(f'Collecting events since {last_collection_time}')
    
            # Collect different types of events
            logbook_events = collector.collect_logbook_events()
            risk_events = collector.collect_risks_events()
    
            # Save events to GCS
            collector.save_events_to_gcs(logbook_events, 'logbook')
            collector.save_events_to_gcs(risk_events, 'risks')
    
            # Update state
            collector.save_collection_time(current_time)
    
            print(f'Successfully processed {len(logbook_events)} logbook events and {len(risk_events)} risk events')
    
        except Exception as e:
            print(f'Error processing logs: {str(e)}')
            raise
    
    class CensysCollector:
        def __init__(self, bucket_name: str, prefix: str, state_key: str, 
                     api_key: str, org_id: str, api_base: str):
            self.bucket_name = bucket_name
            self.prefix = prefix
            self.state_key = state_key
            self.headers = {
                'Authorization': f'Bearer {api_key}',
                'X-Organization-ID': org_id,
                'Content-Type': 'application/json'
            }
            self.api_base = api_base
            self.bucket = storage_client.bucket(bucket_name)
    
        def get_last_collection_time(self) -> Optional[datetime]:
            """Get the last collection timestamp from GCS state file."""
            try:
                blob = self.bucket.blob(self.state_key)
                if blob.exists():
                    state_data = blob.download_as_text()
                    state = json.loads(state_data)
                    return datetime.fromisoformat(state.get('last_collection_time', '2024-01-01T00:00:00Z'))
            except Exception as e:
                print(f'No state file found or error reading state: {e}')
            return datetime.now(timezone.utc) - timedelta(hours=1)
    
        def save_collection_time(self, collection_time: datetime):
            """Save the current collection timestamp to GCS state file."""
            state = {'last_collection_time': collection_time.strftime('%Y-%m-%dT%H:%M:%SZ')}
            blob = self.bucket.blob(self.state_key)
            blob.upload_from_string(
                json.dumps(state),
                content_type='application/json'
            )
    
        def collect_logbook_events(self, cursor: str = None) -> List[Dict[str, Any]]:
            """Collect logbook events from Censys ASM API using cursor-based pagination."""
            events = []
            url = f"{self.api_base}/v3/logbook"
    
            params = {}
            if cursor:
                params['cursor'] = cursor
    
            try:
                query_string = urlencode(params) if params else ''
                full_url = f"{url}?{query_string}" if query_string else url
    
                response = http.request('GET', full_url, headers=self.headers)
    
                # Handle rate limiting with exponential backoff
                if response.status == 429:
                    retry_after = int(response.headers.get('Retry-After', '60'))
                    print(f'Rate limited (429). Retrying after {retry_after}s...')
                    import time
                    time.sleep(retry_after)
                    return self.collect_logbook_events(cursor)
    
                if response.status != 200:
                    print(f'API request failed with status {response.status}: {response.data}')
                    return []
    
                data = json.loads(response.data.decode('utf-8'))
                events.extend(data.get('logbook_entries', []))
    
                # Handle cursor-based pagination
                next_cursor = data.get('next_cursor')
                if next_cursor:
                    events.extend(self.collect_logbook_events(next_cursor))
    
                print(f'Collected {len(events)} logbook events')
                return events
    
            except Exception as e:
                print(f'Error collecting logbook events: {e}')
                return []
    
        def collect_risks_events(self) -> List[Dict[str, Any]]:
            """Collect risk events from Censys ASM API."""
            events = []
            url = f"{self.api_base}/v3/risks"
    
            try:
                response = http.request('GET', url, headers=self.headers)
    
                # Handle rate limiting with exponential backoff
                if response.status == 429:
                    retry_after = int(response.headers.get('Retry-After', '60'))
                    print(f'Rate limited (429). Retrying after {retry_after}s...')
                    import time
                    time.sleep(retry_after)
                    return self.collect_risks_events()
    
                if response.status != 200:
                    print(f'API request failed with status {response.status}: {response.data}')
                    return []
    
                data = json.loads(response.data.decode('utf-8'))
                events.extend(data.get('risks', []))
    
                print(f'Collected {len(events)} risk events')
                return events
    
            except Exception as e:
                print(f'Error collecting risk events: {e}')
                return []
    
        def save_events_to_gcs(self, events: List[Dict[str, Any]], event_type: str):
            """Save events to GCS in compressed NDJSON format."""
            if not events:
                return
    
            timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
            filename = f"{self.prefix}{event_type}_{timestamp}.json.gz"
    
            try:
                # Convert events to newline-delimited JSON
                ndjson_content = '\n'.join(json.dumps(event, separators=(',', ':')) for event in events)
    
                # Compress with gzip
                gz_bytes = gzip.compress(ndjson_content.encode('utf-8'))
    
                blob = self.bucket.blob(filename)
                blob.upload_from_string(
                    gz_bytes,
                    content_type='application/gzip'
                )
    
                print(f'Saved {len(events)} {event_type} events to {filename}')
    
            except Exception as e:
                print(f'Error saving {event_type} events to GCS: {e}')
                raise
    

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).


**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.

## Create Cloud Scheduler job

Cloud Scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `censys-data-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`censys-data-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

  * Choose frequency based on log volume and latency requirements:

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
  5. Click on your function name (`censys-data-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for the following:
         
         Collecting events since YYYY-MM-DDTHH:MM:SS+00:00
         Collected X logbook events
         Collected X risk events
         Saved X logbook events to censys/logbook_YYYYMMDD_HHMMSS.json.gz
         Saved X risks events to censys/risks_YYYYMMDD_HHMMSS.json.gz
         Successfully processed X logbook events and X risk events
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name.

  10. Navigate to the prefix folder (`censys/`).

  11. Verify that new `.json.gz` files were created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify account has required permissions
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Censys logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **CENSYS** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.


**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.

## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.

## Configure a feed in Google SecOps to ingest Censys logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Censys logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **CENSYS** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://censys-logs/censys/
           

       * Replace:

         * `censys-logs`: Your GCS bucket name.
         * `censys/`: Optional prefix/folder path where logs are stored (leave empty for root).
       * **Examples:**

         * Root bucket: `gs://censys-logs/`
         * With prefix: `gs://censys-logs/censys/`
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
assetId | read_only_udm.principal.asset.hostname | If the assetId field is not an IP address, it is mapped to principal.asset.hostname.  
assetId | read_only_udm.principal.asset.ip | If the assetId field is an IP address, it is mapped to principal.asset.ip.  
assetId | read_only_udm.principal.hostname | If the assetId field is not an IP address, it is mapped to principal.hostname.  
assetId | read_only_udm.principal.ip | If the assetId field is an IP address, it is mapped to principal.ip.  
associatedAt | read_only_udm.security_result.detection_fields.value | The associatedAt field is mapped to security_result.detection_fields.value.  
autonomousSystem.asn | read_only_udm.additional.fields.value.string_value | The autonomousSystem.asn field is converted to a string and mapped to additional.fields.value.string_value with key "autonomousSystem_asn".  
autonomousSystem.bgpPrefix | read_only_udm.additional.fields.value.string_value | The autonomousSystem.bgpPrefix field is mapped to additional.fields.value.string_value with key "autonomousSystem_bgpPrefix".  
banner | read_only_udm.principal.resource.attribute.labels.value | The banner field is mapped to principal.resource.attribute.labels.value with key "banner".  
cloud | read_only_udm.metadata.vendor_name | The cloud field is mapped to metadata.vendor_name.  
comments.refUrl | read_only_udm.network.http.referral_url | The comments.refUrl field is mapped to network.http.referral_url.  
data.cve | read_only_udm.additional.fields.value.string_value | The data.cve field is mapped to additional.fields.value.string_value with key "data_cve".  
data.cvss | read_only_udm.additional.fields.value.string_value | The data.cvss field is mapped to additional.fields.value.string_value with key "data_cvss".  
data.ipAddress | read_only_udm.principal.asset.ip | If the data.ipAddress field is not equal to the assetId field, it is mapped to principal.asset.ip.  
data.ipAddress | read_only_udm.principal.ip | If the data.ipAddress field is not equal to the assetId field, it is mapped to principal.ip.  
data.location.city | read_only_udm.principal.location.city | If the location.city field is empty, the data.location.city field is mapped to principal.location.city.  
data.location.countryCode | read_only_udm.principal.location.country_or_region | If the location.country field is empty, the data.location.countryCode field is mapped to principal.location.country_or_region.  
data.location.latitude | read_only_udm.principal.location.region_coordinates.latitude | If the location.coordinates.latitude and location.geoCoordinates.latitude fields are empty, the data.location.latitude field is converted to a float and mapped to principal.location.region_coordinates.latitude.  
data.location.longitude | read_only_udm.principal.location.region_coordinates.longitude | If the location.coordinates.longitude and location.geoCoordinates.longitude fields are empty, the data.location.longitude field is converted to a float and mapped to principal.location.region_coordinates.longitude.  
data.location.province | read_only_udm.principal.location.state | If the location.province field is empty, the data.location.province field is mapped to principal.location.state.  
data.mailServers | read_only_udm.additional.fields.value.list_value.values.string_value | Each element in the data.mailServers array is mapped to a separate additional.fields entry with key "Mail Servers" and value.list_value.values.string_value set to the element value.  
data.names.forwardDns[].name | read_only_udm.network.dns.questions.name | Each element in the data.names.forwardDns array is mapped to a separate network.dns.questions entry with the name field set to the element's name field.  
data.nameServers | read_only_udm.additional.fields.value.list_value.values.string_value | Each element in the data.nameServers array is mapped to a separate additional.fields entry with key "Name nameServers" and value.list_value.values.string_value set to the element value.  
data.protocols[].transportProtocol | read_only_udm.network.ip_protocol | If the data.protocols[].transportProtocol field is one of TCP, EIGRP, ESP, ETHERIP, GRE, ICMP, IGMP, IP6IN4, PIM, UDP, or VRRP, it is mapped to network.ip_protocol.  
data.protocols[].transportProtocol | read_only_udm.principal.resource.attribute.labels.value | The data.protocols[].transportProtocol field is mapped to principal.resource.attribute.labels.value with key "data_protocols {index}".  
http.request.headers[].key, http.request.headers[].value.headers.0 | read_only_udm.network.http.user_agent | If the http.request.headers[].key field is "User-Agent", the corresponding http.request.headers[].value.headers.0 field is mapped to network.http.user_agent.  
http.request.headers[].key, http.request.headers[].value.headers.0 | read_only_udm.network.http.parsed_user_agent | If the http.request.headers[].key field is "User-Agent", the corresponding http.request.headers[].value.headers.0 field is parsed as a user agent string and mapped to network.http.parsed_user_agent.  
http.request.headers[].key, http.request.headers[].value.headers.0 | read_only_udm.principal.resource.attribute.labels.key, read_only_udm.principal.resource.attribute.labels.value | For each element in the http.request.headers array, the key field is mapped to principal.resource.attribute.labels.key and value.headers.0 field is mapped to principal.resource.attribute.labels.value.  
http.request.uri | read_only_udm.principal.asset.hostname | The hostname part of the http.request.uri field is extracted and mapped to principal.asset.hostname.  
http.request.uri | read_only_udm.principal.hostname | The hostname part of the http.request.uri field is extracted and mapped to principal.hostname.  
http.response.body | read_only_udm.principal.resource.attribute.labels.value | The http.response.body field is mapped to principal.resource.attribute.labels.value with key "http_response_body".  
http.response.headers[].key, http.response.headers[].value.headers.0 | read_only_udm.target.hostname | If the http.response.headers[].key field is "Server", the corresponding http.response.headers[].value.headers.0 field is mapped to target.hostname.  
http.response.headers[].key, http.response.headers[].value.headers.0 | read_only_udm.principal.resource.attribute.labels.key, read_only_udm.principal.resource.attribute.labels.value | For each element in the http.response.headers array, the key field is mapped to principal.resource.attribute.labels.key and value.headers.0 field is mapped to principal.resource.attribute.labels.value.  
http.response.statusCode | read_only_udm.network.http.response_code | The http.response.statusCode field is converted to an integer and mapped to network.http.response_code.  
ip | read_only_udm.target.asset.ip | The ip field is mapped to target.asset.ip.  
ip | read_only_udm.target.ip | The ip field is mapped to target.ip.  
isSeed | read_only_udm.additional.fields.value.string_value | The isSeed field is converted to a string and mapped to additional.fields.value.string_value with key "isSeed".  
location.city | read_only_udm.principal.location.city | The location.city field is mapped to principal.location.city.  
location.continent | read_only_udm.additional.fields.value.string_value | The location.continent field is mapped to additional.fields.value.string_value with key "location_continent".  
location.coordinates.latitude | read_only_udm.principal.location.region_coordinates.latitude | The location.coordinates.latitude field is converted to a float and mapped to principal.location.region_coordinates.latitude.  
location.coordinates.longitude | read_only_udm.principal.location.region_coordinates.longitude | The location.coordinates.longitude field is converted to a float and mapped to principal.location.region_coordinates.longitude.  
location.country | read_only_udm.principal.location.country_or_region | The location.country field is mapped to principal.location.country_or_region.  
location.geoCoordinates.latitude | read_only_udm.principal.location.region_coordinates.latitude | If the location.coordinates.latitude field is empty, the location.geoCoordinates.latitude field is converted to a float and mapped to principal.location.region_coordinates.latitude.  
location.geoCoordinates.longitude | read_only_udm.principal.location.region_coordinates.longitude | If the location.coordinates.longitude field is empty, the location.geoCoordinates.longitude field is converted to a float and mapped to principal.location.region_coordinates.longitude.  
location.postalCode | read_only_udm.additional.fields.value.string_value | The location.postalCode field is mapped to additional.fields.value.string_value with key "Postal code".  
location.province | read_only_udm.principal.location.state | The location.province field is mapped to principal.location.state.  
operation | read_only_udm.security_result.action_details | The operation field is mapped to security_result.action_details.  
perspectiveId | read_only_udm.principal.group.product_object_id | The perspectiveId field is mapped to principal.group.product_object_id.  
port | read_only_udm.principal.port | The port field is converted to an integer and mapped to principal.port.  
risks[].severity, risks[].title | read_only_udm.security_result.category_details | The risks[].severity field is concatenated with the risks[].title field and mapped to security_result.category_details.  
serviceName | read_only_udm.network.application_protocol | If the serviceName field is "HTTP" or "HTTPS", it is mapped to network.application_protocol.  
sourceIp | read_only_udm.principal.asset.ip | The sourceIp field is mapped to principal.asset.ip.  
sourceIp | read_only_udm.principal.ip | The sourceIp field is mapped to principal.ip.  
timestamp | read_only_udm.metadata.event_timestamp | The timestamp field is parsed as a timestamp and mapped to metadata.event_timestamp.  
transportFingerprint.id | read_only_udm.metadata.product_log_id | The transportFingerprint.id field is converted to a string and mapped to metadata.product_log_id.  
transportFingerprint.raw | read_only_udm.additional.fields.value.string_value | The transportFingerprint.raw field is mapped to additional.fields.value.string_value with key "transportFingerprint_raw".  
type | read_only_udm.metadata.product_event_type | The type field is mapped to metadata.product_event_type.  
- | read_only_udm.metadata.product_name | The value "CENSYS_ASM" is assigned to metadata.product_name.  
- | read_only_udm.metadata.vendor_name | The value "CENSYS" is assigned to metadata.vendor_name.  
- | read_only_udm.metadata.event_type | The event type is determined based on the presence of specific fields: NETWORK_CONNECTION if has_princ_machine_id and has_target_machine are true and has_network_flow is false, NETWORK_DNS if has_network_flow is true, STATUS_UPDATE if has_princ_machine_id is true, and GENERIC_EVENT otherwise.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/censys-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
