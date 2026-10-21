---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dataminr-alert/
title: Collect Dataminr Alerts logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:32:11.870842+00:00
---

# Collect Dataminr Alerts logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dataminr-alert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Dataminr Alerts logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Dataminr Alerts logs into Google Security Operations using Google Cloud Storage V2, a Cloud Run function, and Cloud Scheduler.

Dataminr Pulse delivers AI-powered real-time intelligence from over 500,000 global public data sources, including the deep and dark web. The platform provides early warnings on emerging cyber threats, vulnerabilities, ransomware attacks, data breaches, and digital risks affecting your organization and third parties. The Dataminr Pulse API uses OAuth 2.0 Client Credentials authentication and cursor-based pagination to retrieve alerts.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with the following APIs enabled: 
    * Cloud Storage API
    * Cloud Run functions API
    * Cloud Scheduler API
    * Cloud Pub/Sub API
  * Permissions to create and manage GCS buckets, Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
  * Permissions to manage IAM policies on GCS buckets
  * An active Dataminr Pulse account with API access enabled
  * Dataminr Pulse API credentials (Client ID and Client Secret)
  * At least one Dataminr Pulse Alert List configured in your Dataminr account



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `dataminr-alert-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Dataminr credentials

To enable the Cloud Run function to retrieve alert data, you need API credentials with OAuth 2.0 client credentials authentication from your Dataminr account representative.

### Obtain API credentials

  1. Contact your Dataminr account representative or support team to request API access.
  2. Provide the following information: 
     * Your organization name
     * Use case: Integration with Google Chronicle SIEM
     * Required access: Dataminr Pulse API for Cyber Risk
  3. Dataminr provisions API credentials and provides you with:

     * **Client ID** : Your unique OAuth 2.0 client identifier
     * **Client Secret** : Your OAuth 2.0 client secret key
**Important:** Store the Client Secret securely. If lost, you must request new credentials from Dataminr.



### Verify API credentials

  * To verify that your credentials are working, run the following command:
        
        curl -X POST https://gateway.dataminr.com/auth/2/token \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=api_key"
        

A successful response returns a JSON object containing an `access_token` field:
        
        {
          "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI...",
          "token_type": "Bearer",
          "expire": 3600
        }
        




### Collect alert list IDs

  1. Sign in to the **Dataminr Pulse** web application at `https://app.dataminr.com`.
  2. Navigate to your configured Alert Lists (watchlists).
  3. Note the IDs of the Alert Lists that you want to ingest into Google SecOps.

**Note:** You can specify multiple alert list IDs as a comma-separated string when configuring the Cloud Run function environment variables.



## Create a service account for the Cloud Run function

  1. In the **Google Cloud Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `dataminr-alert-collector`
     * **Service account description** : Enter `Service account for Dataminr Alerts Cloud Run function to write alert data to GCS`
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section, add the following roles: 
     1. Click **Select a role** and search for and select **Storage Object Admin**.
     2. Click **Add Another Role** and search for and select **Cloud Run Invoker**.
  6. Click **Continue**.
  7. Click **Done**.



