---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digital-shadows-ioc/
title: Collect ReliaQuest GreyMatter DRP Indicators (formerly Digital Shadows) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:32.382910+00:00
---

# Collect ReliaQuest GreyMatter DRP Indicators (formerly Digital Shadows) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digital-shadows-ioc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ReliaQuest GreyMatter DRP Indicators (formerly Digital Shadows) logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can ingest ReliaQuest GreyMatter DRP (formerly known as Digital Shadows) Indicators logs to Google Security Operations using Amazon S3.

ReliaQuest GreyMatter DRP is a digital risk protection platform that continuously monitors and detects external threats, data exposures, and brand impersonation across the open web, deep web, dark web, and social media. It provides threat intelligence, incident alerts, and indicators of compromise (IOCs) to help organizations identify and mitigate digital risks.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to Digital Shadows Indicators portal
  * Privileged access to AWS (S3, IAM)
  * Active subscription to Digital Shadows Indicators with API access enabled



## Collect Digital Shadows Indicators API credentials

  1. Sign in to the **Digital Shadows Indicators Portal** at `https://portal-digitalshadows.com`.
  2. Go to **Settings > API Credentials**.
  3. If you don't have an existing API key, click **Create New API Client** or **Generate API Key**.
  4. Copy and save in a secure location the following details: 
     * **API Key** : Your 6-character API key
     * **API Secret** : Your 32-character API secret
     * **Account ID** : Your account ID (displayed in the portal or provided by your Digital Shadows representative)
     * **API Base URL** : `https://api.searchlight.app/v1` or `https://portal-digitalshadows.com/api/v1` (depending on your tenant region)

**Note:** These credentials will be used by the AWS Lambda function to authenticate to the Digital Shadows Indicators API. If you need assistance obtaining API credentials, contact your Digital Shadows representative at drpsupport@reliaquest.com.

## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `digital-shadows-logs`).
  3. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**.
  5. Select **Security credentials** tab.
  6. Click **Create Access Key** in section **Access Keys**.
  7. Select **Third-party service** as **Use case**.
  8. Click **Next**.
  9. Optional: Add description tag.
  10. Click **Create access key**.
  11. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  12. Click **Done**.
  13. Select **Permissions** tab.
  14. Click **Add permissions** in section **Permissions policies**.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**.
  17. Search for **AmazonS3FullAccess** policy.
  18. Select the policy.
  19. Click **Next**.
  20. Click **Add permissions**.



## Configure the IAM policy and role for S3 uploads

  1. In the AWS console, go to **IAM > Policies > Create policy > JSON tab**.
  2. Copy and paste the policy below.
  3. **Policy JSON** (replace `digital-shadows-logs` if you entered a different bucket name):
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Sid": "AllowPutObjects",
                     "Effect": "Allow",
                     "Action": "s3:PutObject",
                     "Resource": "arn:aws:s3:::digital-shadows-logs/*"
                 },
                 {
                     "Sid": "AllowGetStateObject",
                     "Effect": "Allow",
                     "Action": "s3:GetObject",
                     "Resource": "arn:aws:s3:::digital-shadows-logs/digital-shadows/state.json"
                 }
             ]
         }
         

  4. Click **Next > Create policy**.

  5. Go to **IAM > Roles > Create role > AWS service > Lambda**.

  6. Attach the newly created policy.

  7. Name the role `DigitalShadowsLambdaRole` and click **Create role**.




## Create the Lambda function

  1. In the **AWS Console** , go to **Lambda > Functions > Create function**.
  2. Click **Author from scratch**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `DigitalShadowsCollector`  
