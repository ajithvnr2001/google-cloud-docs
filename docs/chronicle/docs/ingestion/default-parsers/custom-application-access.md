---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/custom-application-access/
title: Collect Custom Application Access logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:28:50.784982+00:00
---

# Collect Custom Application Access logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/custom-application-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Custom Application Access logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Custom Application Access logs into Google Security Operations using cloud storage or streaming ingestion methods.

Custom application access logs capture authentication events, authorization decisions, and access patterns from proprietary or custom-built applications. These logs are essential for monitoring user activity, detecting unauthorized access attempts, and maintaining compliance with security policies.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Custom application access logs in JSON, CSV, or structured text format
  * Access to one of the following: 
    * Google Cloud Storage bucket (for GCS ingestion)
    * Amazon S3 bucket (for S3 ingestion)
    * Microsoft Azure Storage Account (for Azure Blob ingestion)
    * Webhook endpoint capability (for push-based ingestion)
    * Amazon Kinesis Data Firehose (for streaming ingestion)



## Create a custom log type

The log type `CUSTOM_APPLICATION_ACCESS` does not exist as a prebuilt parser in Google SecOps. You must create a custom log type before ingesting logs.

  1. Go to **SIEM Settings > Available Log Types**.
  2. Click **Request a Log Type**.
  3. Under **Create a custom log type on your own** , enter the following details: 
     * **Vendor/Product** : Enter `Custom Application Access Logs`
     * **Log Type** : Enter `CUSTOM_APPLICATION_ACCESS`
  4. Click **Create Log Type**.

**Note:** The system automatically adds the `_CUSTOM` suffix to your log type, resulting in `CUSTOM_APPLICATION_ACCESS_CUSTOM`.
  5. Wait 10 minutes to ensure that the new log type is available in all components before creating feeds.




## Choose your ingestion method

Select the ingestion method that best fits your infrastructure:

  * **Google Cloud Storage (GCS)** : Use if your application writes logs to GCS buckets or you can export logs to GCS
  * **Amazon S3** : Use if your application writes logs to S3 buckets or you can export logs to S3
  * **Azure Blob Storage** : Use if your application writes logs to Azure Storage or you can export logs to Azure
  * **Webhook** : Use if your application can send HTTP POST requests to an external endpoint
  * **Amazon Kinesis Data Firehose** : Use if your application writes to CloudWatch Logs or you need real-time streaming



## Option 1: Ingest from Google Cloud Storage

### Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `custom-app-access-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




### Configure your application to write logs to GCS

Configure your custom application to write access logs to the GCS bucket you created. The logs should be written in one of the following formats:

  * **JSON format (recommended):**
        
        {"timestamp": "2025-01-15T10:30:00Z", "user": "john.doe@example.com", "action": "login", "result": "success", "source_ip": "203.0.113.45", "application": "custom-app", "resource": "/api/users"}
        

  * **CSV format:**
        
        timestamp,user,action,result,source_ip,application,resource
        2025-01-15T10:30:00Z,john.doe@example.com,login,success,203.0.113.45,custom-app,/api/users
        

  * **Newline-delimited JSON (NDJSON):**
        
        {"timestamp": "2025-01-15T10:30:00Z", "user": "john.doe@example.com", "action": "login", "result": "success"}
        {"timestamp": "2025-01-15T10:30:05Z", "user": "jane.smith@example.com", "action": "access", "result": "denied"}
        




### Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Custom Application Access Logs - GCS`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **CUSTOM_APPLICATION_ACCESS_CUSTOM** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



### Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs the **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant the **Storage Object Admin** role instead of **Storage Object Viewer**.



### Configure the feed in Google SecOps

  1. Return to the feed creation page (or go to **SIEM Settings > Feeds > Add New Feed**).
  2. Click **Next**.
  3. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://custom-app-access-logs/
           

