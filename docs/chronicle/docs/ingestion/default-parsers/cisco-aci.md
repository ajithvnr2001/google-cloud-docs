---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-aci/
title: Collect Cisco Application Centric Infrastructure (ACI) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:17.789717+00:00
---

# Collect Cisco Application Centric Infrastructure (ACI) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-aci/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Application Centric Infrastructure (ACI) logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Application Centric Infrastructure (ACI) logs to Google Security Operations. The parser first attempts to process incoming Cisco ACI logs as syslog messages using Grok patterns. If the syslog parsing fails, it assumes the message is in JSON format and parses it accordingly. Finally, it maps the extracted fields to the unified data model (UDM).

This integration supports two methods:

  * **Option 1** : Syslog format using Bindplane agent
  * **Option 2** : JSON format Google Cloud Storage using APIC REST API



Each option is self-contained and can be implemented independently based on your infrastructure requirements and log format preferences.

## Option 1: Syslog using Bindplane agent

This option configures Cisco ACI fabric to send syslog messages to a Bindplane agent, which forwards them to Google Security Operations for analysis.

### Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Cisco APIC console



### Get Google SecOps ingestion authentication file

  1. Go to **SIEM Settings > Collection Agents**.
  2. Download the **Ingestion Authentication File**.
  3. Save the file securely on the system where the Bindplane agent will be installed.



### Get Google SecOps customer ID

  1. Go to **SIEM Settings > Profile**.
  2. Copy and save the **Customer ID** from the **Organization Details** section.



### Install Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

#### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-otel-collector/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         

The service should show as **RUNNING**.




#### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observIQ/bindplane-otel-collector/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         

The service should show as **active (running)**.




#### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

### Configure the Bindplane agent to ingest Syslog and send to Google SecOps

#### Access the configuration file

  1. Locate the `config.yaml` file. Typically, it's in the `/etc/bindplane-agent/` directory on Linux or in the installation directory on Windows.
  2. Open the file using a text editor (for example, `nano`, `vi`, or Notepad).



#### Edit the config.yaml file

  * The `config.yaml` file
        
        receivers:
          udplog:
            # Replace the port and IP address as required
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID
            customer_id: <CUSTOMER_ID>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'CISCO_ACI'
            raw_log_field: body
            ingestion_labels:
              service:
        
        pipelines:
          logs/source0__chronicle_w_labels-0:
            receivers:
              - udplog
            exporters:
              - chronicle/chronicle_w_labels
        




#### Configuration parameters

