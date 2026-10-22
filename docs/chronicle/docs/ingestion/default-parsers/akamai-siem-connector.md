---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-siem-connector/
title: Collect Akamai SIEM Connector logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:03.226056+00:00
---

# Collect Akamai SIEM Connector logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-siem-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Akamai SIEM Connector logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can ingest Akamai SIEM Connector logs to Google Security Operations. Akamai SIEM Integration provides security events from the Akamai platform in near real time through the SIEM Integration API in JSON format. These events include data from Web Application Firewall (WAF), Bot Manager, and other Akamai security products. Because the Akamai SIEM Integration API is pull-based, a scheduled function periodically fetches events and writes them to object storage, where Google SecOps ingests them. You can configure ingestion using one of two supported methods:

  * **Method 1: Cloud Storage**. A Cloud Run function periodically pulls events from the Akamai SIEM Integration API and writes them to a Cloud Storage bucket, where Google SecOps ingests them.
  * **Method 2: Amazon S3**. An AWS Lambda function periodically pulls events from the Akamai SIEM Integration API and writes them to an Amazon S3 bucket, where Google SecOps ingests them.



## Before you begin

Make sure you have the following prerequisites:

**Common to both methods:**

  * A Google SecOps instance
  * Privileged access to Akamai Control Center with the `Manage SIEM` user role.



**Method 1 additional prerequisites (Cloud Storage):**

  * A Google Cloud project with the Cloud Storage, Cloud Run, Pub/Sub, and Cloud Scheduler APIs enabled.
  * Permissions to create and manage Cloud Storage buckets, service accounts, Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs.



**Method 2 additional prerequisites (Amazon S3):**

  * Privileged access to AWS (S3, IAM, Lambda, EventBridge).



## Enable SIEM Integration in Akamai Control Center

  1. Sign in to **Akamai Control Center**.
  2. Go to **Security Configurations** under the **Cloud Security** section.
  3. Open the security configuration (and the appropriate version) for which you want to collect SIEM data.
  4. Click **Advanced Settings** and expand **Data collection for SIEM Integrations**.
  5. Click **On** to enable SIEM.
  6. Choose the security policies for which you want to export data:

     * **All Security policies** \- send SIEM data for events that violate any or all security policies within the security configuration.
     * **Specific security policies** \- select one or more specific security policies from the drop-down list.
     * Optional: If you use Account Protector and want to include the unencrypted **Username** , select the **Include username** checkbox.
**Note:** When you include username, anyone with access to your SIEM output can potentially see this value and its associated risk score.
     * Optional: If you want to receive JA4 fingerprint information in SIEM events, select the **Include the JA4 Client TLS Fingerprint** checkbox.
     * Optional: If you want to exclude events belonging to a specific protection type and action, click **Add exception**. Select the protection and the associated actions you don't want SIEM to collect.
  7. Click **Save**.

  8. Copy and save the **Security Configuration ID** (**configId**) from the SIEM Integration section. You need this value for Lambda configuration.




## Create Akamai API credentials for SIEM Integration

  1. Sign in to **Akamai Control Center**.
  2. Go to **ACCOUNT ADMIN > Identity & access > Users and API Clients**.
  3. Click **Create API client**.
  4. Click **Advanced** to create an advanced API client.
  5. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `SecOps SIEM Poller`).
     * **API service** : Select **SIEM** and set the access level to **READ-WRITE**.
  6. Click **Create API client**.
  7. Click **Download** to save the credentials as an `.edgerc` file, or click **Copy** to copy the credentials. Save the following values securely: 
     * **Client Token**
     * **Client Secret**
     * **Access Token**
     * **Host** (for example, `akab-xxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxx.luna.akamaiapis.net`)



## Method 1: Google Cloud Storage

Use this method to collect Akamai SIEM Connector logs into a Cloud Storage bucket. A Cloud Run function, triggered by Cloud Scheduler through Pub/Sub, periodically pulls events from the Akamai SIEM Integration API and writes them to the bucket, where Google SecOps ingests them.

### Create a Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. Go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details: 
     * **Name your bucket** : Enter a globally unique name (for example, `akamai-siem-logs`).
     * **Location type** : Choose based on your needs (Region, Dual-region, or Multi-region).
     * **Location** : Select the location (for example, `us-central1`).
     * **Storage class** : Select **Standard**.
     * **Access control** : Select **Uniform**.
  6. Click **Create**.



