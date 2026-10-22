---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/custom-security-data-analytics/
title: Collect Custom Security Data Analytics logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:25.468724+00:00
---

# Collect Custom Security Data Analytics logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/custom-security-data-analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Custom Security Data Analytics logs

**Parser Version:** 6.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest custom security analytics data into Google Security Operations using multiple ingestion methods. This guide is for custom security data sources that don't have a prebuilt parser or log type.

Custom security data analytics encompasses proprietary security telemetry, custom application logs, internal security tools, or any security-relevant data from sources without native Google SecOps integration. You can ingest this data as unstructured logs and optionally normalize it using custom parsers.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Custom security data source capable of exporting logs in JSON, CSV, SYSLOG, or other structured formats
  * Access to one of the following: 
    * Google Cloud Console (for API key creation and GCS)
    * AWS Console (for S3 or Firehose)
    * Azure Portal (for Azure Blob Storage)
    * HTTP client or application capable of sending webhook requests
  * Permissions to create and manage feeds in Google SecOps



## Choose your ingestion method

Google SecOps supports multiple ingestion methods for custom security data. Select the method that best fits your data source capabilities:

Ingestion Method | Use Case | Latency | Setup Complexity  
---|---|---|---  
**Webhook** | Real-time push from applications | Seconds | Low  
**Amazon S3 V2** | Batch export to S3 bucket | Minutes to hours | Medium  
**Google Cloud Storage V2** | Batch export to GCS bucket | Minutes to hours | Medium  
**Azure Blob Storage V2** | Batch export to Azure storage | Minutes to hours | Medium  
**Amazon Data Firehose** | Real-time streaming from AWS | Seconds | High  
  
## Option 1: Webhook ingestion (Real-time push)

Use this method when your custom security application can send HTTP POST requests to an external endpoint.

### Create webhook feed in Google SecOps

#### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `custom-security-analytics-webhook`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Custom Security Data Analytics** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** : Optional: Enter a delimiter to split multi-line events. Common values: 
       * `\n` \- Newline delimiter (most common for NDJSON)
       * Leave empty if each request contains a single event
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



#### Generate and save secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. **Copy and save** the secret key securely.

**Important:** The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.



#### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is:
         
         https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import
         

Where `{region}` is the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`), and `{parent}` is the resource path in the format `projects/<PROJECT_ID>/locations/<LOCATION>/instances/<INSTANCE_ID>/logTypes/<LOG_TYPE>`.

  4. Save this URL for the next steps.

  5. Click **Done**.




### Create Google Cloud API key

Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud Console.

#### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Chronicle instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



#### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Chronicle Webhook API Key`).
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Chronicle API, reducing security risk if the key is compromised.



### Configure your custom application to send data

Configure your custom security application or script to send HTTP POST requests to the Chronicle webhook endpoint.

#### Construct the webhook URL:

  * Combine the Chronicle endpoint URL and API key:
        
        <ENDPOINT_URL>?key=<API_KEY>
        

**Example:**
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...
        




#### HTTP request format:

  * **Method:** POST

  * **URL:**
        
        <ENDPOINT_URL>?key=<API_KEY>
        

  * **Headers:**
        
        Content-Type: application/json
        x-chronicle-auth: <SECRET_KEY>
        

  * **Body (single event):**
        
        {
            "timestamp": "2025-01-15T10:30:00Z",
            "event_type": "authentication",
            "user": "john.doe@example.com",
            "action": "login",
            "result": "success",
            "source_ip": "203.0.113.45",
            "custom_field_1": "value1",
            "custom_field_2": "value2"
        }
        

  * **Body (multiple events with newline delimiter):**
        
        {"timestamp": "2025-01-15T10:30:00Z", "event_type": "authentication", "action": "login"}
        {"timestamp": "2025-01-15T10:30:05Z", "event_type": "file_access", "action": "read"}
        {"timestamp": "2025-01-15T10:30:10Z", "event_type": "authentication", "action": "logout"}
        

**Note:** When sending multiple events, configure the Google SecOps feed with split delimiter `\n`.



