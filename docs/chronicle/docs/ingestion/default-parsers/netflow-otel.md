---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netflow-otel/
title: Collect OpenTelemetry Netflow Receiver logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:19.927299+00:00
---

# Collect OpenTelemetry Netflow Receiver logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netflow-otel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect OpenTelemetry Netflow Receiver logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest OpenTelemetry Netflow Receiver logs to Google Security Operations using Google Cloud Storage V2.

The OpenTelemetry Netflow Receiver is an open-source component that listens for netflow, sflow, and IPFIX UDP traffic and converts it to OpenTelemetry log records. This enables network traffic monitoring and analysis, including protocol identification, traffic volume analysis, port usage tracking, and byte/packet statistics.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Network devices capable of sending netflow, sflow, or IPFIX data
  * Access to configure network device export settings



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `netflow-logs-bucket`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `netflow-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect netflow logs`
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
  2. Click on your bucket name (for example, `netflow-logs-bucket`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `netflow-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `netflow-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect netflow logs

The Cloud Run function will run an OpenTelemetry Collector that receives netflow data and exports it to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `netflow-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic `netflow-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `netflow-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `netflow-logs-bucket` | GCS bucket name  
`GCS_PREFIX` | `netflow` | Prefix for log files  
`NETFLOW_PORT` | `2055` | Port for netflow receiver  
`NETFLOW_SCHEME` | `netflow` | Scheme type: netflow, sflow, or ipfix  
`NETFLOW_SOCKETS` | `4` | Number of UDP sockets  
`NETFLOW_WORKERS` | `8` | Number of decoder workers  
  10. In the **Variables & Secrets** section, scroll down to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes)
  11. Go to the **Settings** tab:

     * In the **Resources** section: 
       * **Memory** : Select **1 GiB** or higher
       * **CPU** : Select **2**
  12. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `1`
     * **Maximum number of instances** : Enter `10`
  13. Click **Create**.

  14. Wait for the service to be created (1-2 minutes).

  15. After the service is created, the **inline code editor** will open automatically.




### Add function code

  1. Enter **main** in the **Entry point** field.
  2. In the inline code editor, create three files:

     * **main.py:**
    
    import functions_framework
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import json
    import os
    import subprocess
    import tempfile
    import signal
    import time
    from datetime import datetime, timezone
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    # Environment variables
    GCS_BUCKET = os.environ.get('GCS_BUCKET')
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'netflow')
    NETFLOW_PORT = os.environ.get('NETFLOW_PORT', '2055')
    NETFLOW_SCHEME = os.environ.get('NETFLOW_SCHEME', 'netflow')
    NETFLOW_SOCKETS = os.environ.get('NETFLOW_SOCKETS', '4')
    NETFLOW_WORKERS = os.environ.get('NETFLOW_WORKERS', '8')
    
    # Global process handle
    collector_process = None
    
    def create_collector_config():
      """Create OpenTelemetry Collector configuration."""
      timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
      file_path = f"/tmp/netflow_{timestamp}.ndjson"
    
      config = {
        'receivers': {
          'netflow': {
            'scheme': NETFLOW_SCHEME,
            'hostname': '0.0.0.0',
            'port': int(NETFLOW_PORT),
            'sockets': int(NETFLOW_SOCKETS),
            'workers': int(NETFLOW_WORKERS),
            'queue_size': 5000
          }
        },
        'processors': {
          'batch': {
            'timeout': '10s',
            'send_batch_size': 1000
          }
        },
        'exporters': {
          'file': {
            'path': file_path,
            'format': 'json'
          }
        },
        'service': {
          'pipelines': {
            'logs': {
              'receivers': ['netflow'],
              'processors': ['batch'],
              'exporters': ['file']
            }
          },
          'telemetry': {
            'logs': {
              'level': 'info'
            }
          }
        }
      }
    
      config_path = '/tmp/otel-config.yaml'
      with open(config_path, 'w') as f:
        import yaml
        yaml.dump(config, f)
    
      return config_path, file_path
    
    def upload_to_gcs(file_path):
      """Upload netflow logs to GCS."""
      if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        print(f"No data to upload from {file_path}")
        return
    
      bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
      timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
      object_key = f"{GCS_PREFIX}/netflow_{timestamp}.ndjson"
      blob = bucket.blob(object_key)
    
      blob.[upload_from_filename](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_filename)(file_path, content_type='application/x-ndjson')
      print(f"Uploaded {os.path.getsize(file_path)} bytes to gs://{GCS_BUCKET}/{object_key}")
    
    def signal_handler(signum, frame):
      """Handle shutdown signals."""
      global collector_process
      if collector_process:
        print("Shutting down collector...")
        collector_process.[terminate](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.fileio.BlobWriter.html#google_cloud_storage_fileio_BlobWriter_terminate)()
        collector_process.wait(timeout=10)
    
    @functions_framework.cloud_event
    def main(cloud_event):
      """
      Cloud Run function to run OpenTelemetry Collector for netflow collection.
    
      Args:
        cloud_event: CloudEvent object containing Pub/Sub message
      """
      global collector_process
    
      if not GCS_BUCKET:
        print('Error: GCS_BUCKET environment variable not set')
        return
    
      try:
        # Set up signal handlers
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGINT, signal_handler)
    
        # Create collector configuration
        config_path, file_path = create_collector_config()
        print(f"Created collector config at {config_path}")
        print(f"Netflow receiver listening on {NETFLOW_SCHEME}://0.0.0.0:{NETFLOW_PORT}")
    
        # Start OpenTelemetry Collector
        collector_process = subprocess.Popen(
          ['/otelcol-contrib', '--config', config_path],
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE,
          text=True
        )
    
        print(f"Started OpenTelemetry Collector (PID: {collector_process.pid})")
    
        # Run for collection period (e.g., 5 minutes)
        collection_time = 300
        print(f"Collecting netflow data for {collection_time} seconds...")
    
        start_time = time.time()
        while time.time() - start_time < collection_time:
          if collector_process.poll() is not None:
            stdout, stderr = collector_process.communicate()
            print(f"Collector exited unexpectedly")
            print(f"STDOUT: {stdout}")
            print(f"STDERR: {stderr}")
            break
          time.sleep(10)
    
        # Stop collector
        if collector_process.poll() is None:
          print("Stopping collector...")
          collector_process.[terminate](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.fileio.BlobWriter.html#google_cloud_storage_fileio_BlobWriter_terminate)()
          collector_process.wait(timeout=10)
    
        # Upload collected data
        upload_to_gcs(file_path)
    
        # Cleanup
        if os.path.exists(file_path):
          os.remove(file_path)
        if os.path.exists(config_path):
          os.remove(config_path)
    
        print("Netflow collection completed successfully")
    
      except Exception as e:
        print(f'Error during netflow collection: {str(e)}')
        if collector_process and collector_process.poll() is None:
          collector_process.[terminate](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.fileio.BlobWriter.html#google_cloud_storage_fileio_BlobWriter_terminate)()
        raise
    

     * **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    PyYAML==6.*
    

     * **Dockerfile:**
    
    FROM python:3.12-slim
    
    # Install OpenTelemetry Collector Contrib
    RUN apt-get update && apt-get install -y wget && \
      wget https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.144.0/otelcol-contrib_0.144.0_linux_amd64.deb && \
      dpkg -i otelcol-contrib_0.144.0_linux_amd64.deb && \
      rm otelcol-contrib_0.144.0_linux_amd64.deb && \
      apt-get clean
    
    # Set working directory
    WORKDIR /app
    
    # Copy requirements and install
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Copy function code
    COPY main.py .
    
    # Expose netflow port
    EXPOSE 2055/udp
    
    # Run function
    CMD ["functions-framework", "--target=main", "--port=8080"]
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (3-5 minutes).


**Note:** The function will run an OpenTelemetry Collector that listens for netflow data and exports it to GCS.

## Configure network devices to send netflow data

Configure your network devices (routers, switches, firewalls) to export netflow, sflow, or IPFIX data to the Cloud Run function.

### Get Cloud Run function external IP

  1. In the **GCP Console** , go to **Cloud Run > Services**.
  2. Click on the function name `netflow-collector`.
  3. Copy the **URL** displayed at the top (for example, `https://netflow-collector-xxxxx-uc.a.run.app`).
  4. Extract the hostname from the URL.
  5. Use `nslookup` or `dig` to resolve the IP address:
         
         nslookup netflow-collector-xxxxx-uc.a.run.app
         


**Note:** Cloud Run services use dynamic IPs. For production deployments, consider using a Cloud Load Balancer with a static IP or deploying the collector on Compute Engine.

  * **Example: Cisco router netflow configuration**
        
        ! Configure netflow exporter
          flow exporter OTEL-EXPORTER
          destination <CLOUD_RUN_IP>
          transport udp 2055
          source <INTERFACE>
          export-protocol netflow-v9
        
          ! Configure flow monitor
          flow monitor OTEL-MONITOR
          exporter OTEL-EXPORTER
          record netflow ipv4 original-input
        
          ! Apply to interface
          interface GigabitEthernet0/0
          ip flow monitor OTEL-MONITOR input
          ip flow monitor OTEL-MONITOR output
        

  * **Example: Generic netflow configuration**

For most network devices, configure the following settings:

    * **Netflow version** : NetFlow v5, v9, or IPFIX
    * **Collector IP** : Cloud Run function IP address
    * **Collector port** : `2055` (or configured port)
    * **Protocol** : UDP
    * **Active timeout** : 60 seconds (recommended)
    * **Inactive timeout** : 15 seconds (recommended)



## Create Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `netflow-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic `netflow-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Medium volume  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
  
### Test the integration

  1. In the **Cloud Scheduler** console, find the job `netflow-collector-hourly`.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on the function name `netflow-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Started OpenTelemetry Collector (PID: ...)
         Netflow receiver listening on netflow://0.0.0.0:2055
         Collecting netflow data for 300 seconds...
         Uploaded ... bytes to gs://netflow-logs-bucket/netflow/netflow_YYYYMMDD_HHMMSS.ndjson
         Netflow collection completed successfully
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on the bucket name `netflow-logs-bucket`.

  10. Navigate to the prefix folder `netflow/`.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **Collector exited unexpectedly** : Check netflow receiver configuration
  * **No data to upload** : Verify network devices are sending netflow data to the correct IP and port
  * **Permission denied** : Check service account has Storage Object Admin role
  * **Port binding error** : Ensure port 2055 is not already in use



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `OpenTelemetry Netflow Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **NETFLOW_OTEL** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed. For example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://netflow-logs-bucket/netflow/
           

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of **Storage Object Viewer**. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on the bucket name `netflow-logs-bucket`.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of **Storage Object Viewer**.

## UDM mapping table

The following table shows how OpenTelemetry Netflow Receiver log fields map to Google SecOps UDM fields:

OpenTelemetry Field | UDM Field | Description  
---|---|---  
`source.address` | `principal.ip` | Source IP address  
`source.port` | `principal.port` | Source port number  
`destination.address` | `target.ip` | Destination IP address  
`destination.port` | `target.port` | Destination port number  
`network.transport` | `network.ip_protocol` | Transport protocol (tcp, udp)  
`network.type` | `network.ip_version` | IP version (ipv4, ipv6)  
`flow.io.bytes` | `network.sent_bytes` | Total bytes transferred  
`flow.io.packets` | `network.sent_packets` | Total packets transferred  
`flow.type` | `metadata.product_log_id` | Flow type (NETFLOW_V5, NETFLOW_V9, SFLOW_5, IPFIX)  
`flow.start` | `metadata.event_timestamp` | Flow start time  
`flow.end` | `network.session_duration` | Flow end time  
`flow.sampler_address` | `intermediary.ip` | Netflow exporter IP address  
`flow.tcp_flags` | `network.tcp_flags` | TCP flags  
`flow.io.bytes` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`source.port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`destination.port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`network.transport` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`network.type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`flow.sequence_num` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`flow.sampler_address` | `event.idm.read_only_udm.observer.ip` | Mapped from changelog  
`flow.type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netflow-otel-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