Replace the following placeholders:

  * **`listen_address`** : Replace the port and IP address as required in your infrastructure. Use `0.0.0.0:514` to listen on all interfaces on port 514.
  * **`creds_file_path`** : Update to the path where the authentication file was saved: 
    * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
    * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
  * **`customer_id`** : Replace `YOUR_CUSTOMER_ID` with the actual customer ID from the previous step.
  * **`endpoint`** : Regional endpoint URL: 
    * **US** : `malachiteingestion-pa.googleapis.com`
    * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
    * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`



#### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
  * **Windows** : Click **File > Save**



### Restart the Bindplane agent to apply the changes

#### Linux

To restart the Bindplane agent on a Linux system, do the following:

  1. Restart the agent:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify service status:
         
         sudo systemctl status observiq-otel-collector
         

  3. Tail the agent logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




#### Windows

  * To restart the Bindplane agent in Windows, choose one of the following options:

    * Command Prompt or PowerShell as administrator:
          
          net stop observiq-otel-collector && net start observiq-otel-collector
          

    * Services console:

      1. Press `Win+R`, type `services.msc`, and press Enter.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.
      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




### Configure Syslog forwarding on Cisco ACI

#### Configure Out-of-Band Management Contract

  1. Sign in to the Cisco APIC console.
  2. Go to **Tenants > mgmt > Contracts > Filters**.
  3. Click **Create Filter**.
  4. Provide the following configuration details: 
     * **Name** : Enter `syslog-udp-514`.
     * **Entry Name** : Enter `syslog`.
     * **EtherType** : Select **IP**.
     * **IP Protocol** : Select **UDP**.
     * **Destination Port Range From** : Enter `514`.
     * **Destination Port Range To** : Enter `514`.
  5. Click **Submit**.



#### Create Management Contract

  1. Go to **Tenants > mgmt > Contracts > Standard**.
  2. Click **Create Contract**.
  3. Provide the following configuration details: 
     * **Name** : Enter `mgmt-syslog-contract`.
     * **Scope** : Select **Context**.
  4. Click **Submit**.
  5. Expand the contract and click **Subjects**.
  6. Click **Create Contract Subject**.
  7. Provide the following configuration details: 
     * **Name** : Enter `syslog-subject`.
     * **Apply Both Directions** : Check this option.
  8. Click **Submit**.
  9. Expand the subject and click **Filters**.
  10. Click **Create Filter Binding**.
  11. Select the `syslog-udp-514` filter.
  12. Click **Submit**.



#### Configure Syslog Destination Group

  1. Go to **Admin > External Data Collectors > Monitoring Destinations > Syslog**.
  2. Right-click **Syslog** and select **Create Syslog Monitoring Destination Group**.
  3. Provide the following configuration details: 
     * **Name** : Enter `Chronicle-Syslog-Group`.
     * **Admin State** : Select **Enabled**.
     * **Format** : Select **aci**.
  4. Click **Next**.
  5. In the **Create Syslog Monitoring Destination** dialog: 
     * **Name** : Enter `Chronicle-BindPlane`.
     * **Host** : Enter the IP address of your Bindplane agent server.
     * **Port** : Enter `514`.
     * **Admin State** : Select **Enabled**.
     * **Severity** : Select **information** (to capture detailed logs).
  6. Click **Submit**.



#### Configure Monitoring Policies - Fabric Monitoring

  1. Go to **Fabric > Fabric Policies > Policies > Monitoring > Common Policy**.
  2. Expand **Callhome/Smart Callhome/SNMP/Syslog/TACACS**.
  3. Right-click **Syslog** and select **Create Syslog Source**.
  4. Provide the following configuration details: 
     * **Name** : Enter `Chronicle-Fabric-Syslog`.
     * **Audit Logs** : Check to include audit events.
     * **Events** : Check to include system events.
     * **Faults** : Check to include fault events.
     * **Session Logs** : Check to include session logs.
     * **Destination Group** : Select `Chronicle-Syslog-Group`.
  5. Click **Submit**.



#### Configure Monitoring Policies - Access Monitoring

  1. Go to **Fabric > Access Policies > Policies > Monitoring > Default Policy**.
  2. Expand **Callhome/Smart Callhome/SNMP/Syslog**.
  3. Right-click **Syslog** and select **Create Syslog Source**.
  4. Provide the following configuration details: 
     * **Name** : Enter `Chronicle-Access-Syslog`.
     * **Audit Logs** : Check to include audit events.
     * **Events** : Check to include system events.
     * **Faults** : Check to include fault events.
     * **Session Logs** : Check to include session logs.
     * **Destination Group** : Select `Chronicle-Syslog-Group`.
  5. Click **Submit**.



#### Configure System Syslog Messages Policy

  1. Go to **Fabric > Fabric Policies > Policies > Monitoring > Common Policy**.
  2. Expand **Syslog Messages Policies**.
  3. Click **default**.
  4. In the **Facility Filter** section: 
     * **Facility** : Select **default**.
     * **Minimum Severity** : Change to **information**.
  5. Click **Submit**.



## Option 2: JSON using Google Cloud Storage

This option uses the APIC REST API to collect JSON-formatted events, faults, and audit logs from Cisco ACI fabric and stores them in Google Cloud Storage for Google SecOps ingestion.

### Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Cisco APIC console



### Collect Cisco ACI APIC prerequisites

#### Get APIC credentials

  1. Sign in to the Cisco APIC console using HTTPS.
  2. Go to **Admin > AAA** (on APIC 6.0+) or **Admin > Authentication > AAA** (on older releases).

**Note:** The AAA menu path changed starting in APIC 6.0(1).
  3. Create or use an existing local user with appropriate privileges.

  4. Copy and save in a secure location the following details:

     * **APIC Username** : Local user with read access to monitoring data
     * **APIC Password** : User password
     * **APIC URL** : The HTTPS URL of your APIC (for example, `https://apic.example.com`)