### Create a service account for the Cloud Run function

  1. Go to **IAM & Admin > Service Accounts**.
  2. Click **Create service account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `akamai-siem-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Akamai SIEM Connector logs`.
  4. Click **Create and continue**.
  5. Grant the following roles: 
     * **Storage Object Admin** : write events to the bucket and manage the state file.
     * **Cloud Run Invoker** : allow Pub/Sub to invoke the function.
  6. Click **Continue > Done**.



### Grant the service account access to the bucket

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`akamai-siem-collector-sa@<PROJECT_ID>.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



### Create a Pub/Sub topic

  1. Go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. In the **Topic ID** field, enter `akamai-siem-trigger`.
  4. Click **Create**.



### Create the Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler. It signs requests with the Akamai EdgeGrid credentials, fetches events from the SIEM Integration API, and writes them to the bucket.

  1. Go to **Cloud Run**.
  2. Click **Write a function**.
  3. Provide the following configuration details: 
     * **Service name** : Enter `akamai-siem-collector`.
     * **Region** : Select the region matching your bucket (for example, `us-central1`).
     * **Runtime** : Select **Python 3.12** or later.
  4. In the **Trigger** section, click **Add trigger** and select **Pub/Sub trigger**.
  5. In the **Eventarc trigger** pane, provide the following configuration details: 
     * **Trigger name** : Keep the generated name or enter a name for the trigger.
     * **Trigger type** : Select **Google Sources**.
     * **Event provider** : Select **Pub/Sub**.
     * **Event type** : Select **google.cloud.pubsub.topic.v1.messagePublished**.
     * **Select a Cloud Pub/Sub topic** : Choose the topic `akamai-siem-trigger`.
     * **Region** : Select the same region as the function.
     * **Service account** : Select the service account you created for the function.
  6. Click **Save trigger**.

**Note:** The trigger options come from Eventarc. If **Pub/Sub trigger** is not listed, enable the **Eventarc API** for the project and reload the page. If you receive a message that the service account is missing the **Eventarc Event Receiver** or **Cloud Run Invoker** role, click **Grant**.
  7. In the **Authentication** section, select **Require authentication**.

  8. Expand **Containers, Networking, Security** , and on the **Security** tab set **Service account** to `akamai-siem-collector-sa`.

  9. On the **Containers > Variables & Secrets** tab, add the following environment variables:

Variable name | Example value  
---|---  
`GCS_BUCKET` | `akamai-siem-logs`  
`GCS_PREFIX` | `akamai-siem/`  
`STATE_KEY` | `akamai-siem-state.json`  
`AKAMAI_HOST` | `akab-xxxxxxxx.luna.akamaiapis.net`  
`AKAMAI_CLIENT_TOKEN` | `akab-client-token-xxxx`  
`AKAMAI_CLIENT_SECRET` | `your-client-secret`  
`AKAMAI_ACCESS_TOKEN` | `akab-access-token-xxxx`  
`AKAMAI_CONFIG_ID` | `12345`  
`LIMIT` | `10000`  
`WINDOW_SECONDS` | `3600`  
`HTTP_TIMEOUT` | `110`  
`MAX_PAGES` | `20`  
**Note:** `STATE_KEY` points outside the log prefix on purpose. The feed ingests every object under its bucket URI and, when a deletion option is selected, deletes what it transferred. Keeping the state file out of that prefix stops it from being ingested as log data and from being deleted, which would reset collection and re-ingest duplicate events.**Note:** Use the **Host** , **Client Token** , **Client Secret** , and **Access Token** from the **Create Akamai API credentials for SIEM Integration** section, and the **configId** from the **Enable SIEM Integration in Akamai Control Center** section.
  10. Set the **Request timeout** to `600` seconds and **Memory** to **512 MiB** or higher.

  11. Click **Create**. After the service is created, the inline code editor opens.




#### Add the function code

  1. In the **Function entry point** field, enter `main`.
  2. In the inline code editor, replace the contents of `main.py` with the following code:
         
         ```python
         import functions_framework
         from google.cloud import storage
         import json
         import os
         import time
         import uuid
         import requests
         from akamai.edgegrid import EdgeGridAuth
         
         storage_client = storage.Client()
         
         GCS_BUCKET = os.environ.get('GCS_BUCKET')
         GCS_PREFIX = os.environ.get('GCS_PREFIX', 'akamai-siem/')
         STATE_KEY = os.environ.get('STATE_KEY', 'akamai-siem-state.json')
         AKAMAI_HOST = os.environ.get('AKAMAI_HOST')
         CLIENT_TOKEN = os.environ.get('AKAMAI_CLIENT_TOKEN')
         CLIENT_SECRET = os.environ.get('AKAMAI_CLIENT_SECRET')
         ACCESS_TOKEN = os.environ.get('AKAMAI_ACCESS_TOKEN')
         CONFIG_ID = os.environ.get('AKAMAI_CONFIG_ID')
         LIMIT = int(os.environ.get('LIMIT', '10000'))
         WINDOW_SEC = int(os.environ.get('WINDOW_SECONDS', '3600'))
         HTTP_TIMEOUT = int(os.environ.get('HTTP_TIMEOUT', '110'))
         MAX_PAGES = int(os.environ.get('MAX_PAGES', '20'))
         
         def _session():
                 """Create a requests session that signs requests with Akamai EdgeGrid."""
                 session = requests.Session()
                 session.auth = EdgeGridAuth(
                         client_token=CLIENT_TOKEN,
                         client_secret=CLIENT_SECRET,
                         access_token=ACCESS_TOKEN,
                 )
                 return session
         
         def _load_state(bucket):
                 """Load the saved offset from GCS."""
                 try:
                         blob = bucket.blob(STATE_KEY)
                         if blob.exists():
                                 return json.loads(blob.download_as_text())
                 except Exception as e:
                         print(f'Warning: could not load state: {e}')
                 return {}
         
         def _save_state(bucket, state):
                 """Persist the offset to GCS for the next run."""
                 try:
                         bucket.blob(STATE_KEY).upload_from_string(
                                 json.dumps(state, separators=(',', ':')),
                                 content_type='application/json',
                         )
                 except Exception as e:
                         print(f'Warning: could not save state: {e}')
         
         def _fetch(session, offset, from_ts):
                 """Fetch one batch of events. Use offset when available, otherwise a time window.
         
                 The Akamai SIEM API does not allow combining the offset parameter with from/to.
                 """
                 url = f'https://{AKAMAI_HOST}/siem/v1/configs/{CONFIG_ID}'
                 params = {'limit': LIMIT}
                 if offset:
                         params['offset'] = offset
                 else:
                         params['from'] = int(from_ts)
                 resp = session.get(
                         url, params=params, timeout=HTTP_TIMEOUT,
                         headers={'Accept': 'application/json'},
                 )
                 resp.raise_for_status()
                 return resp.text
         
         def _parse_ndjson(text):
                 """Split the NDJSON response into event lines and the trailing context object.
         
                 Each line is a JSON security event; the last line is a context object that
                 contains the offset to use for the next request.
                 """
                 lines = [ln for ln in text.splitlines() if ln.strip()]
                 if not lines:
                         return [], {}
                 try:
                         context = json.loads(lines[-1])
                 except ValueError:
                         return lines, {}
                 if isinstance(context, dict) and 'offset' in context:
                         return lines[:-1], context
                 return lines, {}
         
         def _write_events(bucket, event_lines, page_num):
                 """Write a batch of raw JSON events to GCS, one event per line."""
                 ts_path = time.strftime('%Y/%m/%d', time.gmtime())
                 uniq = f'{int(time.time() * 1e6)}_{uuid.uuid4().hex[:8]}'
                 key = f'{GCS_PREFIX}{ts_path}/akamai_siem_p{page_num:03d}_{uniq}.json'
                 bucket.blob(key).upload_from_string(
                         '\n'.join(event_lines),
                         content_type='application/x-ndjson',
                 )
                 return key
         
         @functions_framework.cloud_event
         def main(cloud_event):
                 """Triggered by Pub/Sub to pull Akamai SIEM events and write them to GCS."""
                 if not all([GCS_BUCKET, AKAMAI_HOST, CLIENT_TOKEN, CLIENT_SECRET,
                                         ACCESS_TOKEN, CONFIG_ID]):
                         print('Error: missing required environment variables')
                         return
         
                 bucket = storage_client.bucket(GCS_BUCKET)
                 state = _load_state(bucket)
                 offset = state.get('offset')
                 from_ts = float(state.get('last_to_ts') or (time.time() - WINDOW_SEC))
         
                 session = _session()
                 pages = 0
                 total = 0
                 try:
                         while pages < MAX_PAGES:
                                 text = _fetch(session, offset, from_ts)
                                 events, context = _parse_ndjson(text)
                                 if events:
                                         _write_events(bucket, events, pages + 1)
                                         total += len(events)
                                 new_offset = context.get('offset')
                                 if new_offset:
                                         offset = new_offset
                                 pages += 1
                                 # Stop when this window is drained (fewer than LIMIT events returned).
                                 if not new_offset or len(events) < LIMIT:
                                         break
         
                         state['offset'] = offset
                         state['last_to_ts'] = time.time()
                         state['last_successful_run'] = time.time()
                         _save_state(bucket, state)
                         print(f'Retrieved {total} events across {pages} pages')
                 except Exception as e:
                         print(f'Error collecting Akamai SIEM logs: {e}')
                         raise
         ```
         

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

  3. Create a `requirements.txt` file with the following contents:
         
         ```none
         functions-framework==3.*
         google-cloud-storage==2.*
         requests>=2.31.0
         edgegrid-python>=1.3.1
         ```
         

  4. Click **Deploy** and wait for the deployment to complete.

**Note:** Akamai stops sending the SIEM API response after two minutes. Keep `HTTP_TIMEOUT` below 120 seconds and schedule the function frequently (for example, every five minutes) so each run completes within the window.



### Create a Cloud Scheduler job

  1. Go to **Cloud Scheduler**.
  2. Click **Create job**.
  3. Provide the following configuration details: 
     * **Name** : Enter `akamai-siem-collector-5min`.
     * **Region** : Select the same region as the Cloud Run function.
     * **Frequency** : Enter `*/5 * * * *` (every five minutes).
     * **Timezone** : Select **UTC**.
     * **Target type** : Select **Pub/Sub**.
     * **Topic** : Select `akamai-siem-trigger`.
     * **Message body** : Enter `{}`.
  4. Click **Create**.
  5. To verify the setup, click **Force run** on the job, and then check the Cloud Run logs and the bucket to confirm that events were written.



### Configure a feed in Google SecOps to ingest from Cloud Storage

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Akamai SIEM Connector GCS`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Akamai SIEM Connector** as the **Log type**.
  7. Click **Get Service Account** next to the **Chronicle Service Account** field, and copy the service account email.
  8. Click **Next**.
  9. Specify values for the following input parameters: 
     * **Storage Bucket URI** : Enter `gs://akamai-siem-logs/akamai-siem/`. This URL must end with a trailing forward slash (/).
     * **Source deletion options** : Select the deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
  10. Click **Next**.
  11. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