### Grant IAM permissions on GCS bucket

  1. Go to **Cloud Storage > Buckets**.
  2. Click your Bucket name (for example, `dataminr-alert-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `dataminr-alert-collector@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create a Pub/Sub topic

The Pub/Sub topic triggers the Cloud Run function when a message is published by Cloud Scheduler.

  1. In the **Google Cloud Console** , go to **Pub/Sub > Topics**.
  2. Click **Create Topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `dataminr-alert-trigger`
     * **Add a default subscription** : Leave checked
  4. Click **Create**.



## Create the Cloud Run function

  1. In the **Google Cloud Console** , go to **Cloud Run functions**.
  2. Click **Create function**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Environment** | 2nd gen  
**Function name** | `dataminr-alert-collector`  
**Region** | Select the same region as your GCS bucket  
**Trigger type** | Cloud Pub/Sub  
**Pub/Sub topic** | `dataminr-alert-trigger`  
**Memory allocated** | 512 MiB  
**Timeout** | 540 seconds  
**Runtime service account** | `dataminr-alert-collector`  
  4. Click **Next**.

  5. Set **Runtime** to **Python 3.12**.

  6. Set **Entry point** to `main`.

  7. In the `requirements.txt` file, add the following dependencies:
         
         functions-framework==3.*
         google-cloud-storage==2.*
         requests==2.*
         

  8. In the `main.py` file, paste the following code:
         
         import functions_framework
         import json
         import os
         import logging
         import time
         from datetime import datetime, timedelta, timezone
         from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
         import requests
         
         logger = logging.getLogger(__name__)
         logger.setLevel(logging.INFO)
         
         storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
         
         TOKEN_URL = "https://gateway.dataminr.com/auth/2/token"
         ALERTS_URL = "https://gateway.dataminr.com/api/3/alerts"
         
         def _get_access_token(client_id: str, client_secret: str) -> str:
             """Obtain an OAuth 2.0 access token from Dataminr."""
             payload = {
                 "client_id": client_id,
                 "client_secret": client_secret,
                 "grant_type": "api_key",
             }
             headers = {"Content-Type": "application/x-www-form-urlencoded"}
             resp = requests.post(TOKEN_URL, data=payload, headers=headers, timeout=30)
             resp.raise_for_status()
             token_data = resp.json()
             access_token = token_data.get("access_token")
             if not access_token:
                 raise ValueError("No access_token in token response")
             logger.info("Successfully obtained Dataminr access token.")
             return access_token
         
         def _load_state(bucket_name: str, state_key: str) -> dict:
             """Load the last cursor (alertId) from GCS."""
             try:
                 bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
                 blob = bucket.blob(state_key)
                 if blob.exists():
                     data = json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
                     logger.info(f"Loaded state: {data}")
                     return data
             except Exception as e:
                 logger.warning(f"State read error: {e}")
             logger.info("No previous state found.")
             return {}
         
         def _save_state(bucket_name: str, state_key: str, state: dict) -> None:
             """Save the cursor state to GCS."""
             bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
             blob = bucket.blob(state_key)
             blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 json.dumps(state), content_type="application/json"
             )
             logger.info(f"Saved state: {[state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state)}")
         
         def _fetch_alerts(
             access_token: str,
             alert_lists: str,
             page_size: int,
             cursor: str = None,
         ) -> tuple:
             """Fetch a page of alerts from the Dataminr Pulse API."""
             headers = {
                 "Authorization": f"Bearer {access_token}",
                 "Accept": "application/json",
             }
             params = {
                 "lists": alert_lists,
                 "num": page_size,
             }
             if cursor:
                 params["from"] = cursor
         
             resp = requests.get(
                 ALERTS_URL, headers=headers, params=params, timeout=60
             )
         
             # Handle rate limiting via response headers
             rate_remaining = resp.headers.get("x-ratelimit-remaining")
             rate_reset = resp.headers.get("x-ratelimit-reset")
         
             if resp.status_code == 429:
                 reset_time = int(rate_reset) if rate_reset else 60
                 wait_seconds = max(reset_time - int(time.time()), 1)
                 logger.warning(
                     f"Rate limited. Waiting {wait_seconds}s before retry."
                 )
                 time.sleep(wait_seconds)
                 resp = requests.get(
                     ALERTS_URL, headers=headers, params=params, timeout=60
                 )
         
             resp.raise_for_status()
         
             if rate_remaining is not None:
                 logger.info(
                     f"Rate limit remaining: {rate_remaining}, reset: {rate_reset}"
                 )
         
             data = resp.json()
             alerts = data if isinstance(data, list) else data.get("data", [])
             return alerts
         
         @functions_framework.cloud_event
         def main(cloud_event):
             """Cloud Run function entry point triggered by Pub/Sub."""
             bucket_name = os.environ["GCS_BUCKET"]
             prefix = os.environ.get("GCS_PREFIX", "dataminr_alerts")
             state_key = os.environ.get("STATE_KEY", "dataminr_state/cursor.json")
             client_id = os.environ["CLIENT_ID"]
             client_secret = os.environ["CLIENT_SECRET"]
             alert_lists = os.environ["ALERT_LISTS"]
             max_records = int(os.environ.get("MAX_RECORDS", "1000"))
             page_size = min(int(os.environ.get("PAGE_SIZE", "40")), 40)
             lookback_hours = int(os.environ.get("LOOKBACK_HOURS", "24"))
         
             try:
                 access_token = _get_access_token(client_id, client_secret)
                 state = _load_state(bucket_name, state_key)
                 cursor = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_cursor")
                 is_first_run = cursor is None
         
                 all_alerts = []
                 total_fetched = 0
                 pages_fetched = 0
         
                 while total_fetched < max_records:
                     logger.info(
                         f"Fetching page {pages_fetched + 1} (cursor: {cursor})..."
                     )
                     alerts = _fetch_alerts(
                         access_token, alert_lists, page_size, cursor=cursor
                     )
         
                     if not alerts:
                         logger.info("No more alerts returned. Stopping pagination.")
                         break
         
                     # Filter by lookback window on first run (no prior cursor)
                     if is_first_run:
                         cutoff_ms = int(
                             (
                                 datetime.now(timezone.utc)
                                 - timedelta(hours=lookback_hours)
                             ).timestamp()
                             * 1000
                         )
                         alerts = [
                             a for a in alerts if a.get("eventTime", 0) >= cutoff_ms
                         ]
         
                     all_alerts.extend(alerts)
                     total_fetched += len(alerts)
                     pages_fetched += 1
         
                     # Update cursor to the last alertId in this page
                     last_alert = alerts[-1] if alerts else None
                     if last_alert and "alertId" in last_alert:
                         cursor = last_alert["alertId"]
                     else:
                         break
         
                     # Stop if we received fewer alerts than requested
                     if len(alerts) < page_size:
                         logger.info("Received partial page. Stopping pagination.")
                         break
         
                 logger.info(
                     f"Collected {len(all_alerts)} alerts across {pages_fetched} pages."
                 )
         
                 if not all_alerts:
                     logger.info("No new alerts to write.")
                     return "No new alerts", 200
         
                 # Write alerts as NDJSON to GCS
                 now_str = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
                 blob_path = f"{prefix}/{now_str}.ndjson"
                 ndjson_body = "\n".join(
                     json.dumps(alert, separators=(",", ":")) for alert in all_alerts
                 )
         
                 bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
                 blob = bucket.blob(blob_path)
                 blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                     ndjson_body, content_type="application/x-ndjson"
                 )
         
                 _save_state(
                     bucket_name,
                     state_key,
                     {
                         "last_cursor": cursor,
                         "last_run": datetime.now(timezone.utc).isoformat(),
                     },
                 )
         
                 msg = (
                     f"Wrote {len(all_alerts)} alerts to "
                     f"gs://{bucket_name}/{blob_path}"
                 )
                 logger.info(msg)
                 return msg, 200
         
             except Exception as e:
                 logger.error(f"Error collecting Dataminr alerts: {e}")
                 raise
         

  9. Click **Deploy**.

  10. Wait for the function to be deployed. The status changes to a green checkmark when the deployment is completed.




