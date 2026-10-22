---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-cloud-audit/
title: Collect Oracle Cloud Infrastructure logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:00.855638+00:00
---

# Collect Oracle Cloud Infrastructure logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-cloud-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Oracle Cloud Infrastructure logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Oracle Cloud Infrastructure (OCI) Audit logs to Google Security Operations using one of the following methods:

  * **Method 1: Google Cloud Storage** : An OCI Function writes the logs to a Cloud Storage bucket, and a Google SecOps feed reads them from the bucket.
  * **Method 2: Webhook** : An OCI Function sends the logs directly to a Google SecOps webhook feed. This method does not use a Cloud Storage bucket.



Both methods use OCI Connector Hub to deliver Audit logs to the function, because Oracle Cloud Infrastructure cannot send logs directly to Cloud Storage or to an HTTPS endpoint.

Oracle Cloud Infrastructure Audit service automatically records calls to all supported OCI public application programming interface (API) endpoints as log events. Log events recorded by the Audit service include API calls made by the OCI Console, Command Line Interface (CLI), Software Development Kits (SDK), your own custom clients, or other OCI services. The information in the logs includes the time the API activity occurred, the source and target of the activity, the type of action, and the type of response.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the Oracle Cloud Console, with permissions to create and manage: 
    * Connector Hub connectors
    * Functions applications and functions
    * IAM policies
  * A VCN subnet with internet access for the OCI Function
  * OCI Cloud Shell or a local environment with the Fn CLI
  * **For Method 1:** A Google Cloud project with the Cloud Storage API enabled, and permissions to create Cloud Storage buckets, service accounts, and bucket Identity and Access Management (IAM) policies
  * **For Method 2:** Permission to create API keys in the Google Cloud project linked to your Google SecOps instance



## Method 1: Cloud Storage

### Create a Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `oci-audit-logs-gcs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




### Configure Oracle Cloud Infrastructure to export Audit logs to Cloud Storage

Oracle Cloud Infrastructure does not support built-in export to Cloud Storage. You use the OCI Service Connector Hub with an OCI Function to forward Audit logs to Cloud Storage.

#### Create an Oracle Cloud Infrastructure function to forward logs to Cloud Storage

  1. Sign in to the [Oracle Cloud Console](https://cloud.oracle.com/).
  2. Open the navigation menu and select **Developer Services > Functions > Applications**.
  3. Select the compartment where you want to create the function application.
  4. Click **Create Application**.
  5. Provide the following configuration details: 
     * **Name** : Enter `audit-logs-to-gcs-app`.
     * **VCN** : Select a Virtual Cloud Network.
     * **Subnets** : Select a subnet with internet access.
  6. Click **Create**.
  7. After the application is created, click **Getting Started** and follow the instructions to set up your local development environment with the Fn CLI.
  8. Create a new function directory on your local machine:
         
         mkdir oci-audit-to-gcs
         cd oci-audit-to-gcs
         

  9. Initialize a Python function:
         
         fn init --runtime python oci-audit-to-gcs
         cd oci-audit-to-gcs
         

  10. Replace the contents of `func.py` with the following code:
         
         import io
         import json
         import logging
         import os
         from fdk import response
         from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
         from google.oauth2 import service_account
         from datetime import datetime
         
         # Configure logging
         logging.basicConfig(level=logging.INFO)
         logger = logging.getLogger()
         
         # Environment variables
         GCS_BUCKET = os.environ.get('GCS_BUCKET')
         GCS_PREFIX = os.environ.get('GCS_PREFIX', 'oci-audit-logs')
         GCS_CREDENTIALS_JSON = os.environ.get('GCS_CREDENTIALS_JSON')
         
         def handler(ctx, data: io.BytesIO = None):
             """
             OCI Function to forward Audit logs to GCS.
         
             Args:
                 ctx: Function context
                 data: Input data containing Audit log events
             """
         
             if not all([GCS_BUCKET, GCS_CREDENTIALS_JSON]):
                 logger.error('Missing required environment variables: GCS_BUCKET or GCS_CREDENTIALS_JSON')
                 return response.Response(
                     ctx, response_data=json.dumps({"error": "Missing configuration"}),
                     headers={"Content-Type": "application/json"}
                 )
         
             try:
                 # Parse input data
                 body = json.loads(data.getvalue())
                 logger.info(f"Received event: {json.dumps(body)}")
         
                 # Extract log entries
                 log_entries = []
                 if isinstance(body, list):
                     log_entries = body
                 elif isinstance(body, dict):
                     # Service Connector Hub sends data in specific format
                     if 'data' in body:
                         log_entries = [body['data']] if isinstance(body['data'], dict) else body['data']
                     else:
                         log_entries = [body]
         
                 if not log_entries:
                     logger.info("No log entries to process")
                     return response.Response(
                         ctx, response_data=json.dumps({"status": "no_logs"}),
                         headers={"Content-Type": "application/json"}
                     )
         
                 # Initialize GCS client with service account credentials
                 credentials_dict = json.loads(GCS_CREDENTIALS_JSON)
                 credentials = service_account.Credentials.from_service_account_info(credentials_dict)
                 storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)(credentials=credentials, project=credentials_dict.get('project_id'))
                 bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
         
                 # Write logs to GCS as NDJSON
                 timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S_%f')
                 object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
                 blob = bucket.blob(object_key)
         
                 ndjson = '\n'.join([json.dumps(entry, ensure_ascii=False) for entry in log_entries]) + '\n'
                 blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
         
                 logger.info(f"Wrote {len(log_entries)} records to gs://{GCS_BUCKET}/{object_key}")
         
                 return response.Response(
                     ctx, response_data=json.dumps({"status": "success", "records": len(log_entries)}),
                     headers={"Content-Type": "application/json"}
                 )
         
             except Exception as e:
                 logger.error(f'Error processing logs: {str(e)}')
                 return response.Response(
                     ctx, response_data=json.dumps({"error": str(e)}),
                     headers={"Content-Type": "application/json"},
                     status_code=500
                 )
         

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

  11. Update `requirements.txt` with the following dependencies:
         
         fdk>=0.1.0
         google-cloud-storage>=2.0.0
         google-auth>=2.0.0
         

  12. Deploy the function to OCI:
         
         fn -v deploy --app audit-logs-to-gcs-app
         

  13. After deployment completes, note the function OCID. You will use it when configuring the Service Connector Hub.