### Grant the Google SecOps service account access to the bucket

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email from the feed setup.
     * **Assign roles** : Select both of the following: 
       * **Storage Object Viewer** : reads the log objects.
       * **Storage Legacy Bucket Reader** : reads the bucket metadata. If you selected the **Delete transferred files and empty directories** deletion option, select **Storage Legacy Bucket Writer** instead, which also grants the delete permission.
  6. Click **Save**.



## Method 2: Amazon S3

Use this method to collect Akamai SIEM Connector logs into an Amazon S3 bucket using AWS Lambda and EventBridge.

### Configure an AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `akamai-siem-logs`).
  3. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**.
  5. Select **Security credentials** tab.
  6. Click **Create Access Key** in section **Access Keys**.
  7. Select **Third-party service** as **Use case**.
  8. Click **Next**. 
     * Optional: Add a description tag.
  9. Click **Create access key**.
  10. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  11. Click **Done**.
  12. Select **Permissions** tab.
  13. Click **Add permissions** in section **Permissions policies**.
  14. Select **Add permissions**.
  15. Select **Attach policies directly**.
  16. Search for **AmazonS3FullAccess** policy.
  17. Select the policy.
  18. Click **Next**.
  19. Click **Add permissions**.



### Configure the IAM policy and role for S3 uploads

  1. In the AWS console, go to **IAM > Policies > Create policy > JSON tab**.
  2. Copy and paste the following policy.

     * **Policy JSON** (replace `akamai-siem-logs` with your bucket name):
           
           {
               "Version": "2012-10-17",
               "Statement": [
                   {
                       "Sid": "AllowPutObjects",
                       "Effect": "Allow",
                       "Action": "s3:PutObject",
                       "Resource": "arn:aws:s3:::akamai-siem-logs/*"
                   },
                   {
                       "Sid": "AllowGetStateObject",
                       "Effect": "Allow",
                       "Action": "s3:GetObject",
                       "Resource": "arn:aws:s3:::akamai-siem-logs/akamai-siem-state.json"
                   }
               ]
           }
           

  3. Click **Next**.

  4. Enter policy name `AkamaiSIEMtoS3Policy` and click **Create policy**.

  5. Go to **IAM > Roles > Create role**.

  6. Select **AWS service**.

  7. Select **Lambda** as the use case.

  8. Click **Next**.

  9. Search for and select the policy `AkamaiSIEMtoS3Policy`.

  10. Click **Next**.

  11. Enter role name `AkamaiSIEMtoS3Role` and click **Create role**.