### Configure environment variables

  1. After the function is deployed, go to **Cloud Run Functions > dataminr-alert-collector**.
  2. Click **Edit and deploy new revision**.
  3. Click the **Variables and Secrets** tab (or expand **Runtime, build, connections and security settings** for 1st gen).
  4. Add the following environment variables:

Key | Example value  
---|---  
`GCS_BUCKET` | `dataminr-alert-logs`  
`GCS_PREFIX` | `dataminr_alerts`  
`STATE_KEY` | `dataminr_state/cursor.json`  
`CLIENT_ID` | Your Dataminr OAuth 2.0 Client ID  
`CLIENT_SECRET` | Your Dataminr OAuth 2.0 Client Secret  
`ALERT_LISTS` | Comma-separated Dataminr alert list IDs  
`MAX_RECORDS` | `1000`  
`PAGE_SIZE` | `40`  
`LOOKBACK_HOURS` | `24`  
**Note:** For production deployments, store `CLIENT_ID` and `CLIENT_SECRET` in Google Cloud Secret Manager and reference them using the **Reference a Secret** option instead of plain-text environment variables.**Note:** The `PAGE_SIZE` value cannot exceed 40, which is the maximum page size supported by the Dataminr Pulse API. The `ALERT_LISTS` value should contain the alert list IDs you want to monitor, separated by commas.
  5. Click **Deploy**.