#### Examples:

  * **Example: Python script** :
        
        import requests
        import json
        from datetime import datetime
        
        # Configuration
        ENDPOINT_URL = "https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import"
        API_KEY = "your-api-key-here"
        SECRET_KEY = "your-secret-key-here"
        
        # Construct full URL
        url = f"{ENDPOINT_URL}?key={API_KEY}"
        
        # Headers
        headers = {
            "Content-Type": "application/json",
            "x-chronicle-auth": SECRET_KEY
        }
        
        # Sample event
        event = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event_type": "custom_security_event",
            "severity": "high",
            "source": "custom_security_tool",
            "message": "Suspicious activity detected",
            "user": "admin@example.com",
            "ip_address": "192.168.1.100"
        }
        
        # Send request
        response = requests.post(url, headers=headers, data=json.dumps(event))
        
        if response.status_code == 200:
            print("Event sent successfully")
        else:
            print(f"Error: {response.status_code} - {response.text}")
        

  * **Example: cURL command** :
        
        curl -X POST \
            "https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=YOUR_API_KEY" \
            -H "Content-Type: application/json" \
            -H "x-chronicle-auth: YOUR_SECRET_KEY" \
            -d '{
                "timestamp": "2025-01-15T10:30:00Z",
                "event_type": "security_alert",
                "severity": "critical",
                "source": "custom_tool",
                "message": "Threat detected"
            }'
        




### Authentication methods reference

Google SecOps webhook feeds support multiple authentication methods. Choose the method that your application supports.

#### Method 1: Custom headers (Recommended)

If your application supports custom HTTP headers, use this method for better security.

  * **Request format:**
        
        POST <ENDPOINT_URL> HTTP/1.1
        Content-Type: application/json
        x-goog-chronicle-auth: <API_KEY>
        x-chronicle-auth: <SECRET_KEY>
        
        {
          "event": "data",
          "timestamp": "2025-01-15T10:30:00Z"
        }
        

  * **Advantages** :

    * The API key and secret are not visible in URL.
    * More secure because headers are not logged in web server access logs.
    * Preferred method when the application supports it.



#### Method 2: Query parameters

If your application does not support custom headers, append credentials to the URL.

  * **URL format:**
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

**Example:**
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...
        

  * **Request format:**
        
        POST <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY> HTTP/1.1
        Content-Type: application/json
        
        {
          "event": "data",
          "timestamp": "2025-01-15T10:30:00Z"
        }
        

  * **Disadvantages** :

    * Credentials are visible in URL.
    * Credentials may be logged in web server access logs.
    * Less secure than headers.



#### Method 3: Hybrid (URL + Header)

Some configurations use API key in URL and secret key in header.

  * **Request format:**
        
        POST <ENDPOINT_URL>?key=<API_KEY> HTTP/1.1
        Content-Type: application/json
        x-chronicle-auth: <SECRET_KEY>
        
        {
            "event": "data",
            "timestamp": "2025-01-15T10:30:00Z"
        }
        




### Webhook limits and best practices

#### Request limits

Limit | Value  
---|---  
**Max request size** | 4 MB  
**Max QPS (queries per second)** | 15,000  
**Request timeout** | 30 seconds  
**Retry behavior** | Automatic with exponential backoff  
  
#### Best practices

  * **Batch events** : Send multiple events in a single request using newline-delimited JSON (NDJSON) format to reduce overhead.
  * **Include timestamps** : Always include a timestamp field in ISO 8601 format for accurate event ordering.
  * **Use structured data** : Send data in JSON format for easier parsing and field extraction.
  * **Implement retry logic** : Handle transient failures with exponential backoff.
  * **Monitor response codes** : Log and alert on non-200 responses.



## Option 2: Amazon S3 V2 ingestion (Batch export)

Use this method when your custom security application can export logs to an Amazon S3 bucket.

### Create Amazon S3 bucket

  1. Open the **Amazon S3 console**.
  2. Click **Create Bucket**.
  3. Provide the following configuration details: 
     * **Bucket Name** : Enter a meaningful name for the bucket (for example, `custom-security-analytics-logs`).
     * **Region** : Select your preferred AWS region (for example, `us-east-1`).
  4. Click **Create**.