### Create the Lambda function

  1. In the **AWS Console** , go to **Lambda > Functions > Create function**.
  2. Click **Author from scratch**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `AkamaiSIEMtoS3Function`  
**Runtime** | Python 3.13  
**Architecture** | x86_64  
**Execution role** | Use an existing role  
**Existing role** | `AkamaiSIEMtoS3Role`  
  4. Click **Create function**.

  5. After the function is created, open the **Code** tab, delete the stub and paste the following code:
         
         ```python
         import json
         import boto3
         import os
         import urllib3
         import hmac
         import hashlib
         import base64
         from datetime import datetime
         from urllib.parse import urlparse, urljoin
         
         # Configuration from environment variables
         S3_BUCKET = os.environ['S3_BUCKET']
         S3_PREFIX = os.environ.get('S3_PREFIX', 'akamai-siem/')
         STATE_KEY = os.environ.get('STATE_KEY', 'akamai-siem-state.json')
         
         AKAMAI_HOST = os.environ['AKAMAI_HOST']
         AKAMAI_CLIENT_TOKEN = os.environ['AKAMAI_CLIENT_TOKEN']
         AKAMAI_CLIENT_SECRET = os.environ['AKAMAI_CLIENT_SECRET']
         AKAMAI_ACCESS_TOKEN = os.environ['AKAMAI_ACCESS_TOKEN']
         AKAMAI_CONFIG_IDS = os.environ['AKAMAI_CONFIG_IDS'].split(',')
         
         LIMIT = int(os.environ.get('LIMIT', '10000'))
         
         s3_client = boto3.client('s3')
         http = urllib3.PoolManager()
         
         def load_state():
                 """Load offset state from S3"""
                 try:
                         response = s3_client.get_object(Bucket=S3_BUCKET, Key=STATE_KEY)
                         return json.loads(response['Body'].read().decode('utf-8'))
                 except s3_client.exceptions.NoSuchKey:
                         # Only a missing object is a cold start. Any other error is raised:
                         # swallowing it would drop the saved offset and restart collection.
                         return {}
         
         def save_state(state):
                 """Save offset state to S3.
         
                 Failures are raised, not logged. If the state write fails after the
                 events were uploaded, the next run repeats the same batch and duplicates it.
                 """
                 s3_client.put_object(
                         Bucket=S3_BUCKET,
                         Key=STATE_KEY,
                         Body=json.dumps(state, indent=2).encode('utf-8'),
                         ContentType='application/json'
                 )
         
         def make_edgegrid_auth_header(url, method='GET'):
                 """Create EdgeGrid authentication header"""
                 timestamp = datetime.utcnow().strftime('%Y%m%dT%H:%M:%S+0000')
                 nonce = base64.b64encode(os.urandom(16)).decode('utf-8')
         
                 parsed_url = urlparse(url)
                 relative_url = parsed_url.path
                 if parsed_url.query:
                         relative_url += '?' + parsed_url.query
         
                 auth_header = f'EG1-HMAC-SHA256 ' \
                                         f'client_token={AKAMAI_CLIENT_TOKEN};' \
                                         f'access_token={AKAMAI_ACCESS_TOKEN};' \
                                         f'timestamp={timestamp};' \
                                         f'nonce={nonce};'
         
                 data_to_sign = '\t'.join([
                         method,
                         parsed_url.scheme,
                         parsed_url.netloc,
                         relative_url,
                         '',  # Request body for GET
                         '',  # No additional headers
                 ])
         
                 signing_key = hmac.new(
                         AKAMAI_CLIENT_SECRET.encode('utf-8'),
                         timestamp.encode('utf-8'),
                         hashlib.sha256
                 ).digest()
         
                 auth_signature = base64.b64encode(
                         hmac.new(
                                 signing_key,
                                 (data_to_sign + auth_header).encode('utf-8'),
                                 hashlib.sha256
                         ).digest()
                 ).decode('utf-8')
         
                 return auth_header + f'signature={auth_signature}'
         
         def fetch_akamai_events(config_id, offset=None):
                 """Fetch events from Akamai SIEM API"""
                 base_url = f'https://{AKAMAI_HOST}'
                 endpoint = f'/siem/v1/configs/{config_id}'
         
                 params = f'limit={LIMIT}'
                 if offset:
                         params += f'&offset={offset}'
         
                 url = f'{base_url}{endpoint}?{params}'
         
                 headers = {
                         'Authorization': make_edgegrid_auth_header(url)
                 }
         
                 # Any transport or HTTP failure is raised so the invocation fails visibly
                 # and the saved offset is left untouched for the next run.
                 response = http.request('GET', url, headers=headers, timeout=120)
         
                 if response.status != 200:
                         raise RuntimeError(
                                 f"Akamai SIEM API returned {response.status} for config {config_id}: "
                                 f"{response.data.decode('utf-8', 'replace')}"
                         )
         
                 # Parse multi-JSON response (newline-delimited JSON)
                 lines = response.data.decode('utf-8').strip().split('\n')
                 events = []
                 new_offset = offset
         
                 for line in lines:
                         if not line.strip():
                                 continue
                         try:
                                 obj = json.loads(line)
                         except json.JSONDecodeError as e:
                                 print(f"Warning: Failed to parse line: {e}")
                                 continue
         
                         # Check if this is offset context (metadata object with offset)
                         if 'offset' in obj and ('total' in obj or 'responseContext' in obj):
                                 new_offset = obj.get('offset')
                                 continue
         
                         # This is an event
                         events.append(obj)
         
                 return events, new_offset
         
         def lambda_handler(event, context):
                 """Lambda handler - fetches Akamai events and writes to S3"""
                 print(f"Starting Akamai SIEM fetch at {datetime.utcnow().isoformat()}Z")
         
                 state = load_state()
                 total_events = 0
         
                 for config_id in AKAMAI_CONFIG_IDS:
                         config_id = config_id.strip()
                         if not config_id:
                                 continue
         
                         print(f"Fetching events for config: {config_id}")
         
                         current_offset = state.get(config_id)
                         events, new_offset = fetch_akamai_events(config_id, current_offset)
         
                         if events:
                                 print(f"Fetched {len(events)} events for config {config_id}")
         
                                 # Write events to S3 as newline-delimited JSON
                                 timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
                                 s3_key = f'{S3_PREFIX}{config_id}/{timestamp}.json'
         
                                 payload = '\n'.join(json.dumps(event) for event in events)
         
                                 # A failed upload raises: the offset stays where it was and the
                                 # next run fetches the same batch again.
                                 s3_client.put_object(
                                         Bucket=S3_BUCKET,
                                         Key=s3_key,
                                         Body=payload.encode('utf-8'),
                                         ContentType='application/json'
                                 )
                                 print(f"Wrote {len(events)} events to s3://{S3_BUCKET}/{s3_key}")
         
                                 # Update offset only after successful write
                                 if new_offset:
                                         state[config_id] = new_offset
                                         total_events += len(events)
                         else:
                                 print(f"No new events for config {config_id}")
         
                 # Save updated state
                 save_state(state)
         
                 return {
                         'statusCode': 200,
                         'body': json.dumps({
                                 'message': f'Successfully processed {total_events} events',
                                 'configs_processed': len(AKAMAI_CONFIG_IDS)
                         })
                 }
         ```
         

  6. Click **Deploy** to save the code.

  7. Go to **Configuration > Environment variables > Edit**.

  8. Click **Add environment variable** for each of the following:

