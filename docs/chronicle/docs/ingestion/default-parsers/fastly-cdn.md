---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fastly-cdn/
title: Collect Fastly CDN logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:56.080516+00:00
---

# Collect Fastly CDN logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fastly-cdn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fastly CDN logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Fastly CDN logs to Google Security Operations using Amazon S3.

Fastly is a content delivery network (CDN) and edge cloud platform that provides real-time content delivery, security, and edge computing services. Fastly's Real-Time Log Streaming feature can send CDN access logs, WAF events, and other telemetry data to various destinations including Amazon S3 for security monitoring and analysis.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Fastly** control panel or API
  * Privileged access to **AWS** (S3, IAM)
  * A Fastly API token with `global` or `global:read` scope



## Create Fastly API token

  1. Sign in to the **Fastly control panel** at https://manage.fastly.com.
  2. Click your **user icon** in the upper-right corner.
  3. Go to **Account > Personal API tokens**.
  4. Click **Create Token**.
  5. In the **Create API Token** dialog, provide the following: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps S3 Logging Configuration`).
     * **Type** : Select **User token**.
     * **Scope** : Select **Global access** (required to configure logging endpoints).
     * **Expiration** : Select **Never expire** or set an appropriate expiration date.
  6. Click **Create Token**.
  7. Copy and save the API token securely.

**Note:** The API token is displayed only once. If you lose it, you must create a new token.

## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. Save bucket **Name** and **Region** for future reference (for example, `fastly-cdn-logs`).
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
  13. Select the **Permissions** tab.
  14. Click **Add permissions** in section **Permissions policies**.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**.
  17. Search for **AmazonS3FullAccess** policy.
  18. Select the policy.
  19. Click **Next**.
  20. Click **Add permissions**.



## Configure Fastly S3 logging endpoint

### Option A: Configure via Fastly control panel

  1. Sign in to the **Fastly control panel** at https://manage.fastly.com
  2. Select the **service** you want to configure logging for.
  3. Click **Edit configuration** and select **Clone active version** to create a new draft version.
  4. Click **Logging** in the left navigation menu.
  5. In the **Amazon Web Services S3** section, click **Create endpoint**.
  6. In the **Create an Amazon S3 endpoint** form, provide the following configuration details:

     * **Basic settings:**

       * **Name** : Enter a descriptive name (for example, `secops-s3-logs`).
       * **Placement** : Select **Format Version Default** (recommended).
       * **Log format** : Enter the following JSON format string:
             
             {"timestamp":"%{begin:%Y-%m-%dT%H:%M:%S%z}t","client_ip":"%{req.http.Fastly-Client-IP}V","geo_country":"%{client.geo.country_name}V","geo_city":"%{client.geo.city}V","geo_region":"%{client.geo.region}V","datacenter":"%{server.datacenter}V","host":"%{if(req.http.Fastly-Orig-Host, req.http.Fastly-Orig-Host, req.http.Host)}V","url":"%{json.escape(req.url)}V","request_method":"%{json.escape(req.method)}V","request_protocol":"%{json.escape(req.proto)}V","request_referer":"%{json.escape(req.http.referer)}V","request_user_agent":"%{json.escape(req.http.User-Agent)}V","response_state":"%{json.escape(fastly_info.state)}V","response_status":%{resp.status}V,"response_reason":%{if(resp.response, "\"%22\"+json.escape(resp.response)+\"%22\", \"null\")}V,"response_body_size":%{resp.body_bytes_written}V,"response_header_size":%{resp.header_bytes_written}V,"request_body_size":%{req.body_bytes_read}V,"request_header_size":%{req.header_bytes_read}V,"cache_status":"%{fastly_info.state}V","is_tls":"%{if(req.is_ssl, \"true\", \"false\")}V","tls_protocol":"%{cstr_escape(tls.client.protocol)}V","tls_cipher":"%{cstr_escape(tls.client.cipher)}V","server_identity":"%{json.escape(server.identity)}V","is_edge":%{if(fastly.ff.visits_this_service == 0, "true", "false")}V,"time_elapsed_usec":%{time.elapsed.usec}V,"time_start_sec":%{time.start.sec}V}
             

**Note:** This format includes essential CDN fields, geographic data, TLS information, and timing metrics. You can customize this format based on your requirements using variables from the [Useful variables to log](https://docs.fastly.com/en/guides/useful-variables-to-log) documentation.
       * **Timestamp format** : Leave as default (strftime compatible string).

**S3 bucket configuration:**

     * **Bucket name** : Enter the S3 bucket name (for example, `fastly-cdn-logs`).
     * **Domain** : Leave empty if your bucket is in US Standard region. For other regions, enter the appropriate S3 endpoint (for example, `s3-us-west-2.amazonaws.com` for us-west-2 region).
     * **Access method** : Select **User Credentials**
     * **Access key** : Enter the AWS access key from step 11.
     * **Secret key** : Enter the AWS secret access key from step 11.
     * **Period** : Enter `3600` (logs are finalized every hour).
  7. Click **Advanced options** to expand additional settings:

**Advanced settings:**

     * **Path** : Enter `fastly-cdn/` (optional prefix for organizing logs within the bucket).
     * **PGP public key** : Leave empty (encryption not required for this integration).
     * **Select a log line format** : Select **Blank** (we're using custom JSON format).
     * **Compression** : Select **gzip** (recommended to reduce storage costs).
     * **Redundancy level** : Select **Standard**.
     * **ACL** : Select **private** (recommended).
     * **Server side encryption** : Select **None** (or configure as per your security requirements).
     * **Maximum bytes** : Enter `0` (no maximum file size limit).
  8. Click **Create** to create the logging endpoint.

  9. Click **Activate** in the top-right corner.

  10. Select **Activate on Production** to deploy your configuration changes.

  11. In the confirmation dialog, click **Activate** to confirm.


**Note:** Fastly will begin streaming logs to S3 immediately. Files are finalized and made available for reading based on the configured period (default 3600 seconds).

### Option B: Configure via Fastly API

If you prefer to configure logging via API, use the following approach:

  1. Get your Fastly service ID from the control panel or by listing services:
         
         curl -H "Fastly-Key: YOUR_FASTLY_TOKEN" https://api.fastly.com/service
         

  2. Clone the active version to create a new draft version:
         
         curl -X PUT -H "Fastly-Key: YOUR_FASTLY_TOKEN" \
           "https://api.fastly.com/service/SERVICE_ID/version/ACTIVE_VERSION/clone"
         

  3. Create the S3 logging endpoint on the new draft version:
         
         curl -X POST -H "Fastly-Key: YOUR_FASTLY_TOKEN" \
           -H "Content-Type: application/x-www-form-urlencoded" \
           "https://api.fastly.com/service/SERVICE_ID/version/NEW_VERSION/logging/s3" \
           --data-urlencode 'name=secops-s3-logs' \
           --data-urlencode 'bucket_name=fastly-cdn-logs' \
           --data-urlencode 'access_key=YOUR_AWS_ACCESS_KEY' \
           --data-urlencode 'secret_key=YOUR_AWS_SECRET_KEY' \
           --data-urlencode 'path=fastly-cdn/' \
           --data-urlencode 'period=3600' \
           --data-urlencode 'gzip_level=9' \
           --data-urlencode 'format_version=2' \
           --data-urlencode 'format={"timestamp":"%{begin:%Y-%m-%dT%H:%M:%S%z}t","client_ip":"%{req.http.Fastly-Client-IP}V","geo_country":"%{client.geo.country_name}V","geo_city":"%{client.geo.city}V","host":"%{if(req.http.Fastly-Orig-Host, req.http.Fastly-Orig-Host, req.http.Host)}V","url":"%{json.escape(req.url)}V","request_method":"%{json.escape(req.method)}V","response_status":%{resp.status}V,"cache_status":"%{fastly_info.state}V"}'
         

  4. Activate the new version:
         
         curl -X PUT -H "Fastly-Key: YOUR_FASTLY_TOKEN" \
           "https://api.fastly.com/service/SERVICE_ID/version/NEW_VERSION/activate"
         


**Note:** Replace `SERVICE_ID`, `ACTIVE_VERSION`, `NEW_VERSION`, `YOUR_FASTLY_TOKEN`, `YOUR_AWS_ACCESS_KEY`, and `YOUR_AWS_SECRET_KEY` with your actual values.

## Verify log delivery to S3

  1. Wait approximately 1 hour (based on the configured period) for the first log file to be finalized.
  2. In the **AWS Console** , go to **S3 > Buckets**.
  3. Click your bucket name (for example, `fastly-cdn-logs`).
  4. Navigate to the `fastly-cdn/` prefix folder.
  5. Verify that log files are being created with naming pattern similar to:
         
         fastly-cdn/YYYY-MM-DD-HH-MM-SS-RANDOM_STRING.log.gz
         

  6. Download a sample log file and verify the JSON format matches your configuration.




## Configure a feed in Google SecOps to ingest Fastly CDN logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name**.
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Fastly CDN** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields:

     * **S3 URI** : `s3://fastly-cdn-logs/fastly-cdn/`.
     * **Source deletion option** : Select the deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
  9. Click **Next** and then click **Submit**.




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
request_protocol, response_state, response_reason, response_body_size, fastly_server, fastly_is_edge | additional.fields | Merged with labels created from each field if not empty  
| metadata.event_type | Set to "GENERIC_EVENT", then to "STATUS_UPDATE" if principal_mid_present is true  
request_method | network.http.method | Value copied directly  
request_user_agent | network.http.parsed_user_agent | Converted to parseduseragent then renamed  
request_referer | network.http.referral_url | Value copied directly  
response_status | network.http.response_code | Converted to string then to integer  
request_user_agent | network.http.user_agent | Value copied directly  
host | principal.asset.hostname | Value copied directly  
client_ip | principal.asset.ip | Value copied directly (after grok validation as IP)  
host | principal.hostname | Value copied directly  
client_ip | principal.ip | Value copied directly (after grok validation as IP)  
geo_city | principal.location.city | Value copied directly  
geo_country | principal.location.country_or_region | Value copied directly  
security_result | security_result | Value copied directly  
url | target.url | Value copied directly  
| metadata.product_name | Set to "FASTLY_CDN"  
| metadata.vendor_name | Set to "FASTLY_CDN"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fastly-cdn-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
