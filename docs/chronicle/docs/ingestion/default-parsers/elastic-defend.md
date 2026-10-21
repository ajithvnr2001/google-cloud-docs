---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-defend/
title: Collect Elastic Defend logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:27:41.967359+00:00
---

# Collect Elastic Defend logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-defend/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Elastic Defend logs

**Parser Version:** 5.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Elastic Defend logs into Google Security Operations using Google Cloud Storage V2 with a Cloud Run function.

Elastic Defend is an endpoint detection and response (EDR) solution within Elastic Security that provides prevention, detection, and response capabilities with deep visibility across Windows, macOS, and Linux operating systems. It monitors process execution, file activity, network connections, registry modifications, and library loads to detect and prevent threats at the endpoint level. Data is stored in Elasticsearch and can be retrieved using the Elasticsearch Search API.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with the following APIs enabled: 
    * Cloud Storage
    * Cloud Run functions
    * Cloud Scheduler
    * Pub/Sub
    * IAM
  * Access to an Elasticsearch cluster with Elastic Defend deployed
  * Permissions to create API keys in Elasticsearch (`manage_security`, `manage_api_key`, or `manage_own_api_key` cluster privilege)
  * Network connectivity from Cloud Run functions to your Elasticsearch cluster



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `elastic-defend-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Elastic Defend credentials

To enable the Cloud Run function to retrieve Elastic Defend events, you need to create an API key with read permissions on the `logs-endpoint` data streams.

### Create API key using Kibana

  1. Sign in to **Kibana**.
  2. In the navigation menu or global search field, go to **Stack Management > API Keys**.
  3. Click **Create API key**.
  4. In the **Name** field, enter `Google SecOps Cloud Storage Integration`.
  5. In the **Expiration** field, optionally set an expiration date. By default, API keys do not expire.
  6. Click **Control security privileges**.
  7. In the **Indices** section, click **Add index privilege**.
  8. Configure the index privilege: 
     * **Indices** : Enter `logs-endpoint.*`
     * **Privileges** : Select **read**
  9. Leave the **Cluster privileges** section empty (no cluster privileges are required).
  10. Click **Create API key**.



### Record API credentials

After creating the API key, a dialog displays your credentials:

  * **Encoded** : The base64-encoded API key (for example, `VnVhQ2ZHY0JDZGJrUW0tZTVhT3g6dWkybHAyYXhUTm1zeWFrdzl0dk5udw==`)

**Important:** Copy and save the encoded API key immediately. It cannot be retrieved after closing this dialog.

You also need to record your Elasticsearch endpoint URL:

  * For **Elastic Cloud** : The endpoint is displayed in the Cloud Console under your deployment's **Elasticsearch** section (for example, `https://my-deployment.es.us-central1.gcp.cloud.es.io:443`)

  * For **self-managed Elasticsearch** : Use your Elasticsearch cluster's hostname or IP address with port (for example, `https://elasticsearch.example.com:9200`)

**Note:** Include the full URL with protocol and port number for the Cloud Run function configuration.



### Create API key using Dev Tools (alternative method)

Alternatively, you can create an API key using Kibana Dev Tools:

  1. Sign in to **Kibana**.
  2. Go to **Management > Dev Tools**.
  3. In the Console, run the following command:
         
         POST /_security/api_key
         {
           "name": "Google SecOps Cloud Storage Integration",
           "role_descriptors": {
             "chronicle_reader": {
               "indices": [
                 {
                   "names": ["logs-endpoint.*"],
                   "privileges": ["read"]
                 }
               ]
             }
           },
           "metadata": {
             "application": "google-chronicle-gcs",
             "environment": "production"
           }
         }
         

  4. The response contains your API key credentials:
         
         {
           "id": "VuaCfGcBCdbkQm-e5aOx",
           "name": "Google SecOps Cloud Storage Integration",
           "api_key": "ui2lp2axTNmsyakw9tvNnw",
           "encoded": "VnVhQ2ZHY0JDZGJrUW0tZTVhT3g6dWkybHAyYXhUTm1zeWFrdzl0dk5udw=="
         }
         

  5. Copy and save the **encoded** value. This is the base64-encoded API key you will use for authentication.