**Runtime** | Python 3.13  
**Architecture** | x86_64  
**Execution role** | `DigitalShadowsLambdaRole`  
  4. After the function is created, open the **Code** tab, delete the stub and paste the code below (**DigitalShadowsCollector.py**).
         
         import urllib3
         import json
         import boto3
         import os
         import base64
         import logging
         import time
         from datetime import datetime, timedelta, timezone
         from urllib.parse import urlencode
         
         logger = logging.getLogger()
         logger.setLevel(logging.INFO)
         
         HTTP = urllib3.PoolManager(retries=False)
         storage_client = boto3.client('s3')
         
         def _basic_auth_header(key: str, secret: str) -> str:
             token = base64.b64encode(f"{key}:{secret}".encode("utf-8")).decode("utf-8")
             return f"Basic {token}"
         
         def _load_state(bucket, key, default_days=30) -> str:
             """Return ISO8601 checkpoint (UTC)."""
             try:
                 response = storage_client.get_object(Bucket=bucket, Key=key)
                 state_data = response['Body'].read().decode('utf-8')
                 state = json.loads(state_data)
                 ts = state.get("last_timestamp")
                 if ts:
                     return ts
             except storage_client.exceptions.NoSuchKey:
                 logger.info("No previous state found, starting from default lookback")
             except Exception as e:
                 logger.warning(f"State read error: {e}")
             return (datetime.now(timezone.utc) - timedelta(days=default_days)).isoformat()
         
         def _save_state(bucket, key, ts: str) -> None:
             storage_client.put_object(
                 Bucket=bucket,
                 Key=key,
                 Body=json.dumps({"last_timestamp": ts}),
                 ContentType="application/json"
             )
         
         def _get_json(url: str, headers: dict, params: dict, backoff_s=2, max_retries=3) -> dict:
             qs = f"?{urlencode(params)}" if params else ""
             for attempt in range(max_retries):
                 r = HTTP.request("GET", f"{url}{qs}", headers=headers)
                 if r.status == 200:
                     return json.loads(r.data.decode("utf-8"))
                 if r.status in (429, 500, 502, 503, 504):
                     wait = backoff_s * (2 ** attempt)
                     logger.warning(f"HTTP {r.status} from DS API, retrying in {wait}s")
                     time.sleep(wait)
                     continue
                 raise RuntimeError(f"DS API error {r.status}: {r.data[:200]}")
             raise RuntimeError("Exceeded retry budget for DS API")
         
         def _collect(api_base, headers, path, since_ts, account_id, page_size, max_pages, time_param):
             items = []
             for page in range(max_pages):
                 params = {
                     "limit": page_size,
                     "offset": page * page_size,
                     time_param: since_ts,
                 }
                 if account_id:
                     params["account-id"] = account_id
                 data = _get_json(f"{api_base}/{path}", headers, params)
                 batch = data.get("items") or data.get("data") or []
                 if not batch:
                     break
                 items.extend(batch)
                 if len(batch) < page_size:
                     break
             return items
         
         def lambda_handler(event, context):
             bucket_name = os.environ["S3_BUCKET"]
             api_key = os.environ["DS_API_KEY"]
             api_secret = os.environ["DS_API_SECRET"]
             prefix = os.environ.get("S3_PREFIX", "digital-shadows")
             state_key = os.environ.get("STATE_KEY", "digital-shadows/state.json")
             api_base = os.environ.get("API_BASE", "https://api.searchlight.app/v1")
             account_id = os.environ.get("DS_ACCOUNT_ID", "")
             page_size = int(os.environ.get("PAGE_SIZE", "100"))
             max_pages = int(os.environ.get("MAX_PAGES", "10"))
         
             try:
                 last_ts = _load_state(bucket_name, state_key)
                 logger.info(f"Checkpoint: {last_ts}")
         
                 headers = {
                     "Authorization": _basic_auth_header(api_key, api_secret),
                     "Accept": "application/json",
                     "User-Agent": "Chronicle-DigitalShadows-S3/1.0",
                 }
         
                 records = []
         
                 incidents = _collect(
                     api_base, headers, "incidents", last_ts, account_id,
                     page_size, max_pages, time_param="published-after"
                 )
                 for incident in incidents:
                     incident['_source_type'] = 'incident'
                 records.extend(incidents)
         
                 intel_incidents = _collect(
                     api_base, headers, "intel-incidents", last_ts, account_id,
                     page_size, max_pages, time_param="published-after"
                 )
                 for intel in intel_incidents:
                     intel['_source_type'] = 'intelligence_incident'
                 records.extend(intel_incidents)
         
                 indicators = _collect(
                     api_base, headers, "indicators", last_ts, account_id,
                     page_size, max_pages, time_param="lastUpdated-after"
                 )
                 for indicator in indicators:
                     indicator['_source_type'] = 'ioc'
                 records.extend(indicators)
         
                 if records:
                     newest = max(
                         (r.get("updated") or r.get("raised") or r.get("lastUpdated") or last_ts)
                         for r in records
                     )
                     key = f"{prefix}/digital_shadows_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json"
                     body = "\n".join(json.dumps(r, separators=(",", ":")) for r in records)
                     storage_client.put_object(
                         Bucket=bucket_name,
                         Key=key,
                         Body=body,
                         ContentType="application/x-ndjson"
                     )
                     _save_state(bucket_name, state_key, newest)
                     msg = f"Wrote {len(records)} records to s3://{bucket_name}/{key}"
                 else:
                     msg = "No new records"
         
                 logger.info(msg)
                 return {'statusCode': 200, 'body': json.dumps({'message': msg, 'records': len(records) if records else 0})}
         
             except Exception as e:
                 logger.error(f"Error processing logs: {str(e)}")
                 raise
         

  5. Go to **Configuration > Environment variables > Edit > Add new environment variable**.

  6. Enter the environment variables provided below, replacing with your values.