### Create IAM user with S3 access

  1. Open the **IAM console**.
  2. Click **Users > Add user**.
  3. Enter a **user name** (for example, `chronicle-s3-reader`).
  4. Select **Programmatic access**.
  5. Click **Next: Permissions**.
  6. Choose **Attach existing policies directly**.
  7. Search for and select **AmazonS3FullAccess**.
  8. Click **Next: Tags**.
  9. Click **Next: Review**.
  10. Click **Create user**.
  11. Click **Download .csv file** to save the **Access Key ID** and **Secret Access Key**.
  12. Click **Close**.



### Configure your application to export to S3

Configure your custom security application to write log files to the S3 bucket. The application should:

  * Write logs in a structured format (JSON, CSV, or plain text).
  * Use a consistent file naming convention.
  * Optional: Organize files by date (for example, `logs/2025/01/15/events.json`).
  * Write complete files (avoid partial writes).

  * **Example file structure:**
        
        s3://custom-security-analytics-logs/
        ├── security-events/
        │   ├── 2025/01/15/
        │   │   ├── events-10-00.json
        │   │   ├── events-11-00.json
        │   │   └── events-12-00.json
        

  * **Example log file format (NDJSON):**
        
        {"timestamp": "2025-01-15T10:00:00Z", "event_type": "login", "user": "alice@example.com", "result": "success"}
        {"timestamp": "2025-01-15T10:05:00Z", "event_type": "file_access", "user": "bob@example.com", "file": "/data/sensitive.txt"}
        {"timestamp": "2025-01-15T10:10:00Z", "event_type": "logout", "user": "alice@example.com"}
        




### Configure Google SecOps feed for S3

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `custom-security-analytics-s3`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Custom Security Data Analytics** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **S3 URI** : The bucket URI in format: `s3://custom-security-analytics-logs/security-events/`

**Note:** Include the trailing slash (/) at the end of the S3 URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Access Key ID** : Enter the access key from the IAM user.

     * **Secret Access Key** : Enter the secret key from the IAM user.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Option 3: Google Cloud Storage V2 ingestion (Batch export)

Use this method when your custom security application can export logs to a Google Cloud Storage bucket.

### Create GCS bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `custom-security-analytics-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




### Configure your application to export to GCS

Configure your custom security application to write log files to the GCS bucket using one of the following methods:

  * **Google Cloud SDK** : Use `gsutil` or client libraries
  * **Service Account** : Create a service account with Storage Object Creator role
  * **Signed URLs** : Generate signed URLs for temporary write access

  * **Example using gsutil:**
        
        gsutil cp /path/to/logs/events.json gs://custom-security-analytics-logs/security-events/
        

  * **Example using Python client library:**
        
        from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
        import json
        
        # Initialize client
        client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)('custom-security-analytics-logs')
        
        # Upload log file
        blob = bucket.blob('security-events/2025/01/15/events.json')
        
        # Write NDJSON data
        events = [
            {"timestamp": "2025-01-15T10:00:00Z", "event_type": "login"},
            {"timestamp": "2025-01-15T10:05:00Z", "event_type": "logout"}
        ]
        
        ndjson_data = '\n'.join([json.dumps(event) for event in events]) + '\n'
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson_data, content_type='application/x-ndjson')
        




### Get Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `custom-security-analytics-gcs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Custom Security Data Analytics** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.



### Grant IAM permissions

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



### Configure Google SecOps feed for GCS

  1. Continue from the feed creation page (or go to **SIEM Settings > Feeds > Add New Feed**).
  2. Click **Next**.
  3. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://custom-security-analytics-logs/security-events/
           

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  4. Click **Next**.

  5. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Option 4: Azure Blob Storage V2 ingestion (Batch export)

Use this method when your custom security application can export logs to Azure Blob Storage.

### Create Azure Storage Account

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select existing or create new  
**Storage account name** | Enter a unique name (for example, `customsecuritylogs`)  
**Region** | Select the region (for example, `East US`)  
**Performance** | Standard (recommended)  
**Redundancy** | GRS (Geo-redundant storage) or LRS (Locally redundant storage)  
  4. Click **Review + create**.

  5. Review the overview of the account and click **Create**.

  6. Wait for the deployment to complete.




