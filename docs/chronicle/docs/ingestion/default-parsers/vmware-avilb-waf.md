---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-avilb-waf/
title: Collect VMware Avi Load Balancer WAF logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:53.175123+00:00
---

# Collect VMware Avi Load Balancer WAF logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-avilb-waf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect VMware Avi Load Balancer WAF logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest VMware Avi Load Balancer WAF logs to Google Security Operations using the Bindplane agent.

VMware Avi Load Balancer (formerly Avi Networks) is an application delivery controller that generates syslog messages for WAF events, client connection logs, and virtual service activity. The parser extracts fields from syslog-formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the AVI Controller
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to VMware AVI Load Balancer



## Get Google SecOps credentials for the Bindplane agent

To authenticate the Bindplane agent to Google SecOps, choose one of the following methods:

  * **New deployments** : Use the Chronicle API (Option 1).
  * **Legacy deployments** : Continue using the ingestion authentication file (Option 2) until the Ingestion API is discontinued on July 20, 2027.



### Option 1: Create a service account for the Chronicle API (recommended)

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

### Option 2: Download the ingestion authentication file (legacy)

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This file authenticates the agent to the legacy Ingestion API (`malachiteingestion-pa.googleapis.com`), which Google has scheduled for end of life on July 20, 2027. Plan to move to Option 1 before that date.

## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** The customer ID is required for configuring the Bindplane agent exporter.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         

The service should show as **RUNNING**.




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         

The service should show as **active (running)**.




### Additional installation resources

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/vmware_avinetworks_iwaf:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: VMWARE_AVINETWORKS_IWAF
            raw_log_field: body
        
        service:
          pipelines:
            logs/vmware_avinetworks_iwaf_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/vmware_avinetworks_iwaf
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/vmware_avinetworks_iwaf:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: VMWARE_AVINETWORKS_IWAF
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

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
             




## Configure external logging for VMware AVI WAF

  1. Sign in to the **AVI Controller** web UI.
  2. Go to **Templates > Profiles > Analytics**.
  3. Create a **new** or select a pre-existing **analytics profile** to edit.
  4. In the **Edit Analytics Profile** screen, select the **Client Log** tab.
  5. Scroll to the **External Logging** section and select the **Stream Logs to an External Server** checkbox.
  6. Provide the following configuration details: 
     * **Log Streaming Protocol** : Select **UDP**.
     * **Default Port** : Enter **514**.
     * **Types of Logs to Stream** : Select **All Logs**.
     * Click the **Add** button under **Servers**.
     * **IP Address** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (for example, `514`).
  7. Click **Save**.
  8. Apply the settings to the virtual services for which you want the log data to be streamed.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`server_name` | `about.hostname` | Directly mapped  