Key | Example value  
---|---  
`S3_BUCKET` | `akamai-siem-logs`  
`S3_PREFIX` | `akamai-siem/`  
`STATE_KEY` | `akamai-siem-state.json`  
`AKAMAI_HOST` | `akab-xxxxxxxx.luna.akamaiapis.net`  
`AKAMAI_CLIENT_TOKEN` | `your-client-token`  
`AKAMAI_CLIENT_SECRET` | `your-client-secret`  
`AKAMAI_ACCESS_TOKEN` | `your-access-token`  
`AKAMAI_CONFIG_IDS` | `12345,67890`  
`LIMIT` | `10000`  
**Note:** `STATE_KEY` points outside the log prefix on purpose. The feed ingests every object under its bucket URI and, when a deletion option is selected, deletes what it transferred. Keeping the state file out of that prefix stops it from being ingested as log data and from being deleted, which would reset collection and re-ingest duplicate events.
  9. Click **Save**.

  10. Select the **Configuration** tab.

  11. In the **General configuration** panel click **Edit**.

  12. Change **Timeout** to **5 minutes (300 seconds)** and click **Save**.

**Note:** Timeout is a hard upper limit. If the function is still running when the timer hits 5 minutes, AWS Lambda will terminate it. You are only billed for actual run time.



