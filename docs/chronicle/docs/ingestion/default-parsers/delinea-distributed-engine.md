---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-distributed-engine/
title: Collect Delinea Distributed Engine logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:46.435539+00:00
---

# Collect Delinea Distributed Engine logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-distributed-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Delinea Distributed Engine logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Delinea Distributed Engine logs to Google Security Operations using the Bindplane agent.

Delinea Distributed Engine provides secure connectivity between the Delinea cloud platform and on-premises resources. The engine generates syslog messages in CEF format for discovery, synchronization, and operational events. The parser extracts fields and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Delinea Distributed Engine
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Delinea portal web UI



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



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

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            tcplog:
                listen_address: "0.0.0.0:5145"
        
        exporters:
            chronicle/delinea_distributed_engine:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: DELINEA_DISTRIBUTED_ENGINE
                raw_log_field: body
        
        service:
            pipelines:
                logs/delinea_distributed_engine_to_chronicle:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/delinea_distributed_engine
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `5145` is the configured syslog port (adjust as needed)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



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
             




## Configure Delinea syslog

  1. Sign in to the **Delinea portal** web UI.
  2. Go to **Admin > Application**.
  3. Click the **Edit** button.
  4. Click the **Enable Syslog/CEF Log Output** checkbox. A Syslog section is displayed.
  5. Enter the Bindplane agent IP address.
  6. Enter the Bindplane agent port number.
  7. Click the **Protocol** menu and select **TCP**.
  8. Click to select **Time Zone list to UTC Time** or **Server Time** , depending on your preference.
  9. Click the **Site** menu to select the related **Site** that Syslog/CEF will run on.
  10. (Optional) Select **Write Syslogs As Windows Events** to write audits and event subscriptions to the Windows Event log.
  11. Click **Save**.



## Configure log level for Distributed Engines

  1. Sign in to the **Delinea portal** web UI.
  2. Go to **Admin > Distributed Engine**.
  3. Click the **three dots** icon over the relevant engine and select **Show Settings**.
  4. Select the **Log Level** menu and select **Info**.
  5. Click **OK**.



## Supported Delinea Distributed Engine sample logs

  * SYSLOG (Delinea Proprietary Format)
        
        2024-09-26 21:14:27,369 [CID:] [C:] [TID:PriorityScheduler Elastic Thread @ Normal] INFO Thycotic.DE.Feature.SS.LocalAccountDiscovery.Areas.Discovery.LocalAccountConsumer - server-dummy-01: Send Local Account Results Count: 0 - (null)
        




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`ACTION` | `security_result.action` | If `ACTION_CODE` is "1", set to "ALLOW". Otherwise, if `ACTION_CODE` is not empty, set to "BLOCK". Otherwise, defaults to "UNKNOWN_ACTION" from earlier in the parser.  
`ACTION_CODE` | `security_result.action` | Used in the logic to determine `security_result.action`.  
`APP_NAME` | `network.http.user_agent` | Directly mapped.  
`BYTES_RECVD` | `network.received_bytes` | Directly mapped, converted to unsigned integer.  
`BYTES_SENT` | `network.sent_bytes` | Directly mapped, converted to unsigned integer.  
`CLOUDGENIX_HOST` | `principal.hostname` | Directly mapped if `NAME` field is empty. Used as intermediary hostname if `NAME` is present.  
`CODE` | `metadata.product_event_type` | Concatenated with `FACILITY` to form `metadata.product_event_type`. Also used to determine `metadata.event_type` (e.g., if `CODE` contains "DOWN", `metadata.event_type` is set to "STATUS_SHUTDOWN").  
`DESTINATION_ZONE_NAME` | `about.labels` | Directly mapped as a label with key "DESTINATION_ZONE_NAME".  
`DEVICE_TIME` | `metadata.event_timestamp` | Directly mapped after being parsed as a date.  
`DST_INTERFACE` | `target.hostname` | Directly mapped.  
`DST_IP` | `target.ip` | Directly mapped.  
`DST_PORT` | `target.port` | Directly mapped, converted to integer.  
`ELEMENT_ID` | `about.labels` | Directly mapped as a label with key "ELEMENT_ID".  
`EVENT_TIME` | `metadata.event_timestamp` | Directly mapped after being parsed as a date.  
`FACILITY` | `metadata.product_event_type` | Concatenated with `CODE` to form `metadata.product_event_type`.  
`FLOW_EVENT` | `security_result.summary` | Used as part of the `security_result.summary` string.  
`IDENTIFIER` | `about.labels` | Directly mapped as a label with key "IDENTIFIER".  
`ION_HOST` | `principal.hostname` | Directly mapped if `CLOUDGENIX_HOST` and `NAME` fields are empty.  
`MSG` | `metadata.description` | Directly mapped. Also used for regex matching to determine `metadata.event_type` and to extract `target.ip`.  
`NAME` | `principal.hostname` | Directly mapped. If present, `CLOUDGENIX_HOST` becomes the `intermediary.hostname`.  
`PROCESS_NAME` | `principal.process.file.full_path` | Directly mapped.  
`PROTOCOL_NAME` | `network.ip_protocol` | Directly mapped, converted to uppercase.  
`REMOTE_HOSTNAME` | `target.hostname` | Directly mapped.  
`REMOTE_IP` | `target.ip` | Directly mapped.  
`RULE_NAME` | `security_result.rule_name` | Directly mapped.  
`SEVERITY` | `security_result.severity`, `security_result.severity_details` | Mapped to `security_result.severity_details`. Also used to determine `security_result.severity` (e.g., if `SEVERITY` is "minor", `security_result.severity` is set to "LOW").  
`SOURCE_ZONE_NAME` | `about.labels` | Directly mapped as a label with key "SOURCE_ZONE_NAME".  
`SRC_INTERFACE` | `principal.hostname` | Directly mapped.  
`SRC_IP` | `principal.ip` | Directly mapped.  
`SRC_PORT` | `principal.port` | Directly mapped, converted to integer.  
`VPN_LINK_ID` | `target.resource.id` | Directly mapped.  
(Parser Logic) | `is_alert` | Set to true if `log_type` is "alert" or "alarm".  
(Parser Logic) | `is_significant` | Set to true if `log_type` is "alert" or "alarm".  
(Parser Logic) | `metadata.event_type` | Determined by a series of conditional statements based on the values of `CODE`, `MSG`, `src_ip`, and `dest_ip`. Defaults to "GENERIC_EVENT".  
(Parser Logic) | `metadata.log_type` | Set to "CLOUDGENIX_SDWAN".  
(Parser Logic) | `metadata.product_event_type` | Defaults to the concatenation of `CODE` and `FACILITY`. Set to "cgxFlowLogV1" for flow logs.  
(Parser Logic) | `metadata.product_name` | Set to "CloudGenix SD-WAN".  
(Parser Logic) | `metadata.vendor_name` | Set to "Palo Alto Networks".  
(Parser Logic) | `principal.process.pid` | Set to the value of `pid` from the raw log for flow logs.  
(Parser Logic) | `security_result.action` | Defaults to "UNKNOWN_ACTION".  
(Parser Logic) | `security_result.severity` | Defaults to "UNKNOWN_SEVERITY". Set based on the value of `SEVERITY`. Set to "INFORMATIONAL" for flow logs.  
(Parser Logic) | `security_result.summary` | Set based on the value of `CODE` for syslog messages. Set to a descriptive string including `FLOW_EVENT`, `SRC_IP`, and `DST_IP` for flow logs.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/delinea-distributed-engine-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
