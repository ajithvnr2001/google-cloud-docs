---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hcl-bigfix/
title: Collect HCL BigFix logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:05.412876+00:00
---

# Collect HCL BigFix logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hcl-bigfix/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect HCL BigFix logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest HCL BigFix logs into Google Security Operations using Google Cloud Storage V2 through a Cloud Run function.

HCL BigFix is an endpoint management platform that provides unified endpoint management, security, and compliance capabilities. It enables organizations to discover, manage, and remediate endpoints across their infrastructure, including patch management, software distribution, configuration management, and security compliance. The Cloud Run function polls the HCL BigFix REST API using session relevance queries, writes the results as NDJSON to a Cloud Storage bucket, and Google SecOps ingests them through a Cloud Storage V2 feed.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with billing enabled
  * Access to HCL BigFix Console with master operator privileges
  * HCL BigFix Server version 9.5 or later
  * WebReports service running on the BigFix Server
  * Network connectivity from the Cloud Run function to BigFix Server on port 52311 (default REST API port)
  * Google Cloud APIs enabled: Cloud Run functions, Cloud Storage, Cloud Scheduler, Pub/Sub, and Identity and Access Management (IAM)



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `hcl-bigfix-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your Google SecOps instance (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**. 

**Note:** Record the bucket name. You will use it when configuring the Cloud Run function and the Google SecOps feed.



## Collect HCL BigFix API credentials

To enable the Cloud Run function to retrieve endpoint data, you need to create a dedicated BigFix Console operator with REST API access permissions.

### Create a dedicated operator for API access

  1. Sign in to the **BigFix Console**.
  2. Go to **Tools > Create Operator**.
  3. In the **Add User** dialog, provide the following information:

     * **Username** : Enter a descriptive username (for example, `chronicle_api`).
     * **Password** : Enter a strong password.
     * **Confirm Password** : Re-enter the password.
  4. Click **OK**.




### Configure operator permissions

After creating the operator, the **Console Operator** window opens automatically.

  1. Click the **Details** tab.
  2. In the **Overview** section: 
     * Select **Always allow this user to login**.
  3. In the **Permissions** section, set the following permissions: 
     * **Can Submit Queries** : Set to **Yes**.
     * **Custom Content** : Set to **Yes**.
  4. In the **Interface Login Privileges** section: 
     * **Can use REST API** : Set to **Yes**.
  5. Click the **Administered Computers** tab.
  6. Select **All computers** to allow the operator to query all endpoints, or select specific computer groups based on your requirements.
  7. Click **Save Changes**.



### Record API credentials

Save the following information for configuring the Cloud Run function environment variables:

  * **Username** : The operator username you created (for example, `chronicle_api`)
  * **Password** : The operator password
  * **BigFix Server Hostname** : The fully qualified domain name or IP address of your BigFix Server (for example, `bigfix.company.com`)
  * **API Port** : The REST API port (default is `52311`)

**Important:** Store these credentials securely. The password cannot be retrieved after this step.



### Test API connectivity

  * Verify that the API credentials work by running the following test query from a machine with network access to the BigFix Server:
        
        curl -k -u "chronicle_api:YOUR_PASSWORD" \
          -X POST \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "relevance=(name of it, id of it) of bes computers" \
          "https://bigfix-server:52311/api/query"
        

**Note:** Replace `bigfix-server` with your BigFix Server hostname, `chronicle_api` with your operator username, and `YOUR_PASSWORD` with the operator password. The `-k` flag skips TLS certificate verification for testing purposes only.

A successful response returns an XML document containing computer names and IDs. If you receive an authentication error, verify the operator permissions configured in the previous steps.




## Create a service account for the Cloud Run function

  1. In the **Google Cloud Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details:

     * **Service account name** : Enter `bigfix-cloud-run` (or a descriptive name).
     * **Service account description** : Enter `Service account for HCL BigFix Cloud Run function to write logs to Cloud Storage`.
  4. Click **Create and Continue**.

  5. In the **Grant this service account access to project** section, add the following roles:

     * **Storage Object Admin** (to read/write objects in the Cloud Storage bucket).
     * **Cloud Run Invoker** (to allow Cloud Scheduler to invoke the function).
  6. Click **Continue**.

  7. Click **Done**.

**Note:** Record the service account email (for example, `bigfix-cloud-run@PROJECT_ID.iam.gserviceaccount.com`). You will use it when creating the Cloud Scheduler job.



## Create a Pub/Sub topic

Cloud Scheduler triggers the Cloud Run function through a Pub/Sub topic.

  1. In the **Google Cloud Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. In the **Topic ID** field, enter `bigfix-ingestion-trigger`.
  4. Leave the default settings.
  5. Click **Create**.

**Note:** Record the full topic name (for example, `projects/PROJECT_ID/topics/bigfix-ingestion-trigger`).



## Create the Cloud Run function

### Prepare function source files

Create the following two files for the Cloud Run function deployment.

  * **requirements.txt**
        
        functions-framework==3.*
        google-cloud-storage==2.*
        requests>=2.31.0
        

  * **main.py**
        
        import base64
        import json
        import logging
        import os
        import xml.etree.ElementTree as ET
        from datetime import datetime, timezone, timedelta
        
        import requests
        import urllib3
        from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
        
        urllib3.disable_warnings(urllib3.[exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html).InsecureRequestWarning)
        
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        
        GCS_BUCKET = os.environ["GCS_BUCKET"]
        GCS_PREFIX = os.environ.get("GCS_PREFIX", "bigfix_logs")
        STATE_KEY = os.environ.get("STATE_KEY", "bigfix_state.json")
        BIGFIX_SERVER = os.environ["BIGFIX_SERVER"]
        BIGFIX_PORT = os.environ.get("BIGFIX_PORT", "52311")
        BIGFIX_USERNAME = os.environ["BIGFIX_USERNAME"]
        BIGFIX_PASSWORD = os.environ["BIGFIX_PASSWORD"]
        MAX_RECORDS = int(os.environ.get("MAX_RECORDS", "10000"))
        LOOKBACK_HOURS = int(os.environ.get("LOOKBACK_HOURS", "24"))
        
        BIGFIX_BASE_URL = f"https://{BIGFIX_SERVER}:{BIGFIX_PORT}/api"
        
        RELEVANCE_QUERIES = {
            "computers": (
                '(id of it, name of it, operating system of it, '
                'last report time of it as string, ip address of it as string, '
                'root server of it) of bes computers'
            ),
            "actions": (
                '(id of it, name of it, name of issuer of it, '
                'time issued of it as string, state of it) of bes actions'
            ),
            "fixlets": (
                '(id of it, name of it, source severity of it, '
                'source of it, category of it) of bes fixlets '
                'whose (source severity of it is not "")'
            ),
        }
        
        def _get_auth_header():
            """Build Basic Auth header from credentials."""
            credentials = f"{BIGFIX_USERNAME}:{BIGFIX_PASSWORD}"
            encoded = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
            return {"Authorization": f"Basic {encoded}"}
        
        def _query_bigfix(relevance, session=None):
            """Execute a session relevance query against the BigFix REST API."""
            url = f"{BIGFIX_BASE_URL}/query"
            headers = _get_auth_header()
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        
            data = {"relevance": relevance}
            http = session or requests
            resp = http.post(url, headers=headers, data=data, verify=False, timeout=120)
            resp.raise_for_status()
            return resp.text
        
        def _parse_query_xml(xml_text, query_name):
            """Parse BigFix XML response into a list of dicts."""
            root = ET.fromstring(xml_text)
            results = []
        
            for result_elem in root.iter("Result"):
                tuples = result_elem.findall("Tuple")
                if tuples:
                    for tup in tuples:
                        answers = [a.text or "" for a in tup.findall("Answer")]
                        record = _map_answers(query_name, answers)
                        record["_query"] = query_name
                        record["_collection_time"] = (
                            datetime.now(timezone.utc).isoformat()
                        )
                        results.append(record)
                else:
                    answers_elems = result_elem.findall("Answer")
                    if answers_elems:
                        answers = [a.text or "" for a in answers_elems]
                        record = _map_answers(query_name, answers)
                        record["_query"] = query_name
                        record["_collection_time"] = (
                            datetime.now(timezone.utc).isoformat()
                        )
                        results.append(record)
        
            logger.info(
                "Query '%s' returned %d results.", query_name, len(results)
            )
            return results
        
        def _map_answers(query_name, answers):
            """Map positional answers to named fields based on query type."""
            field_maps = {
                "computers": [
                    "client_id", "client_name", "OS",
                    "last_report_time", "ip_address", "root_server",
                ],
                "actions": [
                    "action_id", "action_name", "issuer",
                    "time_issued", "state",
                ],
                "fixlets": [
                    "fixlet_id", "fixlet_name", "source_severity",
                    "source", "category",
                ],
            }
            fields = field_maps.get(query_name, [])
            record = {}
            for i, value in enumerate(answers):
                key = fields[i] if i < len(fields) else f"field_{i}"
                record[key] = value
            return record
        
        def _load_state(gcs_client):
            """Load the last run state from GCS."""
            bucket = gcs_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
            blob = bucket.blob(f"{GCS_PREFIX}/{STATE_KEY}")
            if blob.exists():
                data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                return json.loads(data)
            return {}
        
        def _save_state(gcs_client, state):
            """Persist run state to GCS."""
            bucket = gcs_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
            blob = bucket.blob(f"{GCS_PREFIX}/{STATE_KEY}")
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                json.dumps(state), content_type="application/json"
            )
            logger.info("State saved to gs://%s/%s/%s", GCS_BUCKET, GCS_PREFIX, STATE_KEY)
        
        def _write_ndjson(gcs_client, records, timestamp_str):
            """Write records as NDJSON to GCS."""
            if not records:
                logger.info("No records to write.")
                return
        
            records = records[:MAX_RECORDS]
            ndjson_lines = "\n".join(json.dumps(r) for r in records)
            blob_name = f"{GCS_PREFIX}/{timestamp_str}/bigfix_events.ndjson"
            bucket = gcs_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
            blob = bucket.blob(blob_name)
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson_lines, content_type="application/x-ndjson")
            logger.info(
                "Wrote %d records to gs://%s/%s",
                len(records), GCS_BUCKET, blob_name,
            )
        
        def main(event, context):
            """Cloud Run function entry point triggered by Pub/Sub."""
            logger.info("HCL BigFix ingestion function started.")
        
            gcs_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
            state = _load_state(gcs_client)
        
            last_run = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_run")
            if last_run:
                logger.info("Last successful run: %s", last_run)
        
            now = datetime.now(timezone.utc)
            timestamp_str = now.strftime("%Y/%m/%d/%H%M%S")
        
            all_records = []
            session = requests.Session()
        
            for query_name, relevance in RELEVANCE_QUERIES.items():
                try:
                    xml_text = _query_bigfix(relevance, session=session)
                    records = _parse_query_xml(xml_text, query_name)
                    all_records.extend(records)
                except requests.[exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html).RequestException as e:
                    logger.error(
                        "Failed to execute query '%s': %s", query_name, e
                    )
                except ET.ParseError as e:
                    logger.error(
                        "Failed to parse XML for query '%s': %s", query_name, e
                    )
        
            session.close()
        
            _write_ndjson(gcs_client, all_records, timestamp_str)
        
            state["last_run"] = now.isoformat()
            state["records_written"] = len(all_records)
            _save_state(gcs_client, state)
        
            logger.info(
                "HCL BigFix ingestion complete. %d total records written.",
                len(all_records),
            )
            return "OK"
        




### Deploy the Cloud Run function

  1. Save both files (`main.py` and `requirements.txt`) into a local directory (for example, `bigfix-function/`).
  2. Open **Cloud Shell** or a terminal with the `gcloud` CLI installed.
  3. Run the following command to deploy the function:
         
         gcloud functions deploy bigfix-to-gcs \
           --gen2 \
           --region=us-central1 \
           --runtime=python312 \
           --trigger-topic=bigfix-ingestion-trigger \
           --entry-point=main \
           --memory=512MB \
           --timeout=540s \
           --service-account=bigfix-cloud-run@PROJECT_ID.iam.gserviceaccount.com \
           --set-env-vars="GCS_BUCKET=hcl-bigfix-logs,GCS_PREFIX=bigfix_logs,STATE_KEY=bigfix_state.json,BIGFIX_SERVER=bigfix.company.com,BIGFIX_PORT=52311,BIGFIX_USERNAME=chronicle_api,BIGFIX_PASSWORD=YOUR_PASSWORD,MAX_RECORDS=10000,LOOKBACK_HOURS=24"
         

  4. Replace the following placeholder values:

     * `PROJECT_ID`: Your Google Cloud project ID.
     * `hcl-bigfix-logs`: Your Cloud Storage bucket name.
     * `bigfix.company.com`: Your BigFix Server hostname or IP address.
     * `chronicle_api`: Your BigFix operator username.
     * `YOUR_PASSWORD`: Your BigFix operator password.
**Note:** For production deployments, use Google Cloud Secret Manager to store the `BIGFIX_PASSWORD` instead of passing it as a plaintext environment variable. Reference the secret using `--set-secrets="BIGFIX_PASSWORD=bigfix-password:latest"`.
  5. Verify the deployment by checking the function status:
         
         gcloud functions describe bigfix-to-gcs --region=us-central1 --gen2
         




### Environment variables reference

Variable | Required | Default | Description  
---|---|---|---  
`GCS_BUCKET` | Yes |  | Cloud Storage bucket name for storing NDJSON output  
`GCS_PREFIX` | No | `bigfix_logs` | Object prefix (folder path) within the bucket  
`STATE_KEY` | No | `bigfix_state.json` | Blob name for the state file within the prefix  
`BIGFIX_SERVER` | Yes |  | BigFix Server hostname or IP address  
`BIGFIX_PORT` | No | `52311` | BigFix REST API port  
`BIGFIX_USERNAME` | Yes |  | BigFix operator username  
`BIGFIX_PASSWORD` | Yes |  | BigFix operator password  
`MAX_RECORDS` | No | `10000` | Maximum number of records to write per execution  
`LOOKBACK_HOURS` | No | `24` | Number of hours to look back for initial collection  
  
## Create a Cloud Scheduler job

Cloud Scheduler triggers the Cloud Run function at regular intervals through the Pub/Sub topic.

  1. In the **Google Cloud Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details: 
     * **Name** : Enter `bigfix-ingestion-schedule`.
     * **Region** : Select the same region as your Cloud Run function (for example, `us-central1`).
     * **Frequency** : Enter `0 */4 * * *` (runs every 4 hours). Adjust the schedule based on your data volume and freshness requirements.
     * **Timezone** : Select your preferred timezone.
  4. Click **Continue**.
  5. In the **Configure the execution** section: 
     * **Target type** : Select **Pub/Sub**.
     * **Topic** : Select `bigfix-ingestion-trigger`.
     * **Message body** : Enter `{"run": true}`.
  6. Click **Continue**.
  7. In the **Configure optional settings** section: 
     * **Max retry attempts** : Enter `3`.
     * **Min backoff duration** : Enter `5s`.
     * **Max backoff duration** : Enter `60s`.
  8. Click **Create**.
  9. To run an immediate test, click the three dots (**...**) next to the job name and select **Force run**.

**Note:** Monitor the function execution logs in **Cloud Logging** by filtering on the function name `bigfix-to-gcs`. Verify that NDJSON files appear in your Cloud Storage bucket under the configured prefix.



## Retrieve the Google SecOps service account and configure the feed

Google SecOps uses a unique service account to read data from your Cloud Storage bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `HCL BigFix Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **HCL BigFix** as the **Log type**.
  7. Click **Get Service Account**.