## Create service account

Create a dedicated service account for the Cloud Run function.

  1. In the **Google Cloud console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `elastic-defend-collector`
     * **Service account description** : Enter `Service account for Elastic Defend log collection to GCS`
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section, add the following roles: 
     1. Click **Select a role** and select **Storage Object Admin** (`roles/storage.objectAdmin`).
     2. Click **Add another role** and select **Cloud Run Invoker** (`roles/run.invoker`).
  6. Click **Continue**.
  7. Click **Done**.



## Create Pub/Sub topic

Create a Pub/Sub topic to trigger the Cloud Run function from Cloud Scheduler.

  1. In the **Google Cloud console** , go to **Pub/Sub > Topics**.
  2. Click **Create Topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `elastic-defend-trigger`
     * **Add a default subscription** : Leave checked
  4. Click **Create**.



## Create Cloud Run function

Create a Cloud Run function that retrieves events from Elasticsearch and writes them to GCS.

### Create the function

  1. In the **Google Cloud console** , go to **Cloud Run functions**.
  2. Click **Create function**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Environment** | 2nd gen  
**Function name** | `elastic-defend-to-gcs`  
**Region** | Select the same region as your GCS bucket  
**Trigger type** | Cloud Pub/Sub  
**Cloud Pub/Sub topic** | Select `elastic-defend-trigger`  
**Memory allocated** | 512 MiB (increase for large data volumes)  
**Timeout** | 540 seconds  
**Runtime service account** | Select `elastic-defend-collector`  
  4. Click **Next**.




### Add environment variables

  * Add the following environment variables in the **Runtime, build, connections and security settings** section:

Variable | Value  
---|---  
`GCS_BUCKET` | Name of your GCS bucket (for example, `elastic-defend-logs`)  
`GCS_PREFIX` | Prefix for log files (for example, `elastic-defend`)  
`STATE_KEY` | Name of the state file (for example, `state.json`)  
`ES_HOST` | Elasticsearch URL (for example, `https://my-deployment.es.us-central1.gcp.cloud.es.io:443`)  
`ES_API_KEY` | Encoded API key from the credential creation step  
`MAX_RECORDS` | Maximum number of records per execution (for example, `100000`)  
`PAGE_SIZE` | Number of records per search request (for example, `1000`)  
`LOOKBACK_HOURS` | Hours to look back on first run (for example, `24`)  
**Note:** Store the `ES_API_KEY` value in Secret Manager for production deployments. Reference it using the **Secrets** tab in the function configuration.