**Environment variables**

Key | Example value  
---|---  
`S3_BUCKET` | `digital-shadows-logs`  
`S3_PREFIX` | `digital-shadows/`  
`STATE_KEY` | `digital-shadows/state.json`  
`DS_API_KEY` | `ABC123` (your 6-character API key)  
`DS_API_SECRET` | `your-32-character-api-secret`  
`API_BASE` | `https://api.searchlight.app/v1`  
`DS_ACCOUNT_ID` | `your-account-id`  
`PAGE_SIZE` | `100`  
`MAX_PAGES` | `10`  
  
  1. After the function is created, stay on its page (or open **Lambda > Functions > DigitalShadowsCollector**).
  2. Select the **Configuration** tab.
  3. In the **General configuration** panel click **Edit**.
  4. Change **Timeout** to **5 minutes (300 seconds)** and click **Save**.

**Note:** Timeout is a hard upper limit, meaning if the function is still running when the timer hits 5 minutes, AWS Lambda will terminate it. Any shorter execution just finishes normally; you are billed only for the actual run time.

## Create an EventBridge schedule

  1. Go to **Amazon EventBridge > Scheduler > Create schedule**.
  2. Provide the following configuration details: 
     * **Recurring schedule** : **Rate** (`1 hour`)
     * **Target** : Your Lambda function `DigitalShadowsCollector`
     * **Name** : `DigitalShadowsCollector-1h`
  3. Click **Create schedule**.



## Configure a feed in Google SecOps to ingest Digital Shadows Indicators logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name**.
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Digital Shadows Indicators** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields:

     * **S3 URI** : `s3://digital-shadows-logs/digital-shadows/`
     * **Source deletion option** : Select the deletion option according to your preference
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Access Key ID** : User access key with access to the S3 bucket
     * **Secret Access Key** : User secret key with access to the S3 bucket
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
  9. Click **Next** and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
value | entity.entity.file.md5 | Set if type == "MD5"  
value | entity.entity.file.sha1 | Set if type == "SHA1"  
value | entity.entity.file.sha256 | Set if type == "SHA256"  
value | entity.entity.hostname | Set if type == "HOST"  
value | entity.entity.ip | Value copied directly if type == "IP"  
value | entity.entity.url | Set if type == "URL"  
value | entity.entity.user.email_addresses | Value copied directly if type == "EMAIL"  
type | entity.metadata.entity_type | Set to "DOMAIN_NAME" if type == "HOST", "IP_ADDRESS" if type == "IP", "URL" if type == "URL", "USER" if type == "EMAIL", "FILE" if type in ["SHA1","SHA256","MD5"], else "UNKNOWN_ENTITYTYPE"  
lastUpdated | entity.metadata.interval.start_time | Converted from ISO8601 to timestamp if not empty  
id | entity.metadata.product_entity_id | Value copied directly if not empty  
attributionTag.id, attributionTag.name, attributionTag.type | entity.metadata.threat.about.labels | Merged with objects {key: tag field name, value: tag value} if not empty  
sourceType | entity.metadata.threat.category_details | Value copied directly  
| entity.metadata.threat.threat_feed_name | Set to "Indicators"  
id | entity.metadata.threat.threat_id | Value copied directly if not empty  
sourceIdentifier | entity.metadata.threat.url_back_to_product | Value copied directly  
| entity.metadata.product_name | Set to "Indicators"  
| entity.metadata.vendor_name | Set to "Digital Shadows"  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