A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI:
           
           gs://hcl-bigfix-logs/bigfix_logs/
           

       * Replace `hcl-bigfix-logs` with your Cloud Storage bucket name.
       * Replace `bigfix_logs` with your configured `GCS_PREFIX` value.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the Google SecOps service account must have **Storage Object Admin** role instead of **Storage Object Viewer**. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your Cloud Storage bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `hcl-bigfix-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email (for example, `chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of **Storage Object Viewer**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
WMI_Asset_ID | entity.asset.asset_id | Set to "Asset Id:" + value if not empty and not "N/A"  
Computer_Serial_Number, Computer_Manufacturer, Computer_Model | entity.asset.hardware | Object with serial_number, manufacturer, model  
client_name | entity.asset.hostname | Value copied directly  
MAC_Addresses | entity.asset.mac | Merged from array after formatting  
OperatingSystemType | entity.asset.platform_software.platform | Uppercased value if not empty and not "Unix"  
OS | entity.asset.platform_software.platform_version | Value copied directly  
SerialNumber | entity.asset.product_object_id | Value if not empty  
WindowsOperatingSystem | entity.asset.software | Object with name set to value if not empty  
OperatingSystemRole | entity.asset.type | Uppercased value if not empty  
DNS_Name | entity.domain.name | Value if not empty  
CloudInfo | entity.labels | Label object with key "CloudInfo" and value (quotes removed) if not empty  
Domain Role | entity.user.attribute.roles | Object with name set to value if not empty  
Active_Directory_Path | entity.user.group_identifiers | Merged value if not empty and not ""  
WMI_Service_Tag | entity.user.product_object_id | Value if not empty  
User_Name | entity.user.user_display_name | Value if not empty and not ""  
client_id | entity.user.userid | Value copied directly  
| metadata.entity_type | Set to "ASSET" if SerialNumber not empty, else "USER"  
| metadata.product_name | Set to "HCL Big Fix"  
| metadata.vendor_name | Set to "HCL Software"  
`CloudInfo` | `event.idm.entity.entity.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hcl-bigfix-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