**Note:** Always include the trailing slash (/) at the end of the URI. If your logs are in a subdirectory, include the path (for example, `gs://custom-app-access-logs/access-logs/`).
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed (for example, `custom_app_access`).

  4. Click **Next**.

  5. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Option 2: Ingest from Amazon S3

### Create an Amazon S3 bucket

  1. Open the **Amazon S3 console**.
  2. Click **Create Bucket**.
  3. Provide the following configuration details: 
     * **Bucket Name** : Enter a meaningful name for the bucket (for example, `custom-app-access-logs`).
     * **Region** : Select the Region where your application runs (for example, `us-east-1`).
  4. Click **Create**.



### Create an IAM user with S3 access

  1. Open the **IAM console**.
  2. Click **Users > Add user**.
  3. Enter a **user name** (for example, `chronicle-s3-reader`).
  4. Select **Programmatic access**.
  5. Click **Next: Permissions**.
  6. Choose **Attach existing policies directly**.
  7. Search for and select the **AmazonS3FullAccess** policy.
  8. Click **Next: Tags**.
  9. Click **Next: Review**.
  10. Click **Create user**.
  11. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  12. Click **Close**.



### Configure your application to write logs to S3

Configure your custom application to write access logs to the S3 bucket you created. Use the same log formats as described in the GCS section (JSON, CSV, or NDJSON).

### Configure a feed in Google SecOps to ingest logs from S3

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Custom Application Access Logs - S3`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **CUSTOM_APPLICATION_ACCESS_CUSTOM** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following input parameters:

     * **S3 URI** : Enter the bucket URI in format:
           
           s3://custom-app-access-logs/
           

**Note:** Include the trailing slash (/) at the end of the S3 URI.
     * **Source deletion option** : Select the deletion option according to your preference.

     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Access Key ID** : User access key with access to the S3 bucket.

     * **Secret Access Key** : User secret key with access to the S3 bucket.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed (for example, `custom_app_access`).

  9. Click **Next** and then click **Submit**.




## Option 3: Ingest from Azure Blob Storage

### Create Azure Storage Account

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select existing or create new  
**Storage account name** | Enter a unique name (for example, `customappaccesslogs`)  
**Region** | Select the region (for example, `East US`)  
**Performance** | Standard (recommended)  
**Redundancy** | LRS (Locally redundant storage)  
  4. Click **Review + create**.

  5. Review the overview of the account and click **Create**.

  6. Wait for the deployment to complete.




### Get Storage Account credentials

  1. Go to the **Storage Account** you just created.
  2. In the left navigation, select **Access keys** under **Security + networking**.
  3. Click **Show keys**.
  4. Copy and save the following for later use: 
     * **Storage account name** : `customappaccesslogs`
     * **Key 1** or **Key 2** : The shared access key



### Create a blob container

  1. In the same Storage Account, select **Containers** from the left navigation.
  2. Click **\+ Container**.
  3. Provide the following configuration details: 
     * **Name** : Enter `access-logs`
     * **Public access level** : Select **Private (no anonymous access)**
  4. Click **Create**.



### Configure your application to write logs to Azure Blob Storage

Configure your custom application to write access logs to the Azure Blob Storage container you created. Use the same log formats as described in the GCS section (JSON, CSV, or NDJSON).

### Configure a feed in Google SecOps to ingest logs from Azure

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Custom Application Access Logs - Azure`).
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **CUSTOM_APPLICATION_ACCESS_CUSTOM** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** : Enter the Blob Service endpoint URL with the container path:
           
           https://customappaccesslogs.blob.core.windows.net/access-logs/
           

**Note:** Include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference

     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Shared key** : Enter the shared key value (access key) you captured from the Storage Account

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed (for example, `custom_app_access`)

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Option 4: Ingest using Webhook