### Get Storage Account credentials

  1. Go to the **Storage Account** you just created.
  2. In the left navigation, select **Access keys** under **Security + networking**.
  3. Click **Show keys**.
  4. Copy and save the following for later use: 
     * **Storage account name** : `customsecuritylogs`
     * **Key 1** or **Key 2** : The shared access key



### Create blob container

  1. In the same Storage Account, select **Containers** from the left navigation.
  2. Click **\+ Container**.
  3. Provide the following configuration details: 
     * **Name** : Enter a container name (for example, `security-events`)
     * **Public access level** : Select **Private (no anonymous access)**
  4. Click **Create**.



### Configure your application to export to Azure Blob

Configure your custom security application to write log files to the Azure Blob container using one of the following methods:

  * **Azure CLI** : Use `az storage blob upload`
  * **Azure SDK** : Use client libraries for your programming language
  * **AzCopy** : Use the AzCopy command-line tool



**Examples** :

  * **Example using Azure CLI:**
        
        az storage blob upload \
            --account-name customsecuritylogs \
            --container-name security-events \
            --name logs/2025/01/15/events.json \
            --file /path/to/events.json \
            --account-key <YOUR_ACCESS_KEY>
        

  * **Example using Python SDK:**
        
        from azure.storage.blob import BlobServiceClient
        import json
        
        # Initialize client
        connection_string = "DefaultEndpointsProtocol=https;AccountName=customsecuritylogs;AccountKey=<YOUR_KEY>;EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Get container client
        container_client = blob_service_client.get_container_client("security-events")
        
        # Upload log file
        blob_client = container_client.get_blob_client("logs/2025/01/15/events.json")
        
        # Write NDJSON data
        events = [
            {"timestamp": "2025-01-15T10:00:00Z", "event_type": "login"},
            {"timestamp": "2025-01-15T10:05:00Z", "event_type": "logout"}
        ]
        
        ndjson_data = '\n'.join([json.dumps(event) for event in events]) + '\n'
        blob_client.upload_blob(ndjson_data, overwrite=True)
        




### Configure Google SecOps feed for Azure Blob

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `custom-security-analytics-azure`).
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Custom Security Data Analytics** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** : Enter the Blob Service endpoint URL with the container path:
           
           https://customsecuritylogs.blob.core.windows.net/security-events/
           

**Note:** Include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers.
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Shared key** : Enter the shared key value (access key) from the Storage Account.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Option 5: Amazon Data Firehose ingestion (Real-time streaming)

Use this method when your custom security application writes logs to Amazon CloudWatch Logs and you need real-time streaming to Google SecOps.

### Create Google SecOps Firehose feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `custom-security-analytics-firehose`).
  4. Select **Amazon Data Firehose** as the **Source type**.
  5. Select **Custom Security Data Analytics** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **Split delimiter** : Optional: Enter `\n` to split newline-delimited logs.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  8. Click **Next**.
  9. Review the feed configuration and click **Submit**.
  10. Click **Generate Secret Key** to generate a secret key to authenticate this feed.
  11. **Copy** and **save** the secret key as you cannot view this secret again.
  12. Go to the **Details** tab.
  13. **Copy** the feed endpoint URL from the **Endpoint Information** field.
  14. Click **Done**.



### Create Google Cloud API key

  1. Go to the **Google Cloud console** **Credentials** page at https://console.cloud.google.com/apis/credentials
  2. Click **Create credentials** , and then select **API key**.
  3. Click **Edit API key** to restrict the key.
  4. Under **API restrictions** , select **Restrict key**.
  5. Search for and select **Google SecOps API**.
  6. Click **Save**.
  7. **Copy** and **save** the API key.



### Construct the endpoint URL

  1. Append the API key to the feed endpoint URL in the following format:
         
         <FEED_ENDPOINT_URL>?key=<API_KEY>
         

**Example:**
         
         https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...
         

  2. Save this full URL for the next step.