**Note:** The user account must have read permissions to the specific classes being queried (`faultInst`, `eventRecord`, `aaaModLR`) according to Cisco role-based access control.



### Create Google Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `cisco-aci-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




### Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

#### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `cisco-aci-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Cisco ACI logs`.
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



#### Grant IAM permissions on GCS bucket

Grant the service account (`cisco-aci-collector-sa`) write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `cisco-aci-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `cisco-aci-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



### Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `cisco-aci-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



### Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Cisco APIC REST API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `cisco-aci-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In**Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`cisco-aci-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`cisco-aci-collector-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `cisco-aci-logs` | GCS bucket name  
`GCS_PREFIX` | `cisco-aci-events` | Prefix for log files  
`STATE_KEY` | `cisco-aci-events/state.json` | State file path  
`APIC_URL` | `https://apic.example.com` | APIC HTTPS URL  
`APIC_USERNAME` | `your-apic-username` | APIC username  
`APIC_PASSWORD` | `your-apic-password` | APIC password  
`PAGE_SIZE` | `100` | Records per page  
`MAX_PAGES` | `10` | Max pages per run  
**Note:** For production environments, consider storing APIC credentials in Google Secret Manager instead of environment variables.
  10. In the **Variables & Secrets** section, scroll to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab:

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
  12. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  13. Click **Create**.

  14. Wait for the service to be created (1-2 minutes).

  15. After the service is created, the **inline code editor** will open automatically.