## Create a Cloud Scheduler job

Cloud Scheduler publishes a message to the Pub/Sub topic on a schedule, triggering the Cloud Run function to poll the Dataminr Pulse for new alerts.

  1. In the **Google Cloud Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `dataminr-alert-poll`  
**Region** | Select the same region as your function  
**Frequency** | `*/5 * * * *` (every 5 minutes)  
**Timezone** | Select your timezone (for example, `UTC`)  
  4. Click **Continue**.

  5. In the **Configure the execution** section:

     * **Target type** : Select **Pub/Sub**
     * **Topic** : Select `dataminr-alert-trigger`
     * **Message body** : Enter `{"poll": true}`
  6. Click **Create**.

**Note:** Dataminr Pulse provides real-time alerts. A polling frequency of 5 minutes ensures timely ingestion while respecting API rate limits. You can adjust the cron expression to poll more or less frequently based on your requirements.



### Verify the Cloud Run function

  1. In **Cloud Scheduler** , locate the `dataminr-alert-poll` job.
  2. Click **Force Run** to trigger an immediate execution.
  3. Go to **Cloud Run Functions > dataminr-alert-collector > Logs**.
  4. Verify the function executed successfully by checking for log entries such as:
         
         Successfully obtained Dataminr access token.
         Fetching page 1 (cursor: None)...
         Collected 35 alerts across 1 pages.
         Wrote 35 alerts to gs://dataminr-alert-logs/dataminr_alerts/20250115T103000Z.ndjson
         

  5. Go to **Cloud Storage > Buckets > dataminr-alert-logs**.

  6. Navigate to the `dataminr_alerts/` prefix.

  7. Verify that NDJSON files are being created with Dataminr alert data.




