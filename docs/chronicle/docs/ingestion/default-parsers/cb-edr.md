---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cb-edr/
title: Collect Broadcom Carbon Black EDR logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:05:43.858257+00:00
---

# Collect Broadcom Carbon Black EDR logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cb-edr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Broadcom Carbon Black EDR logs

**Parser Version:** 17.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Broadcom Carbon Black EDR logs to Google Security Operations using the Bindplane agent or Amazon S3.

Broadcom Carbon Black EDR (formerly VMware Carbon Black EDR) is an endpoint detection and response solution that provides continuous visibility into endpoint activity. It records and stores comprehensive endpoint data, enabling threat hunting, incident response, and real-time detection of advanced threats across your organization. The cb-event-forwarder component subscribes to the EDR event bus and exports events in JSON or LEEF format to external destinations including syslog servers and Amazon S3 buckets.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access (root or sudo) to the Carbon Black EDR server
  * The cb-event-forwarder component installed on your Carbon Black EDR server (see [cb-event-forwarder on GitHub](https://github.com/carbonblack/cb-event-forwarder) for installation instructions)
  * A valid access token from the [Broadcom Support Portal](https://support.broadcom.com) for downloading the cb-event-forwarder package
  * RabbitMQ credentials from the EDR server (`/etc/cb/cb.conf`) if cb-event-forwarder is installed on a separate host



## Option 1: Syslog ingestion using Bindplane agent

### Get Google SecOps credentials for the Bindplane agent

To authenticate the Bindplane agent to Google SecOps, choose one of the following methods:

  * **New deployments** : Use the Chronicle API (Option 1).
  * **Legacy deployments** : Continue using the ingestion authentication file (Option 2) until the Ingestion API is discontinued on July 20, 2027.



#### Option 1: Create a service account for the Chronicle API (recommended)

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/) and select the Google Cloud project that is linked to your Google SecOps instance.
  2. Go to **IAM & Admin > Service Accounts**.
  3. Click **Create service account**.
  4. Provide the following configuration details: 
     * **Service account name** : Enter a name for the account (for example, `bindplane-ingest`).
     * **Service account description** : Enter a description (for example, `Bindplane agent log ingestion`).
  5. Click **Create and continue**.
  6. In the **Grant this service account access to project** section, click **Select a role** and select **Chronicle Editor**.
  7. Click **Continue** , and then click **Done**.
  8. Click the service account you created, and then go to the **Keys** tab.
  9. Click **Add key > Create new key**.
  10. Select **JSON** and click **Create**. The key file is downloaded to your computer.
  11. Save the key file as `ingestion-auth.json` in the Bindplane collector directory (`/opt/observiq-otel-collector/ingestion-auth.json` on Linux or `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json` on Windows), or update `creds_file_path` in `config.yaml` to match the path where you save it.
  12. Go to **IAM & Admin > Settings** and copy the **Project number**. You'll need it for the exporter configuration.

**Note:** The JSON key is a credential. Restrict access to the file on the Bindplane host and rotate the key according to your organization's policy.

#### Option 2: Download the ingestion authentication file (legacy)

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This file authenticates the agent to the legacy Ingestion API (`malachiteingestion-pa.googleapis.com`), which Google has scheduled for end of life on July 20, 2027. Plan to move to Option 1 before that date.

### Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



### Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

#### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

#### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         




The service should show as **active (running)**.

#### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

### Configure the Bindplane agent to ingest syslog and send to Google SecOps

#### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




#### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/cb_edr:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<your-customer-id>'
            endpoint: chronicle.googleapis.com
            log_type: CB_EDR
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/cb_edr_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/cb_edr
        




#### Configuration parameters

  * Replace the following placeholders:

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: The Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



#### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/cb_edr:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<your-customer-id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CB_EDR
            raw_log_field: body
            ingestion_labels:
              env: production
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

#### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



### Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    2. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

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
             




### Configure Carbon Black EDR cb-event-forwarder for syslog output

  1. Sign in to the **Carbon Black EDR** server via SSH.
  2. Open the cb-event-forwarder configuration file:
         
         sudo nano /etc/cb/integrations/event-forwarder/cb-event-forwarder.conf
         

  3. In the `[bridge]` section, configure the following settings:
         
         [bridge]
         server_name=cbserver
         

**Note:** The `server_name` value is a label that appears in all JSON output as `cb_server`. Use a descriptive name for your EDR deployment (for example, `cbserver-prod`).
  4. If cb-event-forwarder is installed on a separate host from the EDR server, provide the RabbitMQ credentials and hostname. These values can be found in `/etc/cb/cb.conf` on the EDR server:
         
         rabbit_mq_username=cb
         rabbit_mq_password=<RABBITMQ_PASSWORD>
         cb_server_hostname=<EDR_SERVER_IP_OR_HOSTNAME>
         

**Note:** If cb-event-forwarder is installed on the same host as the EDR server, leave these fields blank to use local credentials automatically.
  5. Optionally, set the `cb_server_url` to enable deep links in forwarded events that point back to the EDR console:
         
         cb_server_url=https://<YOUR_EDR_SERVER_FQDN>
         

**Note:** If this is not set, cb-event-forwarder defaults to the FQDN of the host where it is installed. Deep links allow one-click navigation to process, binary, and sensor details in the EDR console.
  6. Configure the output type and format for syslog delivery:
         
         output_type=tcp
         output_format=json
         tcpout=<BINDPLANE_AGENT_IP>:514
         

**Note:** Valid `output_type` values for syslog delivery are `tcp`, `udp`, or `syslog`. Use `tcp` for reliable delivery. The `syslog` output type supports TLS encryption with the format `tcp+tls:<hostname>:<port>`. Set `output_format` to `json` for Google SecOps ingestion.
  7. Configure which events to forward. The following settings control event subscriptions:
         
         events_raw_sensor=0
         events_watchlist=ALL
         events_feed=ALL
         events_alert=ALL
         

**Note:** Setting `events_raw_sensor` to `ALL` generates a high volume of events and may impact EDR server performance. Forward only the event types you need. To enable raw sensor events, you must also set `DatastoreBroadcastEventTypes=True` in `/etc/cb/cb.conf` on the EDR server.
  8. Save and close the configuration file.

  9. Restart the cb-event-forwarder service:
         
         sudo systemctl restart cb-event-forwarder
         

  10. Verify the service is running:
         
         sudo systemctl status cb-event-forwarder
         

  11. Verify logs are being sent by checking the Bindplane agent logs.




For more information, see the [cb-event-forwarder repository on GitHub](https://github.com/carbonblack/cb-event-forwarder).

## Option 2: Amazon S3 ingestion

### Configure Carbon Black EDR cb-event-forwarder for S3 output

  1. Sign in to the **Carbon Black EDR** server via SSH.
  2. Open the cb-event-forwarder configuration file:
         
         sudo nano /etc/cb/integrations/event-forwarder/cb-event-forwarder.conf
         

  3. In the `[bridge]` section, configure the following settings:
         
         [bridge]
         server_name=cbserver
         

  4. If cb-event-forwarder is installed on a separate host from the EDR server, provide the RabbitMQ credentials and hostname:
         
         rabbit_mq_username=cb
         rabbit_mq_password=<RABBITMQ_PASSWORD>
         cb_server_hostname=<EDR_SERVER_IP_OR_HOSTNAME>
         

  5. Optionally, set the `cb_server_url` to enable deep links in forwarded events:
         
         cb_server_url=https://<YOUR_EDR_SERVER_FQDN>
         

  6. Configure the output type and format for S3 delivery:
         
         output_type=s3
         output_format=json
         s3out=<TEMP_DIR>:<AWS_REGION>:<S3_BUCKET_NAME>
         

**Note:** The `s3out` value uses the format `<temp-file-directory>:<region>:<bucket-name>`. The temp directory defaults to `/var/cb/data/event-forwarder`. For example: `s3out=/var/cb/data/event-forwarder:us-east-1:cb-edr-logs`.
  7. Optionally, configure additional S3 settings in the `[s3]` section:
         
         [s3]
         bundle_send_timeout=300
         upload_empty_files=false
         bundle_size_max=10485760
         

**Note:** By default, cb-event-forwarder flushes events to S3 every 300 seconds or when the temporary file reaches 10 MB. Set `upload_empty_files=false` to avoid sending empty bundles. The cb-event-forwarder uses AWS credential profiles from `$HOME/.aws/credentials`. You can specify a custom profile with `credential_profile=<profile_name>` or `credential_profile=<filepath>:<profile_name>`.
  8. Configure which events to forward:
         
         events_raw_sensor=0
         events_watchlist=ALL
         events_feed=ALL
         events_alert=ALL
         

  9. Save and close the configuration file.

  10. Restart the cb-event-forwarder service:
         
         sudo systemctl restart cb-event-forwarder
         

  11. Verify the service is running:
         
         sudo systemctl status cb-event-forwarder
         




For more information, see the [cb-event-forwarder repository on GitHub](https://github.com/carbonblack/cb-event-forwarder).

### Configure AWS S3 bucket and IAM for Google SecOps

  1. Create an **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. Save the bucket **Name** and **Region** for future reference.
  3. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**.
  5. Select the **Security credentials** tab.
  6. Click **Create Access Key** in the **Access Keys** section.
  7. Select **Third-party service** as the **Use case**.
  8. Click **Next**.
  9. Optional: Add a description tag.
  10. Click **Create access key**.
  11. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  12. Click **Done**.
  13. Select the **Permissions** tab.
  14. Click **Add permissions** in the **Permissions policies** section.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**.
  17. Search for the **AmazonS3FullAccess** policy.
  18. Select the policy.
  19. Click **Next**.
  20. Click **Add permissions**.



### Configure a feed in Google SecOps to ingest Carbon Black EDR logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name**.
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Carbon Black EDR** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields:

     * **S3 URI** : `s3://<S3_BUCKET_NAME>/`
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
`ioc_about` | `about` | Merged  
`ioc_attrs_highlights_about` | `about` | Merged  
`ioc_qs_about` | `about` | Merged  
`local_about` | `about` | Merged  
`remote_about` | `about` | Merged  
`additional_blocked_threat_category` | `additional.fields` | Merged  
`additional_cmdline` | `additional.fields` | Merged  
`additional_created_by_event_id` | `additional.fields` | Merged  
`additional_crossproc_api` | `additional.fields` | Merged  
`additional_crossproc_guid` | `additional.fields` | Merged  
`additional_crossproc_md5` | `additional.fields` | Merged  
`additional_crossproc_rep` | `additional.fields` | Merged  
`additional_crossproc_sha256` | `additional.fields` | Merged  
`additional_crossproc_target` | `additional.fields` | Merged  
`additional_data` | `additional.fields` | Merged  
`additional_device_location` | `additional.fields` | Merged  
`additional_dns_name` | `additional.fields` | Merged  
`additional_event_id` | `additional.fields` | Merged  
`additional_fileless_scriptload_cmdline_length` | `additional.fields` | Merged  
`additional_fileless_scriptload_hash` | `additional.fields` | Merged  
`additional_first_event_time` | `additional.fields` | Merged  
`additional_ioc_confidence` | `additional.fields` | Merged  
`additional_ioc_query_index` | `additional.fields` | Merged  
`additional_ioc_query_string` | `additional.fields` | Merged  
`additional_ioc_type` | `additional.fields` | Merged  
`additional_ja3` | `additional.fields` | Merged  
`additional_ja3s` | `additional.fields` | Merged  
`additional_last_event_time` | `additional.fields` | Merged  
`additional_last_update_time` | `additional.fields` | Merged  
`additional_not_blocked_threat_category` | `additional.fields` | Merged  
`additional_parent_name` | `additional.fields` | Merged  
`additional_path` | `additional.fields` | Merged  
`additional_policy_applied` | `additional.fields` | Merged  
`additional_policy_id` | `additional.fields` | Merged  
`additional_process_name` | `additional.fields` | Merged  
`additional_process_name_field` | `additional.fields` | Merged  
`additional_process_sha256` | `additional.fields` | Merged  
`additional_reason_code` | `additional.fields` | Merged  
`additional_regmod_count` | `additional.fields` | Merged  
`additional_report_id` | `additional.fields` | Merged  
`additional_run_state` | `additional.fields` | Merged  
`additional_scriptload_count` | `additional.fields` | Merged  
`additional_scriptload_rep` | `additional.fields` | Merged  
`additional_start` | `additional.fields` | Merged  
`additional_status` | `additional.fields` | Merged  
`additional_threat_cause_actor_process_pid` | `additional.fields` | Merged  
`additional_threat_cause_actor_sha256` | `additional.fields` | Merged  
`additional_threat_cause_cause_event_id` | `additional.fields` | Merged  
`additional_threat_cause_reputation` | `additional.fields` | Merged  
`additional_threat_cause_threat_category` | `additional.fields` | Merged  
`additional_threat_cause_vector` | `additional.fields` | Merged  
`additional_username` | `additional.fields` | Merged  
`additional_watchlist_id` | `additional.fields` | Merged  
`additional_watchlist_name` | `additional.fields` | Merged  
`additional_workflow_changed_by` | `additional.fields` | Merged  
`additional_workflow_comment` | `additional.fields` | Merged  
`additional_workflow_remediation` | `additional.fields` | Merged  
`additional_workflow_state` | `additional.fields` | Merged  
`alert_origin_label` | `additional.fields` | Merged  
`change_timestamp_label` | `additional.fields` | Merged  
`changed_by_label` | `additional.fields` | Merged  
`changed_by_type_label` | `additional.fields` | Merged  
`closure_reason_label` | `additional.fields` | Merged  
`comms_ip_label` | `additional.fields` | Merged  
`detection_timestamp_label` | `additional.fields` | Merged  
`index_type_label` | `additional.fields` | Merged  
`last_event_timestamp_label` | `additional.fields` | Merged  
`last_update_label` | `additional.fields` | Merged  
`parent_effective_reputation_label` | `additional.fields` | Merged  
`parent_reputation_label` | `additional.fields` | Merged  
`primary_event_id_label` | `additional.fields` | Merged  
`process_effective_reputation_label` | `additional.fields` | Merged  
`process_issuer_label` | `additional.fields` | Merged  
`process_publisher_label` | `additional.fields` | Merged  
`product_name_label` | `additional.fields` | Merged  
`search_query_label` | `additional.fields` | Merged  
`segment_id_label` | `additional.fields` | Merged  
`start_time_label` | `additional.fields` | Merged  
`status_label` | `additional.fields` | Merged  
`vendor_name_label` | `additional.fields` | Merged  
`_intermediary` | `intermediary` | Merged  
`intermediary` | `intermediary` | Merged  
`device_name` | `intermediary.asset.hostname` | Directly mapped  
`device_internal_ip` | `intermediary.asset.ip` | Merged  
`device_name` | `intermediary.hostname` | Directly mapped  
`comms_ip` | `intermediary.ip` | Merged  
`device_internal_ip` | `intermediary.ip` | Merged  
`intermediary_ip` | `intermediary.ip` | Merged  
`description` | `metadata.description` | Directly mapped  
`event_description` | `metadata.description` | Renamed/mapped  
`reason` | `metadata.description` | Directly mapped  
`action` | `metadata.product_event_type` | Directly mapped  
`type` | `metadata.product_event_type` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`cb_version` | `metadata.product_version` | Directly mapped  
`alert_url` | `metadata.url_back_to_product` | Directly mapped  
`direction` | `network.direction` | Directly mapped  
`ioc_attr.direction` | `network.direction` | Directly mapped  
`ioc_attr.protocol` | `network.ip_protocol` | Directly mapped  
`ip_protocol_out` | `network.ip_protocol` | Renamed/mapped  
`session_id` | `network.session_id` | Directly mapped  
`proxy_domain` | `observer.hostname` | Directly mapped  
`proxy_ip` | `observer.ip` | Merged  
`proxy_port` | `observer.port` | Renamed/mapped  
`device_username` | `principal.administrative_domain` | Directly mapped  
`domain` | `principal.administrative_domain` | Directly mapped  
`orgName` | `principal.administrative_domain` | Directly mapped  
`deviceInfo.deviceId` | `principal.asset.asset_id` | Directly mapped  
`device_id` | `principal.asset.asset_id` | Directly mapped  
`asset_group_label` | `principal.asset.attribute.labels` | Merged  
`device_target_value_label` | `principal.asset.attribute.labels` | Merged  
`device_uem_id_label` | `principal.asset.attribute.labels` | Merged  
`computer_name` | `principal.asset.hostname` | Directly mapped  
`dev_hostname` | `principal.asset.hostname` | Directly mapped  
`device_name` | `principal.asset.hostname` | Directly mapped  
`host` | `principal.asset.hostname` | Directly mapped  
`clientIp` | `principal.asset.ip` | Merged  
`deviceInfo.internalIpAddress` | `principal.asset.ip` | Merged  
`device_external_ip` | `principal.asset.ip` | Merged  
`device_internal_ip` | `principal.asset.ip` | Merged  
`docs.0.interface_ip` | `principal.asset.ip` | Merged  
`interface_ip` | `principal.asset.ip` | Merged  
`local_ip` | `principal.asset.ip` | Merged  
`remote_ip` | `principal.asset.ip` | Merged  
`device_location` | `principal.asset.location.name` | Directly mapped  
`deviceInfo.deviceVersion` | `principal.asset.platform_software.platform_version` | Directly mapped  
`sensor_id` | `principal.asset_id` | Directly mapped  
`deviceInfo.groupName` | `principal.group.group_display_name` | Directly mapped  
`device_group` | `principal.group.group_display_name` | Directly mapped  
`group` | `principal.group.group_display_name` | Directly mapped  
`computer_name` | `principal.hostname` | Directly mapped  
`dev_hostname` | `principal.hostname` | Directly mapped  
`device_name` | `principal.hostname` | Directly mapped  
`host` | `principal.hostname` | Directly mapped  
`clientIp` | `principal.ip` | Merged  
`deviceInfo.internalIpAddress` | `principal.ip` | Merged  
`device_external_ip` | `principal.ip` | Merged  
`device_internal_ip` | `principal.ip` | Merged  
`docs.0.interface_ip` | `principal.ip` | Merged  
`interface_ip` | `principal.ip` | Merged  
`local_ip` | `principal.ip` | Merged  
`remote_ip` | `principal.ip` | Merged  
`device_external_ip` | `principal.nat_ip` | Merged  
`normalized_device_os` | `principal.platform` | Directly mapped  
`device_os_version` | `principal.platform_version` | Directly mapped  
`local_port` | `principal.port` | Renamed/mapped  
`remote_port` | `principal.port` | Renamed/mapped  
`process_cmdline` | `principal.process.command_line` | Directly mapped  
`parent_path` | `principal.process.file.full_path` | Directly mapped  
`process_name` | `principal.process.file.full_path` | Directly mapped  
`process_path` | `principal.process.file.full_path` | Directly mapped  
`doc.process_md5` | `principal.process.file.md5` | Directly mapped  
`md5` | `principal.process.file.md5` | Directly mapped  
`parent_md5` | `principal.process.file.md5` | Directly mapped  
`process_hash.0` | `principal.process.file.md5` | Directly mapped  
`process_md5` | `principal.process.file.md5` | Directly mapped  
`doc.process_sha256` | `principal.process.file.sha256` | Directly mapped  
`process_hash.1` | `principal.process.file.sha256` | Directly mapped  
`process_sha256` | `principal.process.file.sha256` | Directly mapped  
`sha256` | `principal.process.file.sha256` | Directly mapped  
`parent_cmdline` | `principal.process.parent_process.command_line` | Directly mapped  
`parent_name` | `principal.process.parent_process.file.full_path` | Directly mapped  
`parent_path` | `principal.process.parent_process.file.full_path` | Directly mapped  
`val.parent_name` | `principal.process.parent_process.file.full_path` | Directly mapped  
`parent_hash.0` | `principal.process.parent_process.file.md5` | Directly mapped  
`parent_md5` | `principal.process.parent_process.file.md5` | Directly mapped  
`parent_hash.1` | `principal.process.parent_process.file.sha256` | Directly mapped  
`parent_sha256` | `principal.process.parent_process.file.sha256` | Directly mapped  
`doc.parent_pid` | `principal.process.parent_process.pid` | Directly mapped  
`parent_pid` | `principal.process.parent_process.pid` | Directly mapped  
`doc.parent_guid` | `principal.process.parent_process.product_specific_process_id` | Directly mapped  
`parent_guid` | `principal.process.parent_process.product_specific_process_id` | Directly mapped  
`parent_username` | `principal.process.parent_process.user.userid` | Renamed/mapped  
`doc.process_pid` | `principal.process.pid` | Directly mapped  
`parent_pid` | `principal.process.pid` | Directly mapped  
`pid` | `principal.process.pid` | Directly mapped  
`process_id` | `principal.process.pid` | Directly mapped  
`process_pid` | `principal.process.pid` | Directly mapped  
`parent_process_guid` | `principal.process.product_specific_process_id` | Directly mapped  
`process_guid` | `principal.process.product_specific_process_id` | Directly mapped  
`org_key_label` | `principal.resource.attribute.labels` | Merged  
`feed_id` | `principal.resource.id` | Directly mapped  
`feed_name` | `principal.resource.name` | Directly mapped  
`link_process` | `principal.url` | Renamed/mapped  
`process_username` | `principal.user.user_display_name` | Directly mapped  
`dev_username` | `principal.user.userid` | Renamed/mapped  
`process_username` | `principal.user.userid` | Directly mapped  
`username` | `principal.user.userid` | Directly mapped  
`_security_result` | `security_result` | Merged  
`_security_result0` | `security_result` | Merged  
`sec_result` | `security_result` | Merged  
`security_result` | `security_result` | Merged  
`security_result_attack` | `security_result` | Merged  
`sec_action` | `security_result.action` | Merged  
`policy_applied` | `security_result.action_details` | Directly mapped  
`tactic` | `security_result.attack_details.tactics` | Merged  
`category` | `security_result.category_details` | Merged  
`report_description` | `security_result.description` | Directly mapped  
`alert_notes_present_label` | `security_result.detection_fields` | Merged  
`childproc_effective_reputation_label` | `security_result.detection_fields` | Merged  
`childproc_publisher_name_label` | `security_result.detection_fields` | Merged  
`childproc_publisher_state_label` | `security_result.detection_fields` | Merged  
`childproc_rep_label` | `security_result.detection_fields` | Merged  
`detection_action` | `security_result.detection_fields` | Merged  
`detection_blocked_threat_category` | `security_result.detection_fields` | Merged  
`detection_crossproc_publisher_name` | `security_result.detection_fields` | Merged  
`detection_crossproc_publisher_state` | `security_result.detection_fields` | Merged  
`detection_event_origin` | `security_result.detection_fields` | Merged  
`detection_event_origin_proc_publisher_name` | `security_result.detection_fields` | Merged  
`detection_event_origin_proc_publisher_state` | `security_result.detection_fields` | Merged  
`detection_fileless_scriptload_cmdline` | `security_result.detection_fields` | Merged  
`detection_ioc_hit` | `security_result.detection_fields` | Merged  
`detection_ioc_id` | `security_result.detection_fields` | Merged  
`detection_not_blocked_threat_category` | `security_result.detection_fields` | Merged  
`detection_policy_name` | `security_result.detection_fields` | Merged  
`detection_report_link` | `security_result.detection_fields` | Merged  
`detection_report_name` | `security_result.detection_fields` | Merged  
`detection_run_state` | `security_result.detection_fields` | Merged  
`detection_scriptload_eff_rep` | `security_result.detection_fields` | Merged  
`detection_scriptload_publisher` | `security_result.detection_fields` | Merged  
`detection_sensor_action` | `security_result.detection_fields` | Merged  
`detection_threat_cause_actor_name` | `security_result.detection_fields` | Merged  
`detection_threat_cause_actor_sha256` | `security_result.detection_fields` | Merged  
`detection_threat_cause_threat_category` | `security_result.detection_fields` | Merged  
`determination_change_timestamp_label` | `security_result.detection_fields` | Merged  
`determination_changed_by_label` | `security_result.detection_fields` | Merged  
`determination_changed_by_type_label` | `security_result.detection_fields` | Merged  
`determination_value_label` | `security_result.detection_fields` | Merged  
`device_policy_id_label` | `security_result.detection_fields` | Merged  
`id_label` | `security_result.detection_fields` | Merged  
`is_updated_label` | `security_result.detection_fields` | Merged  
`label_alert_severity` | `security_result.detection_fields` | Merged  
`label_device_priority_field` | `security_result.detection_fields` | Merged  
`label_eff_rep` | `security_result.detection_fields` | Merged  
`label_modload_count` | `security_result.detection_fields` | Merged  
`label_modload_md5` | `security_result.detection_fields` | Merged  
`label_modload_publisher_name` | `security_result.detection_fields` | Merged  
`label_modload_publisher_state` | `security_result.detection_fields` | Merged  
`label_modload_sha256` | `security_result.detection_fields` | Merged  
`mdr_alert_label` | `security_result.detection_fields` | Merged  
`mdr_alert_notes_present_label` | `security_result.detection_fields` | Merged  
`mdr_threat_notes_present_label` | `security_result.detection_fields` | Merged  
`modload_label` | `security_result.detection_fields` | Merged  
`name_label` | `security_result.detection_fields` | Merged  
`parent_username_label` | `security_result.detection_fields` | Merged  
`process_reputation_label` | `security_result.detection_fields` | Merged  
`process_username_label` | `security_result.detection_fields` | Merged  
`reason_code_label` | `security_result.detection_fields` | Merged  
`run_state_label` | `security_result.detection_fields` | Merged  
`tags_label` | `security_result.detection_fields` | Merged  
`threat_notes_present_label` | `security_result.detection_fields` | Merged  
`workflow_status_label` | `security_result.detection_fields` | Merged  
`device_policy` | `security_result.rule_name` | Directly mapped  
`severity` | `security_result.severity` | Directly mapped  
`threat_id` | `security_result.threat_id` | Directly mapped  
`threat_cause_actor_name` | `security_result.threat_name` | Directly mapped  
`device_external_ip` | `target.asset.ip` | Merged  
`ioc_value` | `target.asset.ip` | Merged  
`local_ip` | `target.asset.ip` | Merged  
`netconn_ip` | `target.asset.ip` | Merged  
`remote_ip` | `target.asset.ip` | Merged  
`filemod_name` | `target.file.full_path` | Directly mapped  
`path` | `target.file.full_path` | Directly mapped  
`process_path` | `target.file.full_path` | Directly mapped  
`utf8_on_disk_filename` | `target.file.full_path` | Directly mapped  
`file_md5` | `target.file.md5` | Directly mapped  
`filemod_hash.0` | `target.file.md5` | Renamed/mapped  
`md5` | `target.file.md5` | Directly mapped  
`file_sha256` | `target.file.sha256` | Directly mapped  
`filemod_hash.1` | `target.file.sha256` | Renamed/mapped  
`sha256` | `target.file.sha256` | Directly mapped  
`size` | `target.file.size` | Renamed/mapped  
`group` | `target.group.group_display_name` | Directly mapped  
`domain` | `target.hostname` | Directly mapped  
`netconn_domain` | `target.hostname` | Directly mapped  
`deviceInfo.externalIpAddress` | `target.ip` | Merged  
`device_external_ip` | `target.ip` | Merged  
`ioc_value` | `target.ip` | Merged  
`local_ip` | `target.ip` | Merged  
`netconn_ip` | `target.ip` | Merged  
`remote_ip` | `target.ip` | Merged  
`normalized_device_os` | `target.platform` | Directly mapped  
`local_port` | `target.port` | Renamed/mapped  
`remote_port` | `target.port` | Renamed/mapped  
`requested_access` | `target.process.access_mask` | Renamed/mapped  
`child_command_line` | `target.process.command_line` | Directly mapped  
`childproc_cmdline` | `target.process.command_line` | Directly mapped  
`cmdline` | `target.process.command_line` | Directly mapped  
`command_line` | `target.process.command_line` | Directly mapped  
`docs.0.cmdline` | `target.process.command_line` | Directly mapped  
`process_cmdline` | `target.process.command_line` | Directly mapped  
`target_cmdline` | `target.process.command_line` | Directly mapped  
`childproc_name` | `target.process.file.full_path` | Directly mapped  
`crossproc_name` | `target.process.file.full_path` | Directly mapped  
`docs.0.path` | `target.process.file.full_path` | Directly mapped  
`modload_name` | `target.process.file.full_path` | Directly mapped  
`path` | `target.process.file.full_path` | Directly mapped  
`process_path` | `target.process.file.full_path` | Directly mapped  
`target_path` | `target.process.file.full_path` | Directly mapped  
`childproc_hash.0` | `target.process.file.md5` | Renamed/mapped  
`md5` | `target.process.file.md5` | Directly mapped  
`target_md5` | `target.process.file.md5` | Directly mapped  
`childproc_hash.1` | `target.process.file.sha256` | Renamed/mapped  
`childproc_sha256` | `target.process.file.sha256` | Directly mapped  
`sha256` | `target.process.file.sha256` | Directly mapped  
`target_sha256` | `target.process.file.sha256` | Directly mapped  
`parent_path` | `target.process.parent_process.file.full_path` | Directly mapped  
`docs.0.parent_pid` | `target.process.parent_process.pid` | Directly mapped  
`parent_pid` | `target.process.parent_process.pid` | Directly mapped  
`docs.0.parent_guid` | `target.process.parent_process.product_specific_process_id` | Directly mapped  
`child_pid` | `target.process.pid` | Directly mapped  
`childproc_pid` | `target.process.pid` | Renamed/mapped  
`docs.0.process_pid` | `target.process.pid` | Directly mapped  
`pid` | `target.process.pid` | Directly mapped  
`process_pid` | `target.process.pid` | Directly mapped  
`target_pid` | `target.process.pid` | Directly mapped  
`child_process_guid` | `target.process.product_specific_process_id` | Directly mapped  
`childproc_guid` | `target.process.product_specific_process_id` | Directly mapped  
`docs.0.process_guid` | `target.process.product_specific_process_id` | Directly mapped  
`process_guid` | `target.process.product_specific_process_id` | Directly mapped  
`target_process_guid` | `target.process.product_specific_process_id` | Directly mapped  
`path` | `target.registry.registry_key` | Directly mapped  
`path1` | `target.registry.registry_key` | Directly mapped  
`regmod_key` | `target.registry.registry_key` | Directly mapped  
`regmod_name` | `target.registry.registry_key` | Directly mapped  
`regmod_value` | `target.registry.registry_value_name` | Directly mapped  
`value_name` | `target.registry.registry_value_name` | Directly mapped  
`product_id_label` | `target.resource.attribute.labels` | Merged  
`serial_number_label` | `target.resource.attribute.labels` | Merged  
`vendor_id_label` | `target.resource.attribute.labels` | Merged  
`report_id` | `target.resource.id` | Directly mapped  
`watchlist_id` | `target.resource.id` | Directly mapped  
`external_device_friendly_name` | `target.resource.name` | Directly mapped  
`watchlist_name` | `target.resource.name` | Directly mapped  
`docs.0.link_process` | `target.url` | Directly mapped  
`loginName` | `target.user.email_addresses` | Merged  
`child_username` | `target.user.userid` | Directly mapped  
`childproc_username` | `target.user.userid` | Directly mapped  
`docs.0.username` | `target.user.userid` | Renamed/mapped  
`loginName` | `target.user.userid` | Directly mapped  
N/A | `about` | Constant: `local_about`  
N/A | `additional.fields` | Constant: `additional_data`  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `intermediary` | Constant: `_intermediary`  
N/A | `intermediary.asset.ip` | Constant: `device_internal_ip`  
N/A | `intermediary.ip` | Constant: `device_internal_ip`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `EDR`  
N/A | `metadata.vendor_name` | Constant: `Carbon Black`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `network.ip_protocol` | Constant: `TCP`  
N/A | `observer.ip` | Constant: `proxy_ip`  
N/A | `principal.asset.attribute.labels` | Constant: `device_uem_id_label`  
N/A | `principal.asset.ip` | Constant: `local_ip`  
N/A | `principal.asset.platform_software.platform` | Constant: `WINDOWS`  
N/A | `principal.ip` | Constant: `local_ip`  
N/A | `principal.nat_ip` | Constant: `device_external_ip`  
N/A | `principal.platform` | Constant: `WINDOWS`  
N/A | `principal.resource.attribute.labels` | Constant: `org_key_label`  
N/A | `principal.resource.resource_subtype` | Constant: `Feed`  
N/A | `security_result` | Constant: `security_result`  
N/A | `security_result.action` | Constant: `sec_action`  
N/A | `security_result.alert_state` | Constant: `ALERTING`  
N/A | `security_result.attack_details.tactics` | Constant: `tactic`  
N/A | `security_result.category_details` | Constant: `category`  
N/A | `security_result.detection_fields` | Constant: `process_reputation_label`  
N/A | `security_result.severity` | Constant: `LOW`  
N/A | `target.asset.ip` | Constant: `device_external_ip`  
N/A | `target.ip` | Constant: `device_external_ip`  
N/A | `target.resource.attribute.labels` | Constant: `vendor_id_label`  
N/A | `target.resource.name` | Constant: `report_id`  
N/A | `target.resource.type` | Constant: `watchlist`  
N/A | `target.user.email_addresses` | Constant: `loginName`  
`org_key` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`workflow.changed_by` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`primary_event_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`workflow.closure_reason` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`workflow.changed_by_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert_origin` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`device_username` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vendor_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`product_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tags` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`run_state` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`workflow.status` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert_notes_present` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`threat_notes_present` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`is_updated` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`device_policy_id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`mdr_alert` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`mdr_alert_notes_present` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`mdr_threat_notes_present` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`determination.changed_by` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`determination.changed_by_type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`determination.value` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`reason_code` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`device_uem_id` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`device_target_value` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`asset_group` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`device_policy` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`device_location` | `event.idm.read_only_udm.principal.asset.location.name` | Mapped from changelog  
`device_os_version` | `event.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`vendor_id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`product_id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`serial_number` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`external_device_friendly_name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`first_event_timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`policy_applied` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`device_internal_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`threat_id` | `event.idm.read_only_udm.security_result.threat_id` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`feed_id` | `event.idm.read_only_udm.principal.resource.id` | Mapped from changelog  
`intermediary_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`session_id` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`interface_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`host` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`reason` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`segment_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`index_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`search_query` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`start_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`last_update` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`watchlist_id` | `event.idm.read_only_udm.target.resource.id` | Mapped from changelog  
`watchlist_name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`group` | `event.idm.read_only_udm.target.group.group_display_name` | Mapped from changelog  
`report_id` | `event.idm.read_only_udm.target.resource.id` | Mapped from changelog  
`report_id` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`process_sha256` | `event.idm.read_only_udm.principal.process.file.sha256` | Mapped from changelog  
`alliance_data_attackframework` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alliance_updated_attackframework` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alliance_score_attackframework` | `event.idm.read_only_udm.security_result.confidence_score` | Mapped from changelog  
`alliance_link_attackframework` | `event.idm.read_only_udm.security_result.url_back_to_product` | Mapped from changelog  
`comms_ip` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cb-edr-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
