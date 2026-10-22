---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/haproxy/
title: Collect HAProxy logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:20.369021+00:00
---

# Collect HAProxy logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/haproxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect HAProxy logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest HAProxy logs to Google Security Operations using the Bindplane agent.

HAProxy is a high-availability load balancer and proxy server that generates syslog messages for HTTP requests, connection events, backend health checks, and process activity. The parser uses Grok pattern matching to extract fields from various HAProxy log formats and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the HAProxy server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to HAProxy configuration



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
          chronicle/haproxy:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: HAPROXY
            raw_log_field: body
        
        service:
          pipelines:
            logs/haproxy_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/haproxy
        




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
          chronicle/haproxy:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: HAPROXY
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
             




## Configure syslog for HAProxy

  1. Sign in to **HAProxy** using CLI.
  2. Add the **log** directive in the **global** section to the **Configuration** to forward syslog messages over **UDP**.

     * Replace `<bindplane-ip>` with the actual Bindplane agent IP address.
    
    global
        log <bindplane-ip>:514 local0
    
    defaults
        log global
    




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
accept_date_ms |  |   
actconn |  |   
backend_name |  |   
backend_queue |  |   
beconn |  |   
bytes_read | network.received_bytes | Extracted from `bytes_read` field in the log and converted to an unsigned integer.  
captured_request_headers |  |   
client_ip | principal.ip | Extracted from `client_ip` field in the log.  
client_port | principal.port | Extracted from `client_port` field in the log and converted to an integer.  
command_description | metadata.description | Extracted from `command_description` field in the log, if available. Otherwise, it's derived from other fields like `action` or `status` depending on the log message.  
datetime | metadata.event_timestamp.seconds | Extracted from `datetime` field in the log, if available. Otherwise, it's derived from the `timestamp` field in the log entry.  
description | metadata.description | Extracted from `description` field in the log, if available. Otherwise, it's derived from other fields like `command_description` or `action` depending on the log message.  
feconn |  |   
frontend_name |  |   
http_request | target.url | Extracted from `http_request` field in the log.  
http_status_code | network.http.response_code | Extracted from `http_status_code` field in the log and converted to an integer.  
http_verb | network.http.method | Extracted from `http_verb` field in the log.  
http_version | metadata.product_version | Extracted from `http_version` field in the log and formatted as `HTTP/{version}`.  
initiator | target.application | Extracted from `initiator` field in the log.  
module |  |   
msg | security_result.summary | Extracted from `msg` field in the log.  
pid | target.process.pid | Extracted from `pid` field in the log.  
process |  |   
process_name | target.application | Extracted from `process_name` field in the log.  
retries |  |   
server_name | target.hostname | Extracted from `server_name` field in the log. If empty, it defaults to the value of `syslog_server`.  
severity | security_result.severity | Mapped from `severity` field in the log. `WARNING` maps to `MEDIUM`, `ALERT` maps to `CRITICAL`, and `NOTICE` maps to `INFORMATIONAL`.  
shell |  |   
srv_queue |  |   
srvconn |  |   
status |  |   
syslog_server | target.hostname, intermediary.hostname | Extracted from `syslog_server` field in the log. Used for both target hostname (if `server_name` is empty) and intermediary hostname.  
syslog_timestamp |  |   
syslog_timestamp_1 |  |   
syslog_timestamp_2 |  |   
syslog_timestamp_4 |  |   
target_ip |  |   
time_backend_connect |  |   
time_backend_response |  |   
time_duration |  |   
time_queue |  |   
time_request |  |   
timestamp | metadata.event_timestamp.seconds | Extracted from `timestamp` field in the log and parsed for date and time information. Used as the event timestamp.  
unknown_parameters1 |  |   
unknown_parameters2 |  |   
user_name | target.user.userid | Extracted from `user_name` field in the log.  
| metadata.event_type | Set to `NETWORK_HTTP` by default. Changed to specific event types like `PROCESS_UNCATEGORIZED`, `STATUS_UPDATE`, or `USER_UNCATEGORIZED` based on the log message and parsed fields.  
| metadata.vendor_name | Set to `HAProxy Enterprise`.  
| metadata.product_name | Set to `HAProxy`.  
| network.application_protocol | Set to `HTTP` if the `message` field contains `HTTP`.  
| metadata.log_type | Set to `HAPROXY`.  
`source_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`source_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`source_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`status_code` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`bytes` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`inter_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`inter_port` | `event.idm.read_only_udm.intermediary.port` | Mapped from changelog  
`destination_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`destination_ip` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`destination_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`referer` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`user_agent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`time_stamp` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`x_forwarded_for` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`content_length` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`datetime` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/haproxy-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