## Retrieve the Google SecOps service account and configure the feed

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the Feed (for example, `Dataminr Alerts`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Dataminr Alerts** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next section.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://dataminr-alert-logs/dataminr_alerts/
           

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you have selected a deletion option, the service account must have **Storage Object Admin** role, instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed (for example, `DATAMINR_ALERT`).

  12. Click **Next**.

  13. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs the **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your Bucket name (for example, `dataminr-alert-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role, instead of Storage Object Viewer.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
alertId | metadata.product_log_id | Value copied directly  
alertType.color | about.labels.alertType_color | Value copied directly  
alertType.id | about.labels.alertType_id | Value copied directly  
alertType.name | about.labels.alertType_name | Value copied directly  
availableRelatedAlerts | about.labels.availableRelatedAlerts | Converted to string  
caption | metadata.description | Value copied directly  
cat.name | security_result.category_details | Value copied directly  
cat.id | security_result.detection_fields.categories_id | Value copied directly  
cat.idStr | security_result.detection_fields.categories_idStr | Value copied directly  
cat.path | security_result.detection_fields.categories_path | Value copied directly  
cat.requested | security_result.detection_fields.categories_requested | Value copied directly  
cat.retired | security_result.detection_fields.categories_retired | Converted to string  
cat.topicType | about.labels.categories_topicType | Value copied directly  
cat.name | security_result.category | Set to POLICY_VIOLATION if cat.name == "Cybersecurity - Policy"; NETWORK_MALICIOUS if in ["Cybersecurity - Threats & Vulnerabilities", "Cybersecurity - Crime & Malicious Activity", "Threats & Precautions", "Threats"]; NETWORK_SUSPICIOUS if =~ "Cybersecurity"; MAIL_PHISHING if =~ "Email and Web Servers"; DATA_EXFILTRATION if =~ "Data Exposure and Breaches"; POLICY_VIOLATION if =~ "Government, Policy, & Political Affairs"; PHISHING if =~ "(Malware  
comp.dm_bucket.name | security_result.about.resource.attribute.labels.dm _bucket_ %{bucket.id} | Value copied directly  
comp.dm_sector.name | security_result.about.resource.attribute.labels.dm _sector_ %{sector.id} | Value copied directly  
comp.id | security_result.about.resource.attribute.labels.companies_id | Value copied directly  
comp.idStr | security_result.about.resource.attribute.labels.companies_idStr | Value copied directly  
comp.locations.city | security_result.about.location.city | Value from loc.city if loc_index == 0  
comp.locations.country, comp.locations.state.symbol | security_result.about.location.country_or_region | Concatenated as %{loc.country} - %{loc.state.symbol} if loc_index == 0 and both not empty  
comp.locations.postalCode | security_result.about.resource.attribute.labels.locations_postalCode | Value copied directly if loc_index == 0 and not empty  
comp.locations.state.name | security_result.about.location.state | Value copied directly if loc_index == 0  
comp.locations.city | about.labels.loc_%{loc_index}_city | Value copied directly if loc_index != 0 and not empty  
comp.locations.country, comp.locations.state.symbol | about.labels.loc_%{loc_index}_country_or_region | Concatenated as %{loc.country} - %{loc.state.symbol} if loc_index != 0 and both not empty  
comp.locations.postalCode | security _result.about.resource.attribute.labels.locations_ %{loc_index}_postalCode | Value copied directly if loc_index != 0 and not empty  
comp.locations.state.name | about.labels.loc_%{loc_index}_state_name | Value copied directly if loc_index != 0 and not empty  
comp.name | security_result.about.resource.name | Value copied directly  
comp.requested | security_result.about.resource.attribute.labels.companies_requested | Value copied directly  
comp.retired | security_result.about.resource.attribute.labels.companies_retired | Converted to string  
comp.ticker | security_result.about.resource.attribute.labels.companies_ticker | Value copied directly  
comp.topicType | security_result.about.resource.attribute.labels.companies_topicType | Value copied directly  
eventLocation.coordinates.0 | principal.location.region_coordinates.latitude | Value copied directly  
eventLocation.coordinates.1 | principal.location.region_coordinates.longitude | Value copied directly  
eventLocation.name | principal.location.name | Value copied directly  
eventLocation.places | principal.labels.location_places | Joined from array with comma separator  
eventLocation.probability | principal.labels.eventLocation_probability | Converted to string  
eventLocation.radius | principal.labels.eventLocation_radius | Converted to string  
eventMapLargeURL | principal.labels.eventMapLargeURL | Value copied directly  
eventMapSmallURL | principal.labels.eventMapSmallURL | Value copied directly  
eventTime | @timestamp | Converted from epoch ms to timestamp  
eventVolume | about.labels.eventVolume | Converted to string  
expandAlertURL | metadata.url_back_to_product | Value copied directly  
expandMapURL | principal.labels.expandMapURL | Value copied directly  
headerColor | about.labels.headerColor | Value copied directly  
headerLabel | about.labels.headerLabel | Value copied directly  
metadata.cyber.addresses.ip | principal.ip | Extracted using grok pattern if index == 0  
metadata.cyber.addresses.port | principal.port | Value copied directly if index == 0, converted to integer  
metadata.cyber.addresses.port | principal.labels.addresses_%{index}_port | Value copied directly if index != 0  
metadata.cyber.addresses.version | principal.labels.metadata_cyber _addresses_ %{index}_version | Value copied directly  
metadata.cyber.asns | network.asn | Value copied directly if index == 0  
metadata.cyber.asns | about.labels.metadata _cyber_ %{index}_asn | Value copied directly if index != 0  
metadata.cyber.hashValues.value | security_result.about.file.sha1 | Value copied directly if type == SHA1, lowercased  
metadata.cyber.hashValues.value | security_result.about.file.sha256 | Value copied directly if type == SHA256, lowercased  
metadata.cyber.malwares | security_result.associations.name | Value copied directly  
metadata.cyber.malwares | security_result.associations.type | Set to MALWARE  
metadata.cyber.orgs | network.organization_name | Value copied directly if index == 0  
metadata.cyber.orgs | about.labels.metadata _cyber_ %{index}_orgs | Value copied directly if index != 0  
metadata.cyber.products | principal.application | Value copied directly if index == 0  
metadata.cyber.products | principal.labels.metadata_cyber _products_ %{index} | Value copied directly if index != 0  
metadata.cyber.threats | security_result.threat_name | Value copied directly if index == 0  
metadata.cyber.threats | security_result.about.labels.metadata_cyber _threats_ %{index} | Value copied directly if index != 0  
metadata.cyber.URLs | security_result.about.url | Value copied directly if index == 0  
metadata.cyber.URLs | security _result.about.labels.url_ %{index} | Value copied directly if index != 0  
metadata.cyber.malwares.0 | security_result.category | Set to SOFTWARE_MALICIOUS if exists  
metadata.cyber.vulnerabilities.cvss | extensions.vulns.vulnerabilities.cvss_base_score | Value copied directly  
metadata.cyber.vulnerabilities.exploitPocLinks | extensions.vulns.vulnerabilities.cve_description | Joined from array with " n" separator  
metadata.cyber.vulnerabilities.id | extensions.vulns.vulnerabilities.cve_id | Value copied directly  
metadata.cyber.vulnerabilities.products.productName | extensions.vulns.vulnerabilities.about.application | Value copied directly if index == 0  
metadata.cyber.vulnerabilities.products.productVendor | extensions.vulns.vulnerabilities.vendor | Value copied directly if index == 0  
metadata.cyber.vulnerabilities.products.productVersion | extensions.vulns.vulnerabilities.about.platform_version | Value copied directly if index == 0, spaces removed  
metadata.cyber.vulnerabilities.products.productName | extensions.vulns.vulnerabilities.about.labels.productName_%{index} | Value copied directly if index != 0  
metadata.cyber.vulnerabilities.products.productVendor | extensions.vulns.vulnerabilities.about.labels.productVendor_%{index} | Value copied directly if index != 0  
metadata.cyber.vulnerabilities.products.productVersion | extensions.vulns.vulnerabilities.about.labels.productVersion_%{index} | Value copied directly if index != 0, spaces removed  
parentAlertId | about.labels.parentAlertId | Value copied directly  
post.languages.lang | target.labels.post_languages _lang_ %{index} | Value copied directly  
post.languages.position | target.labels.post_languages _position_ %{index} | Converted to string  
post.link | target.labels.post_link | Value copied directly  
post.media.link | principal.resource.name | Value copied directly if index == 0  
post.media.description | target.resource.attribute.labels.post_media_description | Value copied directly if index == 0  
post.media.display_url | target.resource.attribute.labels.post_media_display_url | Value copied directly if index == 0  
post.media.isSafe | target.resource.attribute.labels.post_media_isSafe | Converted to string if index == 0  
post.media.media_url | target.resource.attribute.labels.post_media_media_url | Value copied directly if index == 0  
post.media.sizes.large.h | target.resource.attribute.labels.post_media_sizes_large_h | Converted to string if index == 0  
post.media.sizes.large.resize | target.resource.attribute.labels.post_media_sizes_large_resize | Value copied directly if index == 0  
post.media.sizes.large.w | target.resource.attribute.labels.post_media_sizes_large_w | Converted to string if index == 0  
post.media.sizes.medium.h | target.resource.attribute.labels.post_media_sizes_medium_h | Converted to string if index == 0  
post.media.sizes.medium.resize | target.resource.attribute.labels.post_media_sizes_medium_resize | Value copied directly if index == 0  
post.media.sizes.medium.w | target.resource.attribute.labels.post_media_sizes_medium_w | Converted to string if index == 0  
post.media.sizes.small.h | target.resource.attribute.labels.post_media_sizes_small_h | Converted to string if index == 0  
post.media.sizes.small.resize | target.resource.attribute.labels.post_media_sizes_small_resize | Value copied directly if index == 0  
post.media.sizes.small.w | target.resource.attribute.labels.post_media_sizes_small_w | Converted to string if index == 0  
post.media.sizes.thumb.h | target.resource.attribute.labels.post_media_sizes_thumb_h | Converted to string if index == 0  
post.media.sizes.thumb.resize | target.resource.attribute.labels.post_media_sizes_thumb_resize | Value copied directly if index == 0  
post.media.sizes.thumb.w | target.resource.attribute.labels.post_media_sizes_thumb_w | Converted to string if index == 0  
post.media.source | target.resource.attribute.labels.post_media_source | Value copied directly if index == 0  
post.media.thumbnail | target.resource.attribute.labels.post_media_thumbnail | Value copied directly if index == 0  
post.media.title | target.resource.attribute.labels.post_media_title | Value copied directly if index == 0  
post.media.url | target.resource.attribute.labels.post_media_url | Value copied directly if index == 0  
post.media.video_info.duration_millis | target.resource.attribute.labels.post_media_video_info_duration_millis | Converted to string if index == 0  
post.media.video_info.aspect_ratio | target.resource.attribute.labels.post_media_video_info_aspect_ratio | Concatenated as %{med.video_info.aspect_ratio.0}, %{med.video_info.aspect_ratio.1} if index == 0  
post.media.video_info.variants.bitrate | target.resource.attribute.labels.post_media_video_info_variants _bitrate_ %{var_index} | Converted to string  
post.media.video_info.variants.content_type | target.resource.attribute.labels.post_media_video_info_variants_content _type_ %{var_index} | Value copied directly  
post.media.video_info.variants.url | target.resource.attribute.labels.post_media_video_info_variants _url_ %{var_index} | Value copied directly  
post.media.type | principal.resource.resource_subtype | Value copied directly if index == 0  
post.media.link | about.resource.name | Value copied directly if index != 0  
post.media.description | about.resource.attribute.labels.post_media_description | Value copied directly if index != 0  
post.media.display_url | about.resource.attribute.labels.post_media_display_url | Value copied directly if index != 0  
post.media.isSafe | about.resource.attribute.labels.post_media_isSafe | Converted to string if index != 0  
post.media.media_url | about.resource.attribute.labels.post_media_media_url | Value copied directly if index != 0  
post.media.sizes.large.h | about.resource.attribute.labels.post_media_sizes_large_h | Converted to string if index != 0  
post.media.sizes.large.resize | about.resource.attribute.labels.post_media_sizes_large_resize | Value copied directly if index != 0  
post.media.sizes.large.w | about.resource.attribute.labels.post_media_sizes_large_w | Converted to string if index != 0  
post.media.sizes.medium.h | about.resource.attribute.labels.post_media_sizes_medium_h | Converted to string if index != 0  
post.media.sizes.medium.resize | about.resource.attribute.labels.post_media_sizes_medium_resize | Value copied directly if index != 0  
post.media.sizes.medium.w | about.resource.attribute.labels.post_media_sizes_medium_w | Converted to string if index != 0  
post.media.sizes.small.h | about.resource.attribute.labels.post_media_sizes_small_h | Converted to string if index != 0  
post.media.sizes.small.resize | about.resource.attribute.labels.post_media_sizes_small_resize | Value copied directly if index != 0  
post.media.sizes.small.w | about.resource.attribute.labels.post_media_sizes_small_w | Converted to string if index != 0  
post.media.sizes.thumb.h | about.resource.attribute.labels.post_media_sizes_thumb_h | Converted to string if index != 0  
post.media.sizes.thumb.resize | about.resource.attribute.labels.post_media_sizes_thumb_resize | Value copied directly if index != 0  
post.media.sizes.thumb.w | about.resource.attribute.labels.post_media_sizes_thumb_w | Converted to string if index != 0  
post.media.source | about.resource.attribute.labels.post_media_source | Value copied directly if index != 0  
post.media.thumbnail | about.resource.attribute.labels.post_media_thumbnail | Value copied directly if index != 0  
post.media.title | about.resource.attribute.labels.post_media_title | Value copied directly if index != 0  
post.media.url | about.resource.attribute.labels.post_media_url | Value copied directly if index != 0  
post.media.video_info.duration_millis | about.resource.attribute.labels.post_media_video_info_duration_millis | Converted to string if index != 0  
post.media.video_info.aspect_ratio | about.resource.attribute.labels.post_media_video_info_aspect_ratio | Concatenated as %{med.video_info.aspect_ratio.0}, %{med.video_info.aspect_ratio.1} if index != 0  
post.media.video_info.variants.bitrate | about.resource.attribute.labels.post_media_video_info_variants _bitrate_ %{var_index} | Converted to string  
post.media.video_info.variants.content_type | about.resource.attribute.labels.post_media_video_info_variants_content _type_ %{var_index} | Value copied directly  
post.media.video_info.variants.url | about.resource.attribute.labels.post_media_video_info_variants _url_ %{var_index} | Value copied directly  
post.media.type | about.resource.resource_subtype | Value copied directly if index != 0  
post.translatedText | target.labels.post_translatedText | Value copied directly  
post.text | target.labels.post_text | Value copied directly  
post.timestamp | target.resource.attribute.creation_time | Converted from epoch ms to timestamp  
publisherCategory.color | target.labels.publisherCategory_color | Value copied directly  
publisherCategory.name | target.labels.publisherCategory_name | Value copied directly  
publisherCategory.shortName | target.labels.publisherCategory_shortName | Value copied directly  
relatedTerms.url | principal.labels.relatedTerms_%{terms.text} | Value copied directly  
relatedTermsQueryURL | principal.labels.relatedTermsQueryURL | Value copied directly  
sect.id | about.labels.sectors_id | Value copied directly  
sect.idStr | about.labels.sectors_idStr | Value copied directly  
sect.name | about.labels.sectors_name | Value copied directly  
sect.retired | about.labels.sectors_retired | Converted to string  
sect.topicType | about.labels.sectors_topicType | Value copied directly  
source.channels.0 | principal.application | Value copied directly  
source.displayName | principal.user.user_display_name | Value copied directly  
source.link | principal.url | Value copied directly  
source.verified | principal.labels.source_verified | Converted to string  
subCaption.bullets.content | about.labels.subCaption_bullets_content | Value copied directly  
subCaption.bullets.media | about.labels.subCaption_bullets_media | Value copied directly  
subCaption.bullets.source | about.labels.subCaption_bullets_source | Value copied directly  
watchlist.id | about.labels.watchlistsMatchedByType_id | Value copied directly  
watchlist.externalTopicIds | about.labels.watchlistsMatchedByType_externalTopicIds | Joined from array with comma separator  
watchlist.name | about.labels.watchlistsMatchedByType_name | Value copied directly  
watchlist.type | about.labels.watchlistsMatchedByType_type | Value copied directly  
watchlist.userProperties.omnilist | about.labels.watchlistsMatchedByType_userProperties_omnilist | Value copied directly  
watchlist.userProperties.uiListType | about.labels.watchlistsMatchedByType_userProperties_uiListType | Value copied directly  
watchlist.userProperties.watchlistColor | about.labels.watchlistsMatchedByType_userProperties_watchlistColor | Value copied directly  
watchlist.locationGroups.locations.id | about.labels.watchlistsMatchedByType _locationGroups_ %{lg_i}_locations _id_ %{loc_i} | Value copied directly  
watchlist.locationGroups.locations.lng | about.labels.watchlistsMatchedByType _locationGroups_ %{lg_i}_locations _lng_ %{loc_i} | Converted to string if lg_i != 0 or loc_i != 0  
watchlist.locationGroups.locations.lat | about.labels.watchlistsMatchedByType _locationGroups_ %{lg_i}_locations _lat_ %{loc_i} | Converted to string if lg_i != 0 or loc_i != 0  
watchlist.locationGroups.locations.name | about.labels.watchlistsMatchedByType _locationGroups_ %{lg_i}_locations _name_ %{loc_i} | Value copied directly if lg_i != 0 or loc_i != 0  
watchlist.locationGroups.id | about.labels.watchlistsMatchedByType_locationGroups _id_ %{lg_i} | Value copied directly  
watchlist.locationGroups.name | about.labels.watchlistsMatchedByType_locationGroups _name_ %{lg_i} | Value copied directly  
watchlist.locationGroups.locations.lng | about.location.region_coordinates.longitude | Value copied directly if lg_i == 0 and loc_i == 0  
watchlist.locationGroups.locations.lat | about.location.region_coordinates.latitude | Value copied directly if lg_i == 0 and loc_i == 0  
watchlist.locationGroups.locations.name | about.location.name | Value copied directly if lg_i == 0 and loc_i == 0  
source.entityName | principal.hostname | Value copied directly  
| metadata.event_type | Set to "GENERIC_EVENT"; changed to "SCAN_HOST" if principal_ip or principal.hostname not empty  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dataminr-alert-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