### Create IAM policy for Firehose

  1. In the **AWS Console** , go to **IAM > Policies > Create policy > JSON tab**.
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
                     "Resource": "arn:aws:firehose:<REGION>:<ACCOUNT_ID>:deliverystream/CustomSecurityToChronicle"
                 }
             ]
         }
         

  3. Replace the following:

     * `<REGION>`: Your AWS region (for example, `us-east-1`).
     * `<ACCOUNT_ID>`: Your AWS account ID (12-digit number).
  4. Name the policy `CloudWatchLogsToFirehosePolicy`.

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
                         "Service": "logs.<REGION>.amazonaws.com"
                     },
                     "Action": "sts:AssumeRole"
                 }
             ]
         }
         

  3. Replace `<REGION>` with your AWS region.

  4. Click **Next**.

  5. Search for and select the policy `CloudWatchLogsToFirehosePolicy` that you created in the previous step.

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

       * **Delivery stream name** : Enter `CustomSecurityToChronicle`
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




### Subscribe CloudWatch Log Group to Firehose

  1. In the **AWS Console** , go to **CloudWatch > Logs > Log groups**.
  2. Select the target log group that contains your custom security analytics logs.
  3. Click the **Subscription filters** tab.
  4. Click **Create > Create Amazon Kinesis Data Firehose subscription filter**.
  5. Provide the following configuration details: 
     * **Destination** : Select delivery stream `CustomSecurityToChronicle`.
     * **Grant permission** : Select role `CloudWatchLogsToFirehoseRole`.
     * **Subscription filter name** : Enter `CustomSecurityToChronicle`.
     * **Log format** : Select **Other** (Google SecOps handles parsing).
     * **Subscription filter pattern** : Leave empty to send all events, or enter a filter pattern to send only specific events.
  6. Click **Start streaming**.
  7. Logs will now stream in real-time to Google SecOps via Firehose.



## Create custom parser (optional)

After ingesting custom security data as unstructured logs, you can create a custom parser to normalize the data into UDM format for better searchability and detection.

### When to create a custom parser

Create a custom parser when:

  * You need to extract specific fields from your custom log format
  * You want to enable UDM search on your custom data
  * You need to map custom fields to standard UDM fields for detection rules
  * You want to improve search performance by indexing specific fields



### Create custom log type

  1. Go to **SIEM Settings > Available Log Types**.
  2. Click **Request a Log Type**.
  3. Under the **Create a custom log type or request a prebuilt log type** section, select **Create a custom log type**.
  4. Provide the following information: 
     * **Log type name** : Enter a descriptive name (for example, `CUSTOM_SECURITY_ANALYTICS`).
     * **Description** : Enter a description of the log type.
     * **Sample logs** : Paste 5-10 sample log entries in their raw format.
  5. Click **Submit**.
  6. The custom log type will be available in approximately 10 minutes.



### Create custom parser

  1. Go to **SIEM Settings > Parsers**.
  2. Click **Create Parser**.
  3. Select **Custom Parser**.
  4. Provide the following information: 
     * **Parser name** : Enter a descriptive name
     * **Log type** : Select your custom log type (for example, `CUSTOM_SECURITY_ANALYTICS`)
     * **Parser code** : Enter your parser configuration using Google SecOps's parser configuration language
  5. Test the parser with sample logs.
  6. Click **Submit** to activate the parser.



### Parser configuration example

  * For a custom JSON log format:
        
        {
            "timestamp": "2025-01-15T10:30:00Z",
            "event_type": "authentication",
            "user": "john.doe@example.com",
            "action": "login",
            "result": "success",
            "source_ip": "203.0.113.45"
        }
        

**Example parser configuration:**
        
        filter {
            json {
                fields {
                    timestamp: timestamp
                    event_type: event_type
                    user: user
                    action: action
                    result: result
                    source_ip: source_ip
                }
            }
        }
        
        event {
            $e.metadata.event_timestamp.seconds = parseTimestamp(timestamp, "yyyy-MM-dd'T'HH:mm:ss'Z'")
            $e.metadata.event_type = "USER_LOGIN"
            $e.principal.user.email_addresses = user
            $e.target.ip = source_ip
            $e.security_result.action = if(result == "success", "ALLOW", "BLOCK")
        }
        