### Create an EventBridge schedule

  1. Go to **Amazon EventBridge > Scheduler > Create schedule**.
  2. Provide the following configuration details: 
     * **Schedule name** : Enter `AkamaiSIEMtoS3-5min`.
     * **Schedule pattern** : Select **Recurring schedule**.
     * **Schedule type** : Select **Rate-based schedule**.
     * **Rate expression** : Enter `5` and select **Minutes**.
  3. Click **Next**.
  4. Provide the following configuration details: 
     * **Target** : Select **AWS Lambda Invoke**.
     * **Lambda function** : Select `AkamaiSIEMtoS3Function`.
  5. Click **Next**.
  6. Click **Next** (skip optional settings).
  7. Review and click **Create schedule**.



### Configure a feed in Google SecOps to ingest Akamai SIEM Connector logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name** (for example, `Akamai SIEM Connector`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Akamai SIEM Connector** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following input parameters:

     * **S3 URI** : `s3://akamai-siem-logs/akamai-siem/`
     * **Source deletion option** : Select the deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label applied to the events from this feed.
**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
  9. Click **Next** and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`accept_language` | `additional.fields` | Merged  
`additional_policy_key` | `additional.fields` | Merged  
`attackData_label` | `additional.fields` | Merged  
`attackData_ruleActions_label` | `additional.fields` | Merged  
`attackData_ruleData_label` | `additional.fields` | Merged  
`attackData_ruleSelectors_label` | `additional.fields` | Merged  
`attackdata_ruleMessages_label` | `additional.fields` | Merged  
`attackdata_ruleTags_label` | `additional.fields` | Merged  
`attackdata_ruleVersions_label` | `additional.fields` | Merged  
`botData_label` | `additional.fields` | Merged  
`continent_label` | `additional.fields` | Merged  
`dur_label` | `additional.fields` | Merged  
`etag_label` | `additional.fields` | Merged  
`format_label` | `additional.fields` | Merged  
`httpMessage_query_label` | `additional.fields` | Merged  
`httpMessage_response_headers_label` | `additional.fields` | Merged  
`identity_label` | `additional.fields` | Merged  
`identityv2_label` | `additional.fields` | Merged  
`mime_version_label` | `additional.fields` | Merged  
`regionCode_label` | `additional.fields` | Merged  
`req_id_label` | `additional.fields` | Merged  
`requestHeaders_label` | `additional.fields` | Merged  
`responseSegment_label` | `additional.fields` | Merged  
`ruleAction_list` | `additional.fields` | Merged  
`ruleData_list` | `additional.fields` | Merged  
`ruleMessages_list` | `additional.fields` | Merged  
`ruleSelectors_list` | `additional.fields` | Merged  
`ruleTags_list` | `additional.fields` | Merged  
`ruleVersions_list` | `additional.fields` | Merged  
`rules_list` | `additional.fields` | Merged  
`same_site` | `additional.fields` | Merged  
`telemetryType_label` | `additional.fields` | Merged  
`Date` | `metadata.event_timestamp` | Parsed as `EEE, dd MMM yyyy HH:mm:ss ZZZ`  
`expires` | `metadata.event_timestamp` | Parsed as `EEE, dd-MMM-yyyy HH:mm:ss ZZZ`  
`httpMessage.start` | `metadata.event_timestamp` | Parsed as `UNIX`  
`event_type` | `metadata.event_type` | Directly mapped  
`attackData.configId` | `metadata.product_log_id` | Directly mapped  
`version` | `metadata.product_version` | Directly mapped  
`protocol` | `network.application_protocol` | Directly mapped  
`MS-ASProtocolVersion` | `network.application_protocol_version` | Directly mapped  
`httpMessage.method` | `network.http.method` | Directly mapped  
`httpMessage.status` | `network.http.response_code` | Renamed/mapped  
`User-Agent` | `network.http.user_agent` | Directly mapped  
`httpMessage.bytes` | `network.sent_bytes` | Renamed/mapped  
`ASP.NET_SessionId` | `network.session_id` | Directly mapped  
`httpMessage.requestId` | `network.session_id` | Directly mapped  
`httpMessage.tls` | `network.tls.version` | Directly mapped  
`attackData.clientIP` | `principal.asset.ip` | Merged  
`attackData.clientIP` | `principal.ip` | Merged  
`geo.city` | `principal.location.city` | Directly mapped  
`geo.country` | `principal.location.country_or_region` | Directly mapped  
`geo.asn` | `principal.location.name` | Directly mapped  
`additional_content_Security_Policy` | `principal.resource.attribute.labels` | Merged  
`DeviceType` | `principal.resource.name` | Directly mapped  
`DeviceId` | `principal.resource.product_object_id` | Directly mapped  
`cache_label` | `security_result.about.labels` | Merged  
`accept_encoding_label` | `security_result.about.resource.attribute.labels` | Merged  
`accept_label` | `security_result.about.resource.attribute.labels` | Merged  
`connection_label` | `security_result.about.resource.attribute.labels` | Merged  
`content_encoding` | `security_result.about.resource.attribute.labels` | Merged  
`content_length_label` | `security_result.about.resource.attribute.labels` | Merged  
`content_type_label` | `security_result.about.resource.attribute.labels` | Merged  
`req_content_length_label` | `security_result.about.resource.attribute.labels` | Merged  
`req_content_type_label` | `security_result.about.resource.attribute.labels` | Merged  
`desc` | `security_result.description` | Directly mapped  
`CP_IsMobile_label` | `security_result.detection_fields` | Merged  
`X-BEServer_label` | `security_result.detection_fields` | Merged  
`X-CalculatedBETarget_label` | `security_result.detection_fields` | Merged  
`X-Content-Type-Options_label` | `security_result.detection_fields` | Merged  
`X-DiagInfo_label` | `security_result.detection_fields` | Merged  
`X-FEServer_label` | `security_result.detection_fields` | Merged  
`X-MS-BackOffDuration_label` | `security_result.detection_fields` | Merged  
`apiId_label` | `security_result.detection_fields` | Merged  
`backend_label` | `security_result.detection_fields` | Merged  
`p3p_label` | `security_result.detection_fields` | Merged  
`type_label` | `security_result.detection_fields` | Merged  
`vary_label` | `security_result.detection_fields` | Merged  
`attackData.policyId` | `security_result.summary` | Directly mapped  
`Host` | `target.asset.hostname` | Directly mapped  
`httpMessage.host` | `target.asset.hostname` | Directly mapped  
`path` | `target.file.full_path` | Directly mapped  
`Host` | `target.hostname` | Directly mapped  
`httpMessage.host` | `target.hostname` | Directly mapped  
`httpMessage.port` | `target.port` | Directly mapped  
`Cmd` | `target.process.command_line` | Directly mapped  
`httpMessage.path` | `target.url` | Directly mapped  
`User` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `AKAMAI_SIEM_CONNECTOR`  
N/A | `metadata.vendor_name` | Constant: `AKAMAI_SIEM_CONNECTOR`  
N/A | `principal.resource.resource_type` | Constant: `DEVICE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-siem-connector-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