`_field` | `additional.fields` | Merged  
`additional_field_label` | `additional.fields` | Merged  
`cacheable_label` | `additional.fields` | Merged  
`compression_label` | `additional.fields` | Merged  
`host_label` | `additional.fields` | Merged  
`http_version_label` | `additional.fields` | Merged  
`is_internal_label` | `additional.fields` | Merged  
`key` | `additional.fields` | Mapped: `"all_request_headers_pragma", "all_request_headers_accept", "all_request_headers_co...  
`match_element_label` | `additional.fields` | Merged  
`match_value_label` | `additional.fields` | Merged  
`persistent_session_id_label` | `additional.fields` | Merged  
`request_headers_label` | `additional.fields` | Merged  
`request_id_label` | `additional.fields` | Merged  
`response_content_type_label` | `additional.fields` | Merged  
`response_headers_label` | `additional.fields` | Merged  
`response_time_first_byte_label` | `additional.fields` | Merged  
`response_time_last_byte_label` | `additional.fields` | Merged  
`rule_log_msg_label` | `additional.fields` | Merged  
`rule_log_phase_label` | `additional.fields` | Merged  
`rule_log_rule_group_label` | `additional.fields` | Merged  
`rule_log_rule_id_label` | `additional.fields` | Merged  
`rule_log_rule_name_label` | `additional.fields` | Merged  
`server_connection_reused_label` | `additional.fields` | Merged  
`server_response_code_label` | `additional.fields` | Merged  
`server_response_length_label` | `additional.fields` | Merged  
`server_response_time_first_byte_label` | `additional.fields` | Merged  
`server_response_time_last_byte_label` | `additional.fields` | Merged  
`server_rtt_label` | `additional.fields` | Merged  
`server_side_redirect_uri_label` | `additional.fields` | Merged  
`server_ssl_session_id_label` | `additional.fields` | Merged  
`servers_tried_label` | `additional.fields` | Merged  
`ssl_cipher_label` | `additional.fields` | Merged  
`ssl_session_id_label` | `additional.fields` | Merged  
`ssl_version_label` | `additional.fields` | Merged  
`tag_label` | `additional.fields` | Merged  
`value_label` | `additional.fields` | Merged  
`waf_log.latency_request_header_phase_label` | `additional.fields` | Merged  
`waf_log_latency_request_body_phase_label` | `additional.fields` | Merged  
`waf_log_latency_response_body_phase_label` | `additional.fields` | Merged  
`waf_log_latency_response_header_phase_label` | `additional.fields` | Merged  
`waf_log_rules_configured_label` | `additional.fields` | Merged  
`waf_log_rules_executed_label` | `additional.fields` | Merged  
`service_engine` | `intermediary.hostname` | Directly mapped  
`intermediary_ip` | `intermediary.ip` | Merged  
`server_src_port` | `intermediary.port` | Directly mapped  
`report_timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_HTTP`, `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`log_id` | `metadata.product_log_id` | Directly mapped  
`log_id_syslog` | `metadata.product_log_id` | Directly mapped  
`http_method` | `network.http.method` | Directly mapped  
`method` | `network.http.method` | Directly mapped  
`http_user_agent` | `network.http.parsed_user_agent` | Directly mapped  
`http_referer` | `network.http.referral_url` | Directly mapped  
`referer` | `network.http.referral_url` | Directly mapped  
`http_status` | `network.http.response_code` | Directly mapped  
`response_code` | `network.http.response_code` | Directly mapped  
`http_user_agent` | `network.http.user_agent` | Directly mapped  
`user_agent` | `network.http.user_agent` | Directly mapped  
`http_bytes_received` | `network.received_bytes` | Directly mapped  
`response_length` | `network.received_bytes` | Directly mapped  
`http_bytes_sent` | `network.sent_bytes` | Directly mapped  
`request_length` | `network.sent_bytes` | Directly mapped  
`client_rtt` | `network.session_duration.seconds` | Directly mapped  
`duration` | `network.session_duration.seconds` | Directly mapped  
`server_conn_src_ip` | `observer.ip` | Merged  
`client_ip` | `principal.asset.ip` | Merged  
`source_ip` | `principal.asset.ip` | Mapped: `client_ip` → `source_ip`  
`src_ip` | `principal.asset.ip` | Merged  
`client_ip` | `principal.ip` | Merged  
`source_ip` | `principal.ip` | Mapped: `client_ip` → `source_ip`  
`src_ip` | `principal.ip` | Merged  
`client_src_port` | `principal.port` | Directly mapped  
`user` | `principal.user.userid` | Directly mapped  
`request_state` | `security_result.description` | Directly mapped  
`_field` | `security_result.detection_fields` | Merged  
`waf_status_label` | `security_result.detection_fields` | Merged  
`dest_ip` | `target.asset.ip` | Merged  
`server_ip` | `target.asset.ip` | Merged  
`vs_ip` | `target.asset.ip` | Merged  
`vs_name_syslog` | `target.hostname` | Directly mapped  
`dest_ip` | `target.ip` | Merged  
`server_ip` | `target.ip` | Merged  
`vs_ip` | `target.ip` | Merged  
`client_dest_port` | `target.port` | Renamed/mapped  
`port` | `target.port` | Directly mapped  
`server_dest_port` | `target.port` | Renamed/mapped  
`pool_label` | `target.resource.attribute.labels` | Merged  
`pool_name_label` | `target.resource.attribute.labels` | Merged  
`virtualservice_label` | `target.resource.attribute.labels` | Merged  
`redirected_uri` | `target.url` | Directly mapped  
`uri_query` | `target.url` | Directly mapped  
`url` | `target.url` | Directly mapped  
N/A | `metadata.event_type` | Constant: `NETWORK_HTTP`  
N/A | `metadata.product_name` | Constant: `AVI Load Balancer`  
N/A | `metadata.vendor_name` | Constant: `Vmware`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `network.http.parsed_user_agent` | Constant: `parseduseragent`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