#### Configure function environment variables

  1. In the Oracle Cloud Console, go to **Developer Services > Functions > Applications**.
  2. Click the application (`audit-logs-to-gcs-app`).
  3. Click the function name (`oci-audit-to-gcs`).
  4. Click **Configuration**.
  5. Add the following configuration variables:

Key | Value  
---|---  
`GCS_BUCKET` | Your Cloud Storage bucket name (for example, `oci-audit-logs-gcs`)  
`GCS_PREFIX` | Prefix for log files (for example, `oci-audit-logs`)  
`GCS_CREDENTIALS_JSON` | JSON string of Google Cloud service account key  
  6. Click **Save changes**.




#### Create a Google Cloud service account for the Oracle Cloud Infrastructure function

The OCI function needs a Google Cloud service account to write to the Cloud Storage bucket.

  1. In the **Google Cloud Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `oci-function-gcs-writer`.
     * **Service account description** : Enter `Service account for OCI Function to write Audit logs to GCS`.
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section, add the following role: 
     1. Click **Select a role**.
     2. Search for and select **Storage Object Admin**.
  6. Click **Continue**.
  7. Click **Done**.
  8. Click the newly created service account email.
  9. Go to the **Keys** tab.
  10. Click **Add Key > Create new key**.
  11. Select **JSON** as the key type.
  12. Click **Create**. The JSON key file will be downloaded to your computer.
  13. Open the JSON key file and copy its entire contents.
  14. Return to the Oracle Cloud Console function configuration.
  15. Paste the JSON contents into the `GCS_CREDENTIALS_JSON` configuration variable.

**Note:** Store the service account key securely. Anyone with access to this key can write to your Cloud Storage bucket.



#### Grant IAM permissions on the Cloud Storage bucket