### Create webhook feed in Google SecOps

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Custom Application Access Logs - Webhook`).
  5. Select **Webhook** as the **Source type**.
  6. Select **CUSTOM_APPLICATION_ACCESS_CUSTOM** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** : Enter `\n` to split newline-delimited events (if sending multiple events per request).
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed (for example, `custom_app_access`).
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



### Generate and save secret key

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. Copy and save the secret key securely.

**Note:** The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.



### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is:
         
         https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate
         

  4. Save this URL for the next steps.

  5. Click **Done**.




### Create Google Cloud API key

Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud Console.

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Chronicle instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.
  6. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Chronicle Webhook API Key`).
  7. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API** (or **Chronicle API**).
  8. Click **Save**.
  9. Copy the API key value from the **API key** field at the top of the page.
  10. Save the API key securely.



### Configure your application to send logs via webhook

Configure your custom application to send HTTP POST requests to the Chronicle webhook endpoint.

  * **Construct the webhook URL:**

    1. Append the API key to the feed endpoint URL:
           
           https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=<API_KEY>
           

    2. Replace `<API_KEY>` with the API key you created.

  * **HTTP POST request format:**
        
        POST https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=<API_KEY> HTTP/1.1
        Content-Type: application/json
        x-chronicle-auth: <SECRET_KEY>
        
        {"timestamp": "2025-01-15T10:30:00Z", "user": "john.doe@example.com", "action": "login", "result": "success", "source_ip": "203.0.113.45"}
        

  * **For multiple events (newline-delimited):**
        
        POST https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=<API_KEY> HTTP/1.1
        Content-Type: application/json
        x-chronicle-auth: <SECRET_KEY>
        
        {"timestamp": "2025-01-15T10:30:00Z", "user": "john.doe@example.com", "action": "login", "result": "success"}
        {"timestamp": "2025-01-15T10:30:05Z", "user": "jane.smith@example.com", "action": "access", "result": "denied"}
        

  * **Example using curl:**
        
        curl -X POST \
          "https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=YOUR_API_KEY" \
          -H "Content-Type: application/json" \
          -H "x-chronicle-auth: YOUR_SECRET_KEY" \
          -d '{"timestamp": "2025-01-15T10:30:00Z", "user": "john.doe@example.com", "action": "login", "result": "success", "source_ip": "203.0.113.45"}'
        




## Option 5: Ingest using Amazon Kinesis Data Firehose