For more information on creating custom parsers, see [Manage prebuilt and custom parsers](https://docs.cloud.google.com/chronicle/docs/event-processing/manage-parser-updates).




## Verify data ingestion

After you configure your feed, verify that data is being ingested successfully.

### Check feed status

  1. Go to **SIEM Settings > Feeds**.
  2. Find your feed in the list.
  3. Check the **Status** column: 
     * **Active** : Feed is running and ingesting data
     * **Error** : Feed encountered an error (click for details)
     * **Paused** : Feed is paused



### Search for ingested logs

  1. Go to **Search > Raw Log Scan**.
  2. Enter a search query to find your custom logs:
         
         metadata.log_type = "CUSTOM_SECURITY_DATA_ANALYTICS"
         

  3. Adjust the time range if needed.

  4. Click **Search**.

  5. Verify that your logs appear in the results.




### Monitor feed metrics

  1. Go to **SIEM Settings > Feeds**.
  2. Click on your feed name.
  3. Go to the **Metrics** tab.
  4. Review the following metrics: 
     * **Events ingested** : Total number of events ingested
     * **Bytes ingested** : Total data volume ingested
     * **Ingestion rate** : Events per second
     * **Errors** : Number of ingestion errors



## Troubleshooting

### Webhook ingestion issues

  * **Problem: HTTP 401 Unauthorized**

    * **Cause** : Invalid API key or secret key
    * **Solution** : Verify that the API key and secret key are correct and have not expired
  * **Problem: HTTP 403 Forbidden**

    * **Cause** : API key does not have Chronicle API permissions
    * **Solution** : Edit the API key and ensure **Chronicle API** is selected under API restrictions
  * **Problem: HTTP 400 Bad Request**

    * **Cause** : Invalid request format or payload
    * **Solution** : Verify that the Content-Type header is set to `application/json` and the payload is valid JSON



### S3/GCS/Azure Blob ingestion issues

  * **Problem: No data ingested**

    * **Cause** : Incorrect bucket URI or missing permissions
    * **Solution** : Verify the bucket URI includes the trailing slash and the service account has Storage Object Viewer role
  * **Problem: Files not deleted after ingestion**

    * **Cause** : Service account does not have delete permissions
    * **Solution** : Grant Storage Object Admin role instead of Storage Object Viewer
  * **Problem: Old files not ingested**

    * **Cause** : Maximum File Age setting excludes old files
    * **Solution** : Increase the Maximum File Age value in feed configuration



### Firehose ingestion issues

  * **Problem: Delivery stream shows errors**

    * **Cause** : Invalid endpoint URL or authentication
    * **Solution** : Verify the endpoint URL includes the API key parameter and the X-Goog-Chronicle-Auth header contains the correct secret key
  * **Problem: High data freshness metric**

    * **Cause** : Firehose is throttled or experiencing delivery failures
    * **Solution** : Check CloudWatch metrics for `ThrottledRecords` and `DeliveryToHTTP.Success` rate
  * **Problem: No logs streaming from CloudWatch**

    * **Cause** : Subscription filter not configured or IAM role missing permissions
    * **Solution** : Verify the subscription filter is active and the IAM role has `firehose:PutRecord` permissions



## UDM mapping table

Custom security data analytics logs are ingested as unstructured data. To enable UDM field mapping, create a custom parser as described in the "Create custom parser" section above.

After creating a custom parser, UDM fields will be populated based on your parser configuration. Common UDM fields for security analytics data include:

UDM Field | Description  
---|---  
`metadata.event_timestamp` | Event timestamp  
`metadata.event_type` | Event type (for example, USER_LOGIN, FILE_ACCESS)  
`principal.user.email_addresses` | User email address  
`principal.ip` | Source IP address  
`target.resource.name` | Target resource name  
`security_result.action` | Security action (ALLOW, BLOCK, etc.)  
`security_result.severity` | Event severity  
  
For a complete list of UDM fields, see the [UDM field reference](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list).

## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/custom-security-data-analytics-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