#### Add function code

  1. Enter **main** in the **Entry point** field.
  2. In the inline code editor, create two files:

     * First file: **main.py:**
    
    import functions_framework
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import json
    import os
    import urllib3
    from datetime import datetime, timezone, timedelta
    import logging
    
    # Configure logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Initialize HTTP client with timeouts
    http = urllib3.PoolManager(
        timeout=urllib3.Timeout(connect=5.0, read=60.0),
        retries=False,
    )
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    # Environment variables
    GCS_BUCKET = os.environ.get('GCS_BUCKET')
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'cisco-aci-events')
    STATE_KEY = os.environ.get('STATE_KEY', 'cisco-aci-events/state.json')
    APIC_URL = os.environ.get('APIC_URL')
    APIC_USERNAME = os.environ.get('APIC_USERNAME')
    APIC_PASSWORD = os.environ.get('APIC_PASSWORD')
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '100'))
    MAX_PAGES = int(os.environ.get('MAX_PAGES', '10'))
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch Cisco ACI logs and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        if not all([GCS_BUCKET, APIC_URL, APIC_USERNAME, APIC_PASSWORD]):
            logger.error('Error: Missing required environment variables')
            return
    
        try:
            # Get GCS bucket
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
    
            # Load state
            state = load_state(bucket, STATE_KEY)
    
            # Determine time window
            last_timestamp = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_timestamp')
            if not last_timestamp:
                last_timestamp = (datetime.utcnow() - timedelta(hours=1)).isoformat() + 'Z'
    
            logger.info(f"Starting Cisco ACI data collection for bucket: {GCS_BUCKET}")
    
            # Authenticate to APIC
            session_token = authenticate_apic(APIC_URL, APIC_USERNAME, APIC_PASSWORD)
            headers = {
                'Cookie': f'APIC-cookie={session_token}',
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
    
            # Data types to collect
            data_types = ['faultInst', 'eventRecord', 'aaaModLR']
            all_collected_data = []
    
            for data_type in data_types:
                logger.info(f"Collecting {data_type} data")
                collected_data = collect_aci_data(
                    APIC_URL,
                    headers,
                    data_type,
                    last_timestamp,
                    PAGE_SIZE,
                    MAX_PAGES
                )
    
                # Tag each record with its type
                for record in collected_data:
                    record['_data_type'] = data_type
    
                all_collected_data.extend(collected_data)
                logger.info(f"Collected {len(collected_data)} {data_type} records")
    
            logger.info(f"Total records collected: {len(all_collected_data)}")
    
            # Store data in GCS if any were collected
            if all_collected_data:
                timestamp_str = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
                s3_key = f"{GCS_PREFIX}/cisco_aci_events_{timestamp_str}.ndjson"
    
                # Convert to NDJSON format (one JSON object per line)
                ndjson_content = '\n'.join(json.dumps(record) for record in all_collected_data)
    
                # Upload to GCS
                blob = bucket.blob(s3_key)
                blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                    ndjson_content,
                    content_type='application/x-ndjson'
                )
    
                logger.info(f"Uploaded {len(all_collected_data)} records to gs://{GCS_BUCKET}/{s3_key}")
    
                # Update state file with latest timestamp from collected data
                latest_timestamp = get_latest_timestamp_from_records(all_collected_data)
                if not latest_timestamp:
                    latest_timestamp = datetime.utcnow().isoformat() + 'Z'
    
                update_state(bucket, STATE_KEY, latest_timestamp)
            else:
                logger.info("No new log records found.")
    
            logger.info(f"Successfully processed {len(all_collected_data)} records")
    
        except Exception as e:
            logger.error(f'Error processing logs: {str(e)}')
            raise
    
    def authenticate_apic(apic_url, username, password):
        """Authenticate to APIC and return session token"""
        login_url = f"{apic_url}/api/aaaLogin.json"
        login_data = {
            "aaaUser": {
                "attributes": {
                    "name": username,
                    "pwd": password
                }
            }
        }
    
        response = http.request(
            'POST',
            login_url,
            body=json.dumps(login_data).encode('utf-8'),
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
    
        if response.status != 200:
            raise RuntimeError(f"APIC authentication failed: {response.status} {response.data[:256]!r}")
    
        response_data = json.loads(response.data.decode('utf-8'))
        token = response_data['imdata'][0]['aaaLogin']['attributes']['token']
        logger.info("Successfully authenticated to APIC")
        return token
    
    def collect_aci_data(apic_url, headers, data_type, last_timestamp, page_size, max_pages):
        """Collect data from APIC REST API with pagination"""
        all_data = []
        page = 0
    
        while page < max_pages:
            # Build API URL with pagination and time filters
            api_url = f"{apic_url}/api/class/{data_type}.json"
            params = [
                f'page-size={page_size}',
                f'page={page}',
                f'order-by={data_type}.created|asc'
            ]
    
            # Add time filter to prevent duplicates
            if last_timestamp:
                params.append(f'query-target-filter=gt({data_type}.created,"{last_timestamp}")')
    
            full_url = f"{api_url}?{'&'.join(params)}"
    
            logger.info(f"Fetching {data_type} page {page} from APIC")
    
            # Make API request
            response = http.request('GET', full_url, headers=headers, timeout=60)
    
            if response.status != 200:
                logger.error(f"API request failed: {response.status} {response.data[:256]!r}")
                break
    
            data = json.loads(response.data.decode('utf-8'))
            records = data.get('imdata', [])
    
            if not records:
                logger.info(f"No more {data_type} records found")
                break
    
            # Extract the actual data from APIC format
            extracted_records = []
            for record in records:
                if data_type in record:
                    extracted_records.append(record[data_type])
    
            all_data.extend(extracted_records)
            page += 1
    
            # If we got less than page_size records, we've reached the end
            if len(records) < page_size:
                break
    
        return all_data
    
    def get_last_timestamp(bucket, state_key):
        """Get the last run timestamp from GCS state file"""
        try:
            blob = bucket.blob(state_key)
            if blob.exists():
                state_data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                state = json.loads(state_data)
                return [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_timestamp')
        except Exception as e:
            logger.warning(f"Error reading state file: {str(e)}")
    
        return None
    
    def get_latest_timestamp_from_records(records):
        """Get the latest timestamp from collected records to prevent missing events"""
        if not records:
            return None
    
        latest = None
        latest_time = None
    
        for record in records:
            try:
                # Handle both direct attributes and nested structure
                attrs = record.get('attributes', record)
                created = attrs.get('created')
                modTs = attrs.get('modTs')
    
                # Use created or modTs as fallback
                timestamp = created or modTs
    
                if timestamp:
                    if latest_time is None or timestamp > latest_time:
                        latest_time = timestamp
                        latest = record
            except Exception as e:
                logger.debug(f"Error parsing timestamp from record: {e}")
                continue
    
        return latest_time
    
    def update_state(bucket, state_key, timestamp):
        """Update the state file with the current timestamp"""
        try:
            state_data = {
                'last_timestamp': timestamp,
                'updated_at': datetime.utcnow().isoformat() + 'Z'
            }
            blob = bucket.blob(state_key)
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                json.dumps(state_data),
                content_type='application/json'
            )
            logger.info(f"Updated state file with timestamp: {timestamp}")
        except Exception as e:
            logger.error(f"Error updating state file: {str(e)}")
    
    def load_state(bucket, key):
        """Load state from GCS."""
        try:
            blob = bucket.blob(key)
            if blob.exists():
                state_data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                return json.loads(state_data)
        except Exception as e:
            logger.warning(f"Could not load state: {e}")
    
        return {}
    

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions. The APIC URL must be reachable from the Cloud Run function's network environment, and appropriate firewall rules must allow HTTPS (TCP/443) from the function to APIC.



### Create Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `cisco-aci-collector-15m`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `*/15 * * * *` (every 15 minutes)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`cisco-aci-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




#### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Medium volume (recommended)  
Every hour | `0 * * * *` | Standard  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
Daily | `0 0 * * *` | Historical data collection  
  
#### Test the integration

  1. In the **Cloud Scheduler** console, find your job (`cisco-aci-collector-15m`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click the following function name (`cisco-aci-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Starting Cisco ACI data collection for bucket: cisco-aci-logs
         Successfully authenticated to APIC
         Collecting faultInst data
         Collected X faultInst records
         Collecting eventRecord data
         Collected X eventRecord records
         Collecting aaaModLR data
         Collected X aaaModLR records
         Total records collected: X
         Uploaded X records to gs://cisco-aci-logs/cisco-aci-events/cisco_aci_events_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name (`cisco-aci-logs`).

  10. Navigate to the prefix folder (`cisco-aci-events/`).

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check APIC credentials in environment variables
  * **HTTP 403** : Verify APIC account has read permissions to `faultInst`, `eventRecord`, and `aaaModLR` classes
  * **Connection errors** : Verify Cloud Run function can reach APIC URL on TCP/443
  * **Missing environment variables** : Check all required variables are set



### Configure a feed in Google SecOps to ingest Cisco ACI logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Cisco ACI JSON logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Cisco Application Centric Infrastructure** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
    
    gs://cisco-aci-logs/cisco-aci-events/
    

     * **Replace** : 
       * `cisco-aci-logs`: Your GCS bucket name.
       * `cisco-aci-events`: Prefix/folder path where logs are stored.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label applied to the events from this feed.
  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




### Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (`cisco-aci-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
@timestamp | read_only_udm.metadata.event_timestamp | Value is taken from the raw log field '@timestamp' and parsed as a timestamp.  
aci_tag | read_only_udm.metadata.product_log_id | Value is taken from the raw log field 'aci_tag'.  
cisco_timestamp | - | Not mapped.  
DIP | read_only_udm.target.ip | Value is taken from the raw log field 'DIP'.  
DPort | read_only_udm.target.port | Value is taken from the raw log field 'DPort' and converted to integer.  
description | read_only_udm.security_result.description | Value is taken from the raw log field 'description'.  
fault_cause | read_only_udm.additional.fields.value.string_value | Value is taken from the raw log field 'fault_cause'. The key is set to 'Fault Cause'.  
hostname | read_only_udm.principal.hostname | Value is taken from the raw log field 'hostname'.  
lifecycle_state | read_only_udm.metadata.product_event_type | Value is taken from the raw log field 'lifecycle_state'.  
log.source.address | - | Not mapped.  
logstash.collect.host | - | Not mapped.  
logstash.collect.timestamp | read_only_udm.metadata.collected_timestamp | Value is taken from the raw log field 'logstash.collect.timestamp' and parsed as a timestamp.  
logstash.ingest.host | read_only_udm.intermediary.hostname | Value is taken from the raw log field 'logstash.ingest.host'.  
logstash.irm_environment | read_only_udm.additional.fields.value.string_value | Value is taken from the raw log field 'logstash.irm_environment'. The key is set to 'IRM_Environment'.  
logstash.irm_region | read_only_udm.additional.fields.value.string_value | Value is taken from the raw log field 'logstash.irm_region'. The key is set to 'IRM_Region'.  
logstash.irm_site | read_only_udm.additional.fields.value.string_value | Value is taken from the raw log field 'logstash.irm_site'. The key is set to 'IRM_Site'.  
logstash.process.host | read_only_udm.intermediary.hostname | Value is taken from the raw log field 'logstash.process.host'.  
message | - | Not mapped.  
message_class | - | Not mapped.  
message_code | - | Not mapped.  
message_content | - | Not mapped.  
message_dn | - | Not mapped.  
message_type | read_only_udm.metadata.product_event_type | Value is taken from the raw log field 'message_type' after removing square brackets.  
node_link | read_only_udm.principal.process.file.full_path | Value is taken from the raw log field 'node_link'.  
PktLen | read_only_udm.network.received_bytes | Value is taken from the raw log field 'PktLen' and converted to unsigned integer.  
program | - | Not mapped.  
Proto | read_only_udm.network.ip_protocol | Value is taken from the raw log field 'Proto', converted to integer, and mapped to the corresponding IP protocol name (e.g., 6 -> TCP).  
SIP | read_only_udm.principal.ip | Value is taken from the raw log field 'SIP'.  
SPort | read_only_udm.principal.port | Value is taken from the raw log field 'SPort' and converted to integer.  
syslog_facility | - | Not mapped.  
syslog_facility_code | - | Not mapped.  
syslog_host | read_only_udm.principal.ip, read_only_udm.observer.ip | Value is taken from the raw log field 'syslog_host'.  
syslog_prog | - | Not mapped.  
syslog_severity | read_only_udm.security_result.severity_details | Value is taken from the raw log field 'syslog_severity'.  
syslog_severity_code | read_only_udm.security_result.severity | Value is taken from the raw log field 'syslog_severity_code' and mapped to the corresponding severity level: 5, 6, 7 -> INFORMATIONAL; 3, 4 -> MEDIUM; 0, 1, 2 -> HIGH.  
syslog5424_pri | - | Not mapped.  
Vlan-Id | read_only_udm.principal.resource.id | Value is taken from the raw log field 'Vlan-Id'.  
- | read_only_udm.metadata.event_type | Logic: If 'SIP' or 'hostname' is present and 'Proto' is present, set to 'NETWORK_CONNECTION'. Else if 'SIP', 'hostname', or 'syslog_host' is present, set to 'STATUS_UPDATE'. Otherwise, set to 'GENERIC_EVENT'.  
- | read_only_udm.metadata.log_type | Logic: Set to 'CISCO_ACI'.  
- | read_only_udm.metadata.vendor_name | Logic: Set to 'Cisco'.  
- | read_only_udm.metadata.product_name | Logic: Set to 'ACI'.  
`principal_mac` | `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` | Mapped from changelog  
`context_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`node_number` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`code1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`code2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`pid` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`src_intf` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`VXLAN` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`VlanType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`flag` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Hitcnt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog_facility` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SMac` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`DMac` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`path` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`CName` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`i_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`i_ip` | `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`log_id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`product_event_type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`severity_action` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`session_id` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`protocol` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`message_code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`program` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog_prog` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`message_dn` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`message_class` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog_facility_code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog5424_pri` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`initial_code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logstash.ingest.timestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cisco_timestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-aci-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