### Add the function code

  1. Select **Python 3.11** as the **Runtime**.
  2. Set the **Entry point** to `main`.
  3. In the **Source code** section, select **Inline Editor**.
  4. Replace the contents of `main.py` with the following code:
         
         import os
         import json
         import datetime
         import base64
         import requests
         from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
         
         GCS_BUCKET = os.environ["GCS_BUCKET"]
         GCS_PREFIX = os.environ.get("GCS_PREFIX", "elastic-defend")
         STATE_KEY = os.environ.get("STATE_KEY", "state.json")
         ES_HOST = os.environ["ES_HOST"]
         ES_API_KEY = os.environ["ES_API_KEY"]
         MAX_RECORDS = int(os.environ.get("MAX_RECORDS", "100000"))
         PAGE_SIZE = int(os.environ.get("PAGE_SIZE", "1000"))
         LOOKBACK_HOURS = int(os.environ.get("LOOKBACK_HOURS", "24"))
         
         INDEX_PATTERN = "logs-endpoint.*"
         SEARCH_PATH = f"/{INDEX_PATTERN}/_search"
         
         def _gcs_client():
             return [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
         
         def _load_state(bucket):
             blob = bucket.blob(f"{GCS_PREFIX}/{STATE_KEY}")
             if blob.exists():
                 return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
             return {}
         
         def _save_state(bucket, state):
             blob = bucket.blob(f"{GCS_PREFIX}/{STATE_KEY}")
             blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 json.dumps(state),
                 content_type="application/json",
             )
         
         def _build_query(gte_ts, sort_after=None):
             body = {
                 "size": PAGE_SIZE,
                 "query": {
                     "range": {
                         "@timestamp": {
                             "gte": gte_ts,
                             "format": "strict_date_optional_time",
                         }
                     }
                 },
                 "sort": [
                     {"@timestamp": {"order": "asc"}},
                     {"_shard_doc": "asc"},
                 ],
             }
             if sort_after:
                 body["search_after"] = sort_after
             return body
         
         def _search(session, body):
             url = f"{ES_HOST.rstrip('/')}{SEARCH_PATH}"
             resp = session.post(
                 url,
                 json=body,
                 headers={
                     "Authorization": f"ApiKey {ES_API_KEY}",
                     "Content-Type": "application/json",
                 },
                 timeout=120,
             )
             resp.raise_for_status()
             return resp.json()
         
         def _write_ndjson(bucket, records, ts_label):
             if not records:
                 return
             now = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
             blob_name = f"{GCS_PREFIX}/{ts_label}/{now}.ndjson"
             blob = bucket.blob(blob_name)
             ndjson = "\n".join(json.dumps(r, separators=(",", ":")) for r in records)
             blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type="application/x-ndjson")
             print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{blob_name}")
         
         def main(event, context):
             """Cloud Run function entry point triggered by Pub/Sub."""
             client = _gcs_client()
             bucket = client.bucket(GCS_BUCKET)
         
             state = _load_state(bucket)
             sort_after = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("sort_after")
         
             if [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_timestamp"):
                 gte_ts = state["last_timestamp"]
             else:
                 gte_ts = (
                     datetime.datetime.utcnow()
                     - datetime.timedelta(hours=LOOKBACK_HOURS)
                 ).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
         
             session = requests.Session()
             total = 0
             batch = []
             last_ts = gte_ts
             ts_label = datetime.datetime.utcnow().strftime("%Y/%m/%d/%H")
         
             while total < MAX_RECORDS:
                 body = _build_query(gte_ts, sort_after)
                 result = _search(session, body)
                 hits = result.get("hits", {}).get("hits", [])
         
                 if not hits:
                     break
         
                 for hit in hits:
                     doc = hit.get("_source", {})
                     doc["_id"] = hit.get("_id")
                     doc["_index"] = hit.get("_index")
                     batch.append(doc)
         
                     hit_ts = doc.get("@timestamp", last_ts)
                     if hit_ts > last_ts:
                         last_ts = hit_ts
         
                 sort_after = hits[-1].get("sort")
                 total += len(hits)
         
                 if len(batch) >= PAGE_SIZE:
                     _write_ndjson(bucket, batch, ts_label)
                     batch = []
         
                 if len(hits) < PAGE_SIZE:
                     break
         
             if batch:
                 _write_ndjson(bucket, batch, ts_label)
         
             new_state = {
                 "last_timestamp": last_ts,
                 "sort_after": sort_after,
             }
             _save_state(bucket, new_state)
             print(f"Done. Fetched {total} records. State: {json.dumps(new_state)}")
             return f"OK: {total} records"
         

  5. Replace the contents of `requirements.txt` with the following:
         
         functions-framework==3.*
         google-cloud-storage==2.*
         requests==2.*
         

  6. Click **Deploy**.

  7. Wait for the deployment to complete successfully.

**Note:** The function uses `search_after` pagination with `@timestamp` sort order to efficiently paginate through large result sets without the 10,000 document limit of `from`/`size` pagination.



## Create Cloud Scheduler job

Create a Cloud Scheduler job to trigger the Cloud Run function on a regular schedule.

  1. In the **Google Cloud console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `elastic-defend-scheduler`  
**Region** | Select the same region as your Cloud Run function  
**Frequency** | `*/5 * * * *` (every 5 minutes)  
**Timezone** | Select your timezone (for example, `UTC`)  
  4. Click **Continue**.

  5. In the **Configure the execution** section:

     * **Target type** : Select **Pub/Sub**
     * **Cloud Pub/Sub topic** : Select `elastic-defend-trigger`
     * **Message body** : Enter `{"run": true}`
  6. Click **Create**.

**Note:** Adjust the frequency based on your data volume and latency requirements. For high-volume environments, every 5 minutes is recommended. For lower-volume environments, every 10-15 minutes may be sufficient.



## Retrieve the Google SecOps service account and configure feed

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Elastic Defend Events`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Elastic Defend** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



### Configure the feed

  1. Click **Next**.
  2. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://elastic-defend-logs/elastic-defend/
           

Replace `elastic-defend-logs` with your GCS bucket name.

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the Google SecOps service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  3. Click **Next**.

  4. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `elastic-defend-logs`).
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
_source.agent.id, _source.agent.type, _source.agent.version, _source.host.architecture, _source.event.agent_id_status, _source.event.id, _source.user.id, _source.group.id, _source.data_stream.type, _source.agent.build.original | additional.fields | Merged with label objects containing values from the listed fields  
_source.process.Ext.session_info.logon_type | extensions.auth.auth_details | Value copied directly  
_source.host.os.full | hardware.cpu_platform | Value copied directly  
_source.host.id | hardware.serial_number | Value copied directly  
_source.rule.description | metadata.description | Value copied directly  
_source.@timestamp | metadata.event_timestamp | Converted using date filter with ISO8601, yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ, yyyy-MM-ddTHH:mm:ss.SSSSSSZ, yyyy-MM-ddTHH:mm:ss.SSSZ, yyyy-MM-ddTHH:mm:ssZ formats  
| metadata.event_type | Set based on _index, event.action, and has_ * conditions  
| metadata.log_type | Set to "ELASTIC_DEFEND"  
| metadata.product_event_type | Set to "File Events" if _index ~ events.file; "Library Events" if events.library; "Network Events" if events.network; "Process Events" if events.process; "Registry Events" if events.registry; "Security Events" if events.security; "API Events" if events.api; "Alerts" if .alert  
_id | metadata.product_log_id | Value from _id if not in ["", " ", "null", "N/A"]  
_source.ecs.version | metadata.product_version | Value copied directly  
_source.network.type | network.application_protocol_version | Value copied directly  
_source.network.transport | network.ip_protocol | Set to "TCP" if matches (?i)tcp; "UDP" if (?i)udp; "ICMP" if (?i)icmp; else "UNKNOWN_IP_PROTOCOL"  
_source.destination.as.organization.name | network.organization_name | Value copied directly  
_source.Endpoint.policy.applied.artifacts.global.identifiers | observer.file.names | Merged from _source.Endpoint.policy.applied.artifacts.global.identifiers  
_source.Endpoint.policy.applied.artifacts.global.version, _source.Endpoint.policy.applied.artifacts.global.snapshot | observer.resource.attribute.labels | Merged with label objects containing values from the listed fields  
_source.Endpoint.policy.applied.artifacts.user.version | observer.user.attribute.labels | Merged with label object containing value from _source.Endpoint.policy.applied.artifacts.user.version  
_source.host.os.full | principal.asset.hardware.cpu_platform | Value copied directly  
_source.host.id | principal.asset.hardware.serial_number | Value copied directly  
_source.host.name | principal.asset.hostname | Value copied directly  
_source.host.ip | principal.asset.ip | Merged from _source.host.ip  
_source.host.os.type | principal.asset.platform_software.platform | Set to "WINDOWS" if matches (?i)windows; "LINUX" if (?i)linux; "MAC" if (?i)mac; "IOS" if (?i)ios; else "UNKNOWN_PLATFORM"  
_source.host.os.kernel | principal.asset.platform_software.platform_patch_level | Value copied directly  
_source.event.created | principal.domain.creation_time | Converted using date filter with ISO8601, yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ, yyyy-MM-ddTHH:mm:ss.SSSSSSZ, yyyy-MM-ddTHH:mm:ss.SSSZ, yyyy-MM-ddTHH:mm:ssZ formats  
_source.user.domain | principal.domain.name | Value copied directly  
_source.process.thread.capabilities.effective | principal.file.capabilities_tags | Merged from _source.process.thread.capabilities.effective  
_source.process.executable | principal.file.full_path | Value copied directly  
_source.process.hash.md5 | principal.file.md5 | Value copied directly  
_source.file.name | principal.file.names | Merged from _source.file.name  
_source.process.hash.sha1 | principal.file.sha1 | Value copied directly  
_source.process.hash.sha256 | principal.file.sha256 | Value copied directly  
_source.host.hostname | principal.hostname | Value copied directly  
_source.host.ip | principal.ip | Merged from _source.host.ip  
_source.host.mac | principal.mac | Merged from _source.host.mac after replacing - with :  
_source.host.os.Ext.variant | principal.platform_version | Value copied directly  
_source.source.port | principal.port | Converted to string then to integer  
_source.process.command_line, _source.process.name | principal.process.command_line | Value from _source.process.command_line if not empty, else from _source.process.name  
_source.process.thread.capabilities.permitted | principal.process.file.capabilities_tags | Merged from _source.process.thread.capabilities.permitted  
_source.process.executable | principal.process.file.full_path | Value copied directly  
_source.process.hash.md5 | principal.process.file.md5 | Value copied directly  
_source.process.hash.sha1 | principal.process.file.sha1 | Value copied directly  
_source.process.hash.sha256 | principal.process.file.sha256 | Value copied directly  
_source.process.parent.executable | principal.process.parent_process.file.full_path | Value copied directly  
_source.process.pid | principal.process.pid | Converted to string then copied  
_source.process.Ext.api.name | principal.resource.attribute.labels | Merged with label object containing value from _source.process.Ext.api.name  
_source.event.code | principal.resource.product_object_id | Value copied directly  
_source.group.name | principal.user.group_identifiers | Merged from _source.group.name  
_source.user.name | principal.user.userid | Value copied directly  
_source.user.id | principal.user.windows_sid | Value from _source.user.id if matches regex ^S-\\\d-(\\\\\\\d+-){1,14}\\\\\\\d+$  
_source.file.Ext.malware_signature.primary.signature.hash.sha256 | security_result.about.file.sha256 | Value copied directly  
_source.event.outcome | security_result.action | Value from _source.event.outcome, uppercased, then set to ALLOW if in [SUCCESS, ALLOW], BLOCK if in [FAILURE, DENY, SKIPPED, RATE_LIMIT], UNKNOWN_ACTION if UNKNOWN  
_source.event.action | security_result.action_details | Value copied directly  
_source.destination.geo.region_iso_code | security_result.associations | Merged with object containing name from _source.destination.geo.region_iso_code  
_source.kibana.alert.rule.parameters.threat.tactic.id, _source.kibana.alert.rule.parameters.threat.tactic.name | security_result.attack_details.tactics | Merged with object containing id and name from the listed fields  
_source.kibana.alert.rule.parameters.threat.technique.id, _source.kibana.alert.rule.parameters.threat.technique.name, _source.kibana.alert.rule.parameters.threat.technique.subtechnique.id, _source.kibana.alert.rule.parameters.threat.technique.subtechnique.name | security_result.attack_details.techniques | Merged with objects containing id, name, subtechnique_id, subtechnique_name from the listed fields  
_source.event.category | security_result.category_details | Merged from _source.event.category  
_source.kibana.alert.rule.description | security_result.description | Value copied directly  
_source.event.kind, _source.file.Ext.malware_signature.all_names, _source.file.Ext.malware_signature.identifier, _source.event.risk_score, _source.threat.tactic.reference, _source.threat.technique.reference, _source.threat.technique.subtechnique.reference | security_result.detection_fields | Merged with label objects containing values from the listed fields  
_source.rule.id, _source.kibana.alert.rule.rule_id | security_result.rule_id | Value from _source.rule.id if not empty, else from _source.kibana.alert.rule.rule_id  
_source.rule.name, _source.kibana.alert.rule.name | security_result.rule_name | Value from _source.rule.name if not empty, else from _source.kibana.alert.rule.name  
_source.rule.ruleset | security_result.rule_set | Value copied directly  
| security_result.severity | Set to "LOW"; if _index matches .alert, set to "HIGH"; if _source.kibana.alert.rule.parameters.severity matches (?i)LOW, set to "LOW"  
_source.message | security_result.summary | Value copied directly  
_source.file.Ext.malware_signature.primary.signature.id | security_result.threat_id | Value copied directly  
_source.file.Ext.malware_signature.primary.signature.name | security_result.threat_name | Value copied directly  
_source.source.address, _source.source.ip | src.asset.ip | Merged from _source.source.address and _source.source.ip  
_source.source.address, _source.source.ip | src.ip | Merged from _source.source.address and _source.source.ip  
_source.host.name | target.asset.hostname | Value copied directly  
_source.destination.address, _source.destination.ip | target.asset.ip | Merged from _source.destination.address and _source.destination.ip  
_source.file.path, _source.dll.path, _source.process.executable, _source.Target.process.executable | target.file.full_path | Value from _source.file.path if events.file, _source.dll.path if events.library, _source.process.executable if events.process or events.api, _source.Target.process.executable if events.api  
_source.dll.hash.md5, _source.process.hash.md5 | target.file.md5 | Value from _source.dll.hash.md5 if events.library, _source.process.hash.md5 if .alert  
_source.dll.name, _source.process.name | target.file.names | Merged from _source.dll.name if events.library, _source.process.name if .alert  
_source.dll.hash.sha1, _source.process.hash.sha1 | target.file.sha1 | Value from _source.dll.hash.sha1 if events.library, _source.process.hash.sha1 if .alert  
_source.dll.hash.sha256, _source.process.hash.sha256 | target.file.sha256 | Value from _source.dll.hash.sha256 if events.library, _source.process.hash.sha256 if .alert  
_source.host.name | target.hostname | Value copied directly  
_source.destination.address, _source.destination.ip | target.ip | Merged from _source.destination.address and _source.destination.ip  
_source.destination.geo.city_name | target.location.city | Value copied directly  
_source.destination.geo.country_name | target.location.country_or_region | Value copied directly  
_source.destination.geo.continent_name | target.location.name | Value copied directly  
_source.destination.geo.location.lat | target.location.region_coordinates.latitude | Converted to string then to float  
_source.destination.geo.location.lon | target.location.region_coordinates.longitude | Converted to string then to float  
_source.destination.geo.region_name | target.location.state | Value copied directly  
_source.data_stream.namespace | target.namespace | Value copied directly  
_source.destination.port | target.port | Converted to string then to integer  
_source.process.command_line | target.process.command_line | Value copied directly  
_source.process.executable | target.process.file.full_path | Value copied directly  
_source.process.hash.md5 | target.process.file.md5 | Value copied directly  
_source.process.hash.sha1 | target.process.file.sha1 | Value copied directly  
_source.process.hash.sha256 | target.process.file.sha256 | Value copied directly  
_source.process.name | target.process.file.names | Merged from _source.process.name  
_source.registry.key | target.registry.registry_key | Value copied directly  
_source.registry.path | target.registry.registry_value_data | Value copied directly  
_source.registry.value | target.registry.registry_value_name | Value copied directly  
_source.data_stream.dataset | target.resource.name | Value copied directly  
_source.process.entity_id | target.user.userid | Value copied directly  
| metadata.product_name | Set to "Elastic Defend"  
| metadata.vendor_name | Set to "Elastic"  
`_source.host.hostname` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`_source.process.pid` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`_source.process.command_line` | `event.idm.read_only_udm.principal.process.command_line` | Mapped from changelog  
`_source.process.name` | `event.idm.read_only_udm.principal.process.file.names` | Mapped from changelog  
`_source.process.parent.executable` | `event.idm.read_only_udm.principal.process.parent_process.file.full_path` | Mapped from changelog  
`_source.process.Ext.token.integrity_level_name` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`_source.process.Ext.code_signature` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`_source.process.Ext.ancestry` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`_source.process.Ext.protection` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`_source.process.Ext.authentication_id` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`_source.winlog.event_data.PrivilegeList` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Privilege List` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`_source.event.ingested` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Ingested` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`_source.event.provider` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Provider` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`_source.user.name` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`_source.event.action` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`_source.host.domain` | `event.idm.read_only_udm.principal.administrative_domain` | Mapped from changelog  
`_source.event.sequence` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`_source.kibana.alert.rule.description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`_source.kibana.alert.rule.rule_id` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`_source.kibana.alert.rule.name` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`_source.kibana.alert.rule.parameters.severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`_source.kibana.alert.rule.parameters.threat.tactic.id` | `event.idm.read_only_udm.security_result.attack_details.tactics` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-defend-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