Grant the service account write permissions on the Cloud Storage bucket as follows:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (`oci-audit-logs-gcs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`oci-function-gcs-writer@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



#### Create an OCI Service Connector Hub connector

  1. Sign in to the [Oracle Cloud Console](https://cloud.oracle.com/).
  2. Open the navigation menu and select **Analytics & AI**. Under **Messaging** , select **Connector Hub**.
  3. Select the compartment where you want to create the service connector.
  4. Click **Create connector**.
  5. Provide the following configuration details:

     * **Connector information:**

Setting | Value  
---|---  
**Connector Name** | Enter `audit-logs-to-gcs-connector`  
**Description** | Enter `Forward OCI Audit logs to Cloud Storage`  
**Resource Compartment** | Select the compartment  
     * **Configure source:**

Setting | Value  
---|---  
**Source** | Select **Logging**  
**Compartment** | Select the compartment containing audit logs  
**Log Group** | Select **_Audit** (default log group for audit logs)  
  6. Click **\+ Another Log**.

  7. Select the audit log for your compartment (for example, `_Audit_Include_Subcompartment`).

**Note:** If you want to capture audit logs from multiple compartments, click **\+ Another Log** to add additional log sources.
     * **Configure target:**

Setting | Value  
---|---  
**Target** | Select **Functions**  
**Function Compartment** | Select the compartment containing the function  
**Function Application** | Select `audit-logs-to-gcs-app`  
**Function** | Select `oci-audit-to-gcs`  
  8. Navigate to **Configure task (optional)** and leave the default settings.

  9. If prompted to create a policy (required for access to create or update a service connector), select **Create**.

  10. Click **Create**.




#### Create an IAM policy for the Service Connector Hub

The Service Connector Hub requires permissions to invoke the function.

  1. In the Oracle Cloud Console, go to **Identity & Security > Policies**.
  2. Select the compartment where you created the Service Connector Hub connector.
  3. Click **Create Policy**.
  4. Provide the following configuration details: 
     * **Name** : Enter `service-connector-functions-policy`.
     * **Description** : Enter `Allow Service Connector Hub to invoke Functions`.
     * **Compartment** : Select the compartment.
  5. In the **Policy Builder** section, toggle **Show manual editor**.
  6. Enter the following policy statements:
         
         Allow any-user to use fn-function in compartment <compartment-name> where all {request.principal.type='serviceconnector'}
         Allow any-user to use fn-invocation in compartment <compartment-name> where all {request.principal.type='serviceconnector'}
         

**Note:** Replace `<compartment-name>` with your compartment name.
  7. Click **Create**.




#### Test the integration

  1. Sign in to the Oracle Cloud Console.
  2. Perform some actions that generate audit logs (for example, create or modify a resource).
  3. Wait 2-5 minutes for logs to be processed.
  4. Go to **Cloud Storage > Buckets** in the Google Cloud Console.
  5. Click your bucket name (`oci-audit-logs-gcs`).
  6. Navigate to the prefix folder (`oci-audit-logs/`).
  7. Verify that new `.ndjson` files are appearing in the bucket.

**Note:** Each log file will be named with a timestamp in the format `logs_YYYYMMDD_HHMMSS_microseconds.ndjson`.



### Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your Cloud Storage bucket. You must grant this service account access to your bucket.

#### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Oracle Cloud Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Oracle Cloud Infrastructure Audit Logs** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email is displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.



### Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs two roles on your Cloud Storage bucket: A Storage Object Viewer to read the log objects and a bucket-level role to read the bucket metadata

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (`oci-audit-logs-gcs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select both of the following: 
       * **Storage Object Viewer** : reads the log objects.
       * **Storage Legacy Bucket Reader** : reads the bucket metadata. If you selected the **Delete transferred files and empty directories** deletion option, select **Storage Legacy Bucket Writer** instead, which also grants the delete permission.
  6. Click **Save**.

**Note:** Grant both roles. **Storage Object Viewer** does not grant the bucket-level permission the feed needs, and the **Storage Legacy Bucket** roles do not grant permission to read object contents.



### Configure a feed in Google SecOps to ingest Oracle Cloud Infrastructure Audit logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Oracle Cloud Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Oracle Cloud Infrastructure Audit Logs** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
           
           gs://oci-audit-logs-gcs/oci-audit-logs/
           

     * Replace:

       * `oci-audit-logs-gcs`: Your Cloud Storage bucket name.
       * `oci-audit-logs`: Optional prefix or path where logs are stored (leave empty for root).

**Examples:**

       * Root bucket: `gs://company-logs/`
       * With prefix: `gs://company-logs/oci-audit-logs/`
       * With subfolder: `gs://company-logs/oracle/audit/`
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
     * **Maximum File Age (Days)** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Method 2: Webhook

With this method, Connector Hub delivers batches of Audit log entries to an OCI Function, and the function sends them to a Google SecOps webhook feed over HTTPS. No Cloud Storage bucket is involved.

### Create a webhook feed in Google SecOps

#### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `OCI Audit Logs Webhook`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Oracle Cloud Infrastructure Audit Logs** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** : Enter `\n`. The function sends each log entry on its own line.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



#### Generate and save the secret key

  1. On the feed details page, click **Generate Secret Key**.
  2. Copy and save the secret key securely.

**Note:** The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.



#### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**. The URL has the following format:
         
         https://<REGION>-chronicle.googleapis.com/v1alpha/projects/<PROJECT_NUMBER>/locations/<REGION>/instances/<INSTANCE_ID>/feeds/<FEED_ID>:importPushLogs
         

  3. Click **Done**.




### Create a Google Cloud API key

  1. Go to the [Google Cloud console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select the project linked to your Google SecOps instance.
  3. Click **Create credentials > API key**.
  4. Click **Edit API key** to restrict the key.
  5. In the **Name** field, enter a descriptive name (for example, `oci-audit-webhook`).
  6. Under **API restrictions** , select **Restrict key** , and then select **Chronicle API** in the **Select APIs** list.
  7. Click **Save**.
  8. Copy the API key value and save it securely.



### Create an OCI Function to forward logs to the webhook

#### Create the application

  1. Sign in to the [Oracle Cloud Console](https://cloud.oracle.com/).
  2. Open the navigation menu and select **Developer Services > Functions > Applications**.
  3. Select the compartment where you want to create the function application.
  4. Click **Create Application**.
  5. Provide the following configuration details: 
     * **Name** : Enter `audit-logs-to-secops-app`.
     * **VCN** : Select a Virtual Cloud Network.
     * **Subnets** : Select a subnet with internet access: a public subnet with an internet gateway, or a private subnet with a NAT gateway. The function must reach the Google SecOps endpoint over HTTPS (port 443).
  6. Click **Create**.



#### Create and deploy the function

  1. After the application is created, click **Getting Started** and follow the instructions to set up OCI Cloud Shell or your local development environment with the Fn CLI.
  2. Initialize a Python function:
         
         fn init --runtime python oci-audit-to-secops
         cd oci-audit-to-secops
         

  3. Replace the contents of `func.py` with the following code:
         
         import io
         import json
         import logging
         import os
         import random
         import time
         from email.utils import parsedate_to_datetime
         
         import requests
         from fdk import response
         
         logging.basicConfig(level=logging.INFO)
         logger = logging.getLogger()
         
         # The webhook accepts at most 4 MB per request and 1 MB per log line.
         # Connector Hub delivers batches of up to 6 MB, so a batch is sent as several
         # requests, each made of whole log entries.
         MAX_REQUEST_BYTES = 3 * 1024 * 1024
         MAX_LINE_BYTES = 1024 * 1024
         
         MAX_ATTEMPTS = 5
         RETRYABLE_STATUS = {429, 500, 502, 503, 504}
         # OCI stops the function at its configured timeout (300 seconds). Stop retrying
         # early enough to fail cleanly so that Connector Hub retries the whole batch.
         DEADLINE_SECONDS = 240
         
         def to_lines(body):
             """Serialize each log entry from the Connector Hub batch as one JSON line."""
             entries = body if isinstance(body, list) else [body]
             lines = []
             for entry in entries:
                 line = json.dumps(entry, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
                 if len(line) > MAX_LINE_BYTES:
                     entry_id = entry.get('id') if isinstance(entry, dict) else None
                     logger.error(f'Skipping log entry {entry_id}: {len(line)} bytes exceeds the 1 MB line limit')
                     continue
                 lines.append(line)
             return lines
         
         def to_requests(lines):
             """Group whole lines into newline-delimited request bodies below MAX_REQUEST_BYTES."""
             chunk, size = [], 0
             for line in lines:
                 if chunk and size + len(line) + 1 > MAX_REQUEST_BYTES:
                     yield b'\n'.join(chunk), len(chunk)
                     chunk, size = [], 0
                 chunk.append(line)
                 size += len(line) + 1
             if chunk:
                 yield b'\n'.join(chunk), len(chunk)
         
         def retry_after_seconds(value):
             """Parse a Retry-After header given either in seconds or as an HTTP date."""
             if not value:
                 return None
             try:
                 return max(0.0, float(value))
             except ValueError:
                 pass
             try:
                 return max(0.0, parsedate_to_datetime(value).timestamp() - time.time())
             except (TypeError, ValueError, IndexError, OverflowError):
                 return None
         
         def post(session, url, headers, payload, deadline):
             """Send one request, retrying throttling and server errors until the deadline."""
             status, detail = None, ''
             for attempt in range(1, MAX_ATTEMPTS + 1):
                 remaining = deadline - time.monotonic()
                 if remaining < 5:
                     break
                 wait = None
                 try:
                     resp = session.post(url, data=payload, headers=headers, timeout=(10, min(60, remaining)))
                 except requests.RequestException as e:
                     status, detail = None, str(e)
                 else:
                     if 200 <= resp.status_code < 300:
                         return
                     status, detail = resp.status_code, resp.text[:500]
                     if status not in RETRYABLE_STATUS:
                         raise RuntimeError(f'Webhook rejected the request with HTTP {status}: {detail}')
                     wait = retry_after_seconds(resp.headers.get('Retry-After'))
                 if wait is None:
                     wait = min(30, 2 ** attempt) + random.uniform(0, 1)
                 if attempt == MAX_ATTEMPTS or time.monotonic() + wait >= deadline:
                     break
                 logger.warning(f'Attempt {attempt} failed (HTTP {status}): {detail}. Retrying in {wait:.1f} seconds')
                 time.sleep(wait)
             raise RuntimeError(f'Webhook request failed (HTTP {status}): {detail}')
         
         def handler(ctx, data: io.BytesIO = None):
             """Forward a Connector Hub batch of OCI Audit log entries to the webhook feed.
         
             Any exception fails the invocation, and Connector Hub then retries the batch.
             """
             deadline = time.monotonic() + DEADLINE_SECONDS
         
             url = os.environ.get('SECOPS_WEBHOOK_URL')
             api_key = os.environ.get('SECOPS_API_KEY')
             secret_key = os.environ.get('SECOPS_SECRET_KEY')
             if not all([url, api_key, secret_key]):
                 raise RuntimeError('Missing configuration: SECOPS_WEBHOOK_URL, SECOPS_API_KEY and SECOPS_SECRET_KEY are required')
         
             raw = data.getvalue() if data else b''
             if not raw.strip():
                 logger.info('Received an empty batch')
                 return response.Response(
                     ctx, response_data=json.dumps({'records': 0}),
                     headers={'Content-Type': 'application/json'}
                 )
         
             lines = to_lines(json.loads(raw))
             headers = {
                 'Content-Type': 'application/json',
                 'X-goog-api-key': api_key,
                 'X-Webhook-Access-Key': secret_key,
             }
         
             sent = 0
             with requests.Session() as session:
                 for payload, count in to_requests(lines):
                     post(session, url, headers, payload, deadline)
                     sent += count
         
             logger.info(f'Forwarded {sent} log entries')
             return response.Response(
                 ctx, response_data=json.dumps({'records': sent}),
                 headers={'Content-Type': 'application/json'}
             )
         

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

  4. Replace the contents of `requirements.txt` with the following dependencies:
         
         fdk>=0.1.0
         requests>=2.32.0
         

  5. Open `func.yaml` and add the following line to raise the function timeout from the default 30 seconds to the maximum of 300 seconds:
         
         timeout: 300
         

  6. Deploy the function to OCI:
         
         fn -v deploy --app audit-logs-to-secops-app
         




#### Configure function environment variables

  1. In the Oracle Cloud Console, go to **Developer Services > Functions > Applications**.
  2. Click the application (`audit-logs-to-secops-app`).
  3. Click the function name (`oci-audit-to-secops`).
  4. Click **Configuration**.
  5. Add the following configuration variables:

Key | Value  
---|---  
`SECOPS_WEBHOOK_URL` | The feed endpoint URL  
`SECOPS_API_KEY` | The Google Cloud API key  
`SECOPS_SECRET_KEY` | The feed secret key  
  6. Click **Save changes**.

**Note:** The function sends the API key and the secret key in the `X-goog-api-key` and `X-Webhook-Access-Key` headers, so neither appears in the request URL.



#### Enable function logs

  1. On the **Applications** list page, select `audit-logs-to-secops-app`.
  2. Select the **Monitoring** tab and go to the **Logs** section.
  3. From the **Actions** menu (three dots) for the **Function Invocation Logs** category, select **Enable Log**.
  4. Keep the default compartment, log group, and log name, or change them as needed.
  5. Select **Enable Log**.



### Create an OCI Connector Hub connector

  1. Open the navigation menu and select **Analytics & AI**. Under **Messaging** , select **Connector Hub**.
  2. Select the compartment where you want to create the connector.
  3. Click **Create connector**.
  4. Provide the following configuration details:

     * **Connector information:**

Setting | Value  
---|---  
**Connector Name** | Enter `audit-logs-to-secops-connector`  
**Description** | Enter `Forward OCI Audit logs to a webhook feed`  
**Resource Compartment** | Select the compartment  
     * **Configure source:**

Setting | Value  
---|---  
**Source** | Select **Logging**  
**Compartment** | Select the compartment containing audit logs  
**Log Group** | Select **_Audit** (default log group for audit logs)  
  5. Click **\+ Another Log**.

  6. Select the audit log for your compartment (for example, `_Audit_Include_Subcompartment`).

**Note:** If you want to capture audit logs from multiple compartments, click **\+ Another Log** to add additional log sources.
     * **Configure target:**

Setting | Value  
---|---  
**Target** | Select **Functions**  
**Function Compartment** | Select the compartment containing the function  
**Function Application** | Select `audit-logs-to-secops-app`  
**Function** | Select `oci-audit-to-secops`  
  7. Navigate to **Configure task (optional)** and leave the default settings.

  8. If prompted to create a policy (required for access to create or update a service connector), select **Create**.

  9. Click **Create**.




#### Create IAM policy for Connector Hub

Connector Hub requires permissions to invoke the function.

  1. In the Oracle Cloud Console, go to **Identity & Security > Policies**.
  2. Select the compartment where you created the connector.
  3. Click **Create Policy**.
  4. Provide the following configuration details: 
     * **Name** : Enter `connector-hub-secops-function-policy`.
     * **Description** : Enter `Allow Connector Hub to invoke the webhook forwarding function`.
     * **Compartment** : Select the compartment.
  5. In the **Policy Builder** section, toggle **Show manual editor**.
  6. Enter the following policy statements:
         
         Allow any-user to use fn-function in compartment <compartment-name> where all {request.principal.type='serviceconnector'}
         Allow any-user to use fn-invocation in compartment <compartment-name> where all {request.principal.type='serviceconnector'}
         

**Note:** Replace `<compartment-name>` with your compartment name.
  7. Click **Create**.




### How the function delivers logs

  * **Batch size** : Connector Hub sends the function batches of up to 6 MB, and the webhook accepts up to 4 MB per request. The function splits each batch into requests of up to 3 MB. It splits only between log entries, never inside one, and each entry arrives in Google SecOps as one event.
  * **Retries** : The function retries HTTP 429 and 5xx responses with exponential backoff, and honors the `Retry-After` header. Any other error, or a request that still fails after five attempts, fails the invocation. Connector Hub then retries the whole batch and does not move later batches until it succeeds.
  * **Retention** : The Logging source of Connector Hub keeps undelivered data for 24 hours. If delivery keeps failing for longer, the oldest undelivered logs are lost, so fix errors reported in the function log promptly.
  * **Duplicates** : Connector Hub delivers each batch at least once. When a batch is retried after part of it was already sent, Google SecOps can receive those entries twice.
  * **Oversized entries** : A log entry larger than 1 MB exceeds the webhook line limit. The function skips it and writes its ID to the function log.



### Verify the integration

To verify the integration, do the following:

  1. Perform some actions in the Oracle Cloud Console that generate audit logs (for example, create or modify a resource).
  2. Wait 2-5 minutes for Connector Hub to deliver the logs.
  3. Open the function invocation log that you enabled and confirm that it contains `Forwarded N log entries` messages. An error message includes the HTTP status that Google SecOps returned.
  4. In Google SecOps, run a raw log search for the `OCI_AUDIT` log type and confirm that the audit events arrive.

**Note:** Webhook feeds don't update the **Last succeeded on** column on the **Feeds** page, so don't use it to check this method.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`accept_encoding_field` | `additional.fields` | Merged  
`accept_field` | `additional.fields` | Merged  
`additional_app` | `additional.fields` | Merged  
`additional_content_type` | `additional.fields` | Merged  
`additional_sort_by` | `additional.fields` | Merged  
`additionaldetails_data` | `additional.fields` | Merged  
`allow_methods_field` | `additional.fields` | Merged  
`auth_type_label` | `additional.fields` | Merged  
`authorization_field` | `additional.fields` | Merged  
`backend_connect_time_field` | `additional.fields` | Merged  
`backend_processing_time_field` | `additional.fields` | Merged  
`caller_id_label` | `additional.fields` | Merged  
`caller_name_label` | `additional.fields` | Merged  
`cloud_event_versiom_field` | `additional.fields` | Merged  
`compartment_id_field` | `additional.fields` | Merged  
`compartment_name_field` | `additional.fields` | Merged  
`connection_field` | `additional.fields` | Merged  
`content_length_field` | `additional.fields` | Merged  
`content_type_field` | `additional.fields` | Merged  
`event_grouping_id_field` | `additional.fields` | Merged  
`event_name_label` | `additional.fields` | Merged  
`event_resource_label` | `additional.fields` | Merged  
`event_source_label` | `additional.fields` | Merged  
`event_type_label` | `additional.fields` | Merged  
`event_type_versiom_field` | `additional.fields` | Merged  
`has_compariment_id` | `additional.fields` | Mapped: `true` → `additional_app`  
`has_sort_by` | `additional.fields` | Mapped: `true` → `additional_sort_by`  
`listener_name_field` | `additional.fields` | Merged  
`log_group_id_field` | `additional.fields` | Merged  
`log_id_field` | `additional.fields` | Merged  
`message` | `additional.fields` | Mapped values (41 total, e.g. `\/` → `tenant_id_label`, `\/` → `auth_type_label`, `\/` → `ca...  
`opc_request_id_field` | `additional.fields` | Merged  
`origin_field` | `additional.fields` | Merged  
`param0_field` | `additional.fields` | Merged  
`param1_field` | `additional.fields` | Merged  
`referer_field` | `additional.fields` | Merged  
`request_processing_time_field` | `additional.fields` | Merged  
`resource_id_field` | `additional.fields` | Merged  
`routing_rules_engine_errors_field` | `additional.fields` | Merged  
`routing_rules_matched_rule_field` | `additional.fields` | Merged  
`routing_rules_rule_hits_field` | `additional.fields` | Merged  
`routing_rules_rule_misses_field` | `additional.fields` | Merged  
`source_field` | `additional.fields` | Merged  
`tenant_id_label` | `additional.fields` | Merged  
`column3` | `extensions.auth.type` | Mapped: `login successful` → `AUTHTYPE_UNSPECIFIED`  
`message` | `extensions.auth.type` | Mapped: `\/` → `AUTHTYPE_UNSPECIFIED`  
`column3` | `metadata.description` | Directly mapped  
`data.message` | `metadata.description` | Directly mapped  
`column1` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`data_event_time` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSSSSZ`  
`time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`metadata_event_type` | `metadata.event_type` | Directly mapped  
`type` | `metadata.product_event_type` | Directly mapped  
`data_event_id` | `metadata.product_log_id` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`message` | `metadata.product_name` | Mapped: `\/` → `OCI_AUDIT`  
`specversion` | `metadata.product_version` | Directly mapped  
`message` | `metadata.vendor_name` | Mapped: `\/` → `Oracle`  
`message` | `network.application_protocol` | Mapped: `\/` → `HTTPS`, `\/` → `HTTP`  
`protocol` | `network.application_protocol` | Mapped: `(?i)HTTPS` → `HTTPS`, `(?i)HTTP` → `HTTP`  
`version` | `network.application_protocol_version` | Directly mapped  
`data_request_action` | `network.http.method` | Directly mapped  
`method` | `network.http.method` | Directly mapped  
`data_identity_userAgent` | `network.http.parsed_user_agent` | Renamed/mapped  
`data_request_agent` | `network.http.parsed_user_agent` | Renamed/mapped  
`url` | `network.http.referral_url` | Directly mapped  
`data.backendStatusCode` | `network.http.response_code` | Directly mapped  
`data_response_status` | `network.http.response_code` | Renamed/mapped  
`data.userAgent` | `network.http.user_agent` | Directly mapped  
`data_identity_userAgent` | `network.http.user_agent` | Directly mapped  
`data_request_agent` | `network.http.user_agent` | Directly mapped  
`data.receivedBytes` | `network.received_bytes` | Directly mapped  
`message` | `network.received_bytes` | Mapped: `\/` → `uinteger`  
`data.sentBytes` | `network.sent_bytes` | Directly mapped  
`message` | `network.sent_bytes` | Mapped: `\/` → `uinteger`  
`data_identity_consoleSessionId` | `network.session_id` | Renamed/mapped  
`data.sslCipher` | `network.tls.cipher` | Directly mapped  
`data.sslProtocol` | `network.tls.version` | Directly mapped  
`data.host` | `principal.asset.hostname` | Directly mapped  
`hostname` | `principal.asset.hostname` | Directly mapped  
`column6` | `principal.asset.ip` | Merged  
`data.forwardedForAddr` | `principal.asset.ip` | Merged  
`data_identity_ipAddress` | `principal.asset.ip` | Mapped: `^(?:[0-9]{1,3}[.]){3}[0-9]{1,3}$` → `data_identity_ipAddress`  
`data_request_origin` | `principal.asset.ip` | Merged  
`ip1` | `principal.asset.ip` | Merged  
`ip2` | `principal.asset.ip` | Merged  
`message` | `principal.asset.ip` | Mapped values (7 total, e.g. `\/` → `column6`, `\/` → `data_request_origin`, `\/` → `ip2`)  
`src_ip` | `principal.asset.ip` | Merged  
`data.host` | `principal.hostname` | Directly mapped  
`hostname` | `principal.hostname` | Directly mapped  
`column6` | `principal.ip` | Merged  
`data.forwardedForAddr` | `principal.ip` | Merged  
`data_identity_ipAddress` | `principal.ip` | Mapped: `^(?:[0-9]{1,3}[.]){3}[0-9]{1,3}$` → `data_identity_ipAddress`  
`data_request_origin` | `principal.ip` | Merged  
`ip1` | `principal.ip` | Merged  
`ip2` | `principal.ip` | Merged  
`message` | `principal.ip` | Mapped values (7 total, e.g. `\/` → `column6`, `\/` → `data_request_origin`, `\/` → `ip2`)  
`src_ip` | `principal.ip` | Merged  
`data_request_headers_sec-ch-ua-platform_0` | `principal.platform` | Mapped: `(?i)Linux` → `LINUX`, `(?i)windows` → `WINDOWS`, `(?i)mac/ios` → `MAC`  
`message` | `principal.platform` | Mapped: `\/` → `LINUX`, `\/` → `WINDOWS`, `\/` → `MAC`  
`originalConnection.sourcePort` | `principal.port` | Directly mapped  
`src_port` | `principal.port` | Directly mapped  
`data_request_headers_oci-original-url_0` | `principal.url` | Directly mapped  
`credentials_label` | `principal.user.attribute.labels` | Merged  
`message` | `principal.user.attribute.labels` | Mapped: `\/` → `credentials_label`  
`data.identity.principalName` | `principal.user.user_display_name` | Directly mapped  
`data.username` | `principal.user.user_display_name` | Directly mapped  
`data.identity.principalId` | `principal.user.userid` | Directly mapped  
`data.principalId` | `principal.user.userid` | Directly mapped  
`column3` | `security_result` | Mapped: `login successful` → `security_result`  
`message` | `security_result` | Mapped: `\/` → `security_result`  
`allow_action` | `security_result.action` | Merged  
`column3` | `security_result.action` | Mapped: `login successful` → `allow_action`  
`message` | `security_result.action` | Mapped: `\/` → `allow_action`  
`credential_type_field` | `security_result.detection_fields` | Merged  
`message` | `security_result.detection_fields` | Mapped: `\/` → `credential_type_field`  
`data.response.message` | `security_result.summary` | Directly mapped  
`message` | `target.asset.ip` | Mapped: `\/` → `originalConnection.destinationIp`, `\/` → `tar_ip`  
`originalConnection.destinationIp` | `target.asset.ip` | Merged  
`tar_ip` | `target.asset.ip` | Merged  
`message` | `target.ip` | Mapped: `\/` → `originalConnection.destinationIp`, `\/` → `tar_ip`  
`originalConnection.destinationIp` | `target.ip` | Merged  
`tar_ip` | `target.ip` | Merged  
`originalConnection.destinationPort` | `target.port` | Directly mapped  
`tar_port` | `target.port` | Directly mapped  
`message` | `target.resource.attribute.labels` | Mapped: `\/` → `namespace_label`  
`namespace_label` | `target.resource.attribute.labels` | Merged  
`type` | `target.resource.attribute.labels` | Mapped: `listretentionrules` → `namespace_label`  
`data.resourceId` | `target.resource.name` | Directly mapped  
`data.resourceName` | `target.resource.name` | Directly mapped  
`bucketId` | `target.resource.product_object_id` | Directly mapped  
`data.resourceId` | `target.resource.product_object_id` | Directly mapped  
`data_request_id` | `target.resource.product_object_id` | Directly mapped  
`message` | `target.resource.resource_type` | Mapped: `\/` → `STORAGE_BUCKET`  
`type` | `target.resource.resource_type` | Mapped: `listretentionrules` → `STORAGE_BUCKET`  
`data_request_path` | `target.url` | Directly mapped  
`column2` | `target.user.email_addresses` | Merged  
`message` | `target.user.email_addresses` | Mapped: `\/` → `column2`  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.product_name` | Constant: `OCI_AUDIT`  
N/A | `metadata.vendor_name` | Constant: `Oracle`  
N/A | `network.application_protocol` | Constant: `HTTPS`  
N/A | `principal.platform` | Constant: `LINUX`  
N/A | `target.resource.resource_type` | Constant: `STORAGE_BUCKET`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-cloud-audit-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