### Create a feed in Google SecOps

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Custom Application Access Logs - Firehose`).
  5. Select **Amazon Data Firehose** as the **Source type**.
  6. Select **CUSTOM_APPLICATION_ACCESS_CUSTOM** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** : Enter `\n` to split newline-delimited logs.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed (for example, `custom_app_access`).
  9. Click **Next**.
  10. Review the feed configuration and click **Submit**.
  11. Click **Generate Secret Key** to generate a secret key to authenticate this feed.
  12. Copy and save the secret key as you cannot view this secret again.
  13. Go to the **Details** tab.
  14. Copy the feed endpoint URL from the **Endpoint Information** field.
  15. Click **Done**.



### Create an API key for the Amazon Data Firehose feed

  1. Go to the **Google Cloud console** **Credentials** page at https://console.cloud.google.com/apis/credentials
  2. Click **Create credentials** , and then select **API key**.
  3. Click **Edit API key** to restrict the key.
  4. Under **API restrictions** , select **Restrict key**.
  5. Search for and select **Google SecOps API**.
  6. Click **Save**.
  7. Copy and save the API key.



### Construct the endpoint URL

  1. Append the API key to the feed endpoint URL in the following format:
         
         <FEED_ENDPOINT_URL>?key=<API_KEY>
         

  2. Replace the following:

     * `<FEED_ENDPOINT_URL>`: The feed endpoint URL in a previous step
     * `<API_KEY>`: The API key in a previous step

**Example:**
    
    https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...
    

  3. Save this full URL for the next step.




### Create IAM policy for Firehose

  1. In the **AWS Console** , go to **IAM > Policies > Create policy > JSON** tab.
  2. Paste the following policy JSON:
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Effect": "Allow",
                     "Action": [
                         "firehose:PutRecord",
                         "firehose:PutRecordBatch"
                     ],
                     "Resource": "arn:aws:firehose:us-east-1:123456789012:deliverystream/CustomAppAccessToChronicle"
                 }
             ]
         }
         

  3. Replace the following:

     * `us-east-1`: Your AWS region
     * `123456789012`: Your AWS account ID (12-digit number)
     * `CustomAppAccessToChronicle`: Your Firehose delivery stream name (you will create this in the next step)
  4. Name the policy `CustomAppAccessFirehoseWritePolicy`.

  5. Click **Create policy**.




### Create IAM role for CloudWatch Logs

  1. Go to **IAM > Roles > Create role**.
  2. Select **Custom trust policy** and paste:
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Effect": "Allow",
                     "Principal": {
                         "Service": "logs.us-east-1.amazonaws.com"
                     },
                     "Action": "sts:AssumeRole"
                 }
             ]
         }
         

  3. Replace `us-east-1` with your AWS region.

  4. Click **Next**.

  5. Search for and select the policy `CustomAppAccessFirehoseWritePolicy` that you created in the previous step.

  6. Click **Next**.

  7. Name the role `CloudWatchLogsToFirehoseRole`.

  8. Click **Create role**.




### Create Kinesis Data Firehose delivery stream

  1. In the **AWS Console** , go to **Kinesis > Data Firehose > Create delivery stream**.
  2. Provide the following configuration details:

     * **Source and destination:**

       * **Source** : Select **Direct PUT or other sources**
       * **Destination** : Select **HTTP endpoint**
     * **Delivery stream name:**

       * **Delivery stream name** : Enter `CustomAppAccessToChronicle`
     * **HTTP endpoint destination:**

       * **HTTP endpoint URL** : Enter the full endpoint URL you constructed earlier (feed endpoint + API key)
       * **Content encoding** : Select **GZIP** (recommended for bandwidth savings)
     * **Custom HTTP headers:**

       * Click **Add custom HTTP header**
       * **Header name** : Enter `X-Goog-Chronicle-Auth`
       * **Header value** : Enter the secret key you saved in a previous step
     * **Backup settings:**

       * **Source record backup in Amazon S3** : Select **Failed data only** (recommended)
       * **S3 bucket** : Select an existing bucket or create a new one for failed records
     * **Buffer hints:**

       * **Buffer size** : Enter `1` MiB (minimum for HTTP endpoints)
       * **Buffer interval** : Enter `60` seconds
     * **Retry duration:**

       * **Retry duration** : Enter `300` seconds (5 minutes)
  3. Click **Create delivery stream**.

  4. Wait for the delivery stream status to change to **Active** (1-2 minutes).




### Configure your application to write to CloudWatch Logs

Configure your custom application to write access logs to a CloudWatch Log Group. Then create a subscription filter to stream logs to Firehose.

  1. In the **AWS Console** , go to **CloudWatch > Logs > Log groups**.
  2. Create a new log group or select an existing one where your application writes logs.
  3. Click the **Subscription filters** tab.
  4. Click **Create > Create Amazon Kinesis Data Firehose subscription filter**.
  5. Provide the following configuration details:

     * **Destination** : Select delivery stream `CustomAppAccessToChronicle`.
     * **Grant permission** : Select role `CloudWatchLogsToFirehoseRole`.
     * **Subscription filter name** : Enter `CustomAppAccessToChronicle`.
     * **Log format** : Select **Other** (Google SecOps handles parsing).
     * **Subscription filter pattern** : Leave empty to send all events.
  6. Click **Start streaming**.

  7. Logs stream in real-time to Google SecOps through Firehose.




## Create a custom parser

After ingesting logs, you must create a custom parser to normalize the data into UDM format.

  1. Go to **SIEM Settings > Parsers**.
  2. Click **Create Parser**.
  3. Select **CUSTOM_APPLICATION_ACCESS_CUSTOM** as the **Log type**.
  4. Use the parser editor to create Grok patterns or parser extensions that map your log fields to UDM fields.

**Example parser mapping:**

Custom Log Field | UDM Field  
---|---  
`timestamp` | `metadata.event_timestamp`  
`user` | `principal.user.email_addresses`  
`action` | `security_result.action`  
`result` | `security_result.summary`  
`source_ip` | `principal.ip`  
`application` | `target.application`  
`resource` | `target.resource.name`  
  5. Test the parser with sample logs.

  6. Click **Save** to activate the parser.




For detailed parser creation instructions, see [Self-service parser options](https://docs.cloud.google.com/chronicle/docs/event-processing/self-service-parser-options).

## Verify ingestion

After configuring the feed and parser, verify that logs are being ingested:

  1. Go to **Search > UDM Search**.
  2. Run the following query:
         
         metadata.log_type = "CUSTOM_APPLICATION_ACCESS_CUSTOM"
         

  3. Verify that events appear in the search results.

  4. Check that UDM fields are populated correctly based on your parser configuration.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
| additional | Merged with labels created from service, env, msg.attachment.fileName, msg.attachment.digest, msg.attachment.key, msg.attachment.authorizeId, msg.attachment.contentType, dest.type, type, msg.sortID, msg.refID, state.reported.applications_installed, state.reported.applications_status, state.reported.ota_queue, state.reported.VICMB_Deg_Battery_LimpHome, state.reported.VICMB_Inhibit_Propulsion, state.reported.VICMB_FA_LostComm_BPCM, state.reported.VICMB_FA_LostComm_SFAM1, state.reported.VICMB_Inhibit_HV, state.reported.VICMB_FA_LostComm_RIDM, state.reported.VICMB_FA_LostComm_RWAM1, state.reported.uname, meta.reported.battery_charging_rate_kw.timestamp, state.reported.battery_charging_rate_kw, meta.reported.cell.connected.timestamp, meta.reported.cell.packet_loss.timestamp, meta.reported.cell.average_ping_ms.timestamp, meta.reported.cell.bitrate.timestamp, meta.reported.cell.download_speed_bytes_per_sec.timestamp, meta.reported.cell.signal_strength.timestamp, meta.reported.cell.signal.timestamp, state.reported.cell.connected, state.reported.cell.packet_loss, state.reported.cell.average_ping_ms, state.reported.cell.bitrate, state.reported.cell.download_speed_bytes_per_sec, state.reported.cell.signal_strength, state.reported.cell.signal  
request_time | metadata.collected_timestamp | Parsed from request_time using ISO8601 format  
msg_1, msg.body | metadata.description | Value from msg_1 if not empty, else msg.body  
user_id, src_email, otadata.1687965118.initiator | metadata.event_type | Set to "USER_UNCATEGORIZED" if any of user_id, src_email, otadata.1687965118.initiator are present, else "GENERIC_EVENT"  
otadata.1687965118.deployment_id | metadata.product_deployment_id | Value copied directly  
version | metadata.product_version | Value copied directly  
response.status | network.http.response_code | Converted to integer  
request_id | principal.resource.product_object_id | Value copied directly  
msg.attachment.url, otadata.1687965118.download_url | principal.url | Value from msg.attachment.url if not empty, else otadata.1687965118.download_url  
src_email, otadata.1687965118.initiator | principal.user.email_addresses | Value from src_email if matches email regex, else from otadata.1687965118.initiator  
user_id | principal.user.userid | Value copied directly  
level | security_result.severity | Set to "INFORMATIONAL" if level is "INFO"  
| metadata.product_name | Set to "Custom Application Access"  
| metadata.vendor_name | Set to "Custom Application Access"  
`timestamp` | `metadata.event_timestamp` | Mapped from changelog  
`level` | `additional.fields` | Mapped from changelog  
`service` | `additional.fields` | Mapped from changelog  
`env` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/custom-application-access-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
