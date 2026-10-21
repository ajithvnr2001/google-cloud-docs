---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nokia-router/
title: Collect Nokia Router logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:53:11.633926+00:00
---

# Collect Nokia Router logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nokia-router/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Nokia Router logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Nokia Router logs to Google Security Operations using the Bindplane agent.

Nokia Service Router is a network router that generates syslog messages for BGP events, interface status changes, MKA sessions, LLDP neighbor discovery, IS-IS routing, and security filter matches. The parser extracts fields from syslog-formatted logs using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Nokia Service Router
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Nokia Router



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
          chronicle/nokia_router:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: NOKIA_ROUTER
            raw_log_field: body
        
        service:
          pipelines:
            logs/nokia_router_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/nokia_router
        




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
          chronicle/nokia_router:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: NOKIA_ROUTER
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
             




## Configure syslog on Nokia Service Router

  1. Enter configuration mode:
         
         config# log
         

  2. Define a syslog destination:
         
         config>log# syslog 1
         

  3. Configure syslog parameters:
         
         config>log>syslog# address <syslog-server-ip>
         config>log>syslog# port <port-number>
         config>log>syslog# facility local0
         config>log>syslog# level info
         config>log>syslog# log-prefix "Nokia-SR"
         config>log>syslog# description "Syslog to Bindplane"
         

     * Replace `<syslog-server-ip>` with the Bindplane agent IP address and `<port-number>` with the appropriate port (for example, `514` for UDP).
  4. Apply the syslog destination to a log file:
         
         config>log# log-id 1
         config>log>log-id# to syslog 1
         

  5. Enable the log file:
         
         config>log>log-id# no shutdown
         

  6. Save the configuration:
         
         config>log>log-id# exit
         config>log# save
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`%{SYSLOGTIMESTAMP:date_time}` | `metadata.event_timestamp` | Extracted from the raw log and converted to a timestamp.  
`%{IP:src_ip}` | `principal.ip` | Extracted from the raw log.  
`%{HOSTNAME:host_name}` | `principal.hostname` | Extracted from the raw log.  
`%{INT:sequence_id}` | `metadata.product_log_id` | Extracted from the raw log.  
`%{DATA:router_name}` | `metadata.product_name` | Extracted from the raw log.  
`%{DATA:application}` | `target.application` | Extracted from the raw log.  
`%{WORD:severity}` | `security_result.severity` | Mapped from the raw log severity based on the following logic:  
\- CLEARED, INFO -> INFORMATIONAL  
\- MINOR -> ERROR  
\- WARNING -> LOW  
\- MAJOR -> HIGH  
\- CRITICAL -> CRITICAL  
`%{DATA:event_name}` | `metadata.product_event_type` | Extracted from the raw log.  
`%{INT:event_id}` | `additional.fields.value.string_value` | Extracted from the raw log and placed within the `additional fields` with the key `Event Id`.  
`%{GREEDYDATA:message1}` |  | Used for extracting various fields based on the `event_name`. See logic for specific fields below.  
`Group %{NOTSPACE:group_id}` | `target.group.product_object_id` | Extracted from `message1` when `event_name` is related to BGP events.  
`%{WORD} %{IP:dest_ip}` | `target.ip` | Extracted from `message1` when `event_name` is related to BGP events.  
`%{GREEDYDATA:desc}` | `security_result.description` | Extracted from `message1` for various `event_name` scenarios.  
`SAP %{DATA:sap_id}` | `additional.fields.value.string_value` | Extracted from `message1` when `event_name` is `sapStatusChanged` and placed within the `additional fields` with the key `SAP Id`.  
`in service %{INT:service_id}` | `additional.fields.value.string_value` | Extracted from `message1` when `event_name` is `sapStatusChanged` and placed within the `additional fields` with the key `Service Id`.  
`\\(customer %{INT:customer_id}\\)` | `additional.fields.value.string_value` | Extracted from `message1` when `event_name` is `sapStatusChanged` and placed within the `additional fields` with the key `Customer Id`.  
`admin=%{WORD:admin_status}` | `additional.fields.value.string_value` | Extracted from `message1` when `event_name` is `sapStatusChanged` and placed within the `additional fields` with the key `Admin Status`.  
`oper=%{WORD:operation_status}` | `additional.fields.value.string_value` | Extracted from `message1` when `event_name` is `sapStatusChanged` and placed within the `additional fields` with the key `Operation Status`.  
`flags=%{WORD:flag}` | `additional.fields.value.string_value` | Extracted from `message1` when `event_name` is `sapStatusChanged` and placed within the `additional fields` with the key `Flag`.  
`with MI:SCI %{DATA:mi_sci}` | `additional.fields.value.string_value` | Extracted from `message1` when `event_name` is `tmnxMkaSessionEstablished` and placed within the `additional fields` with the key `MI:SCI`.  
`on port %{DATA:port_id}` | `additional.fields.value.string_value` | Extracted from `message1` when `event_name` is `tmnxMkaSessionEstablished` and placed within the `additional fields` with the key `Port Id`.  
`sub-port %{INT:sub_port_id}` | `additional.fields.value.string_value` | Extracted from `message1` when `event_name` is `tmnxMkaSessionEstablished` and placed within the `additional fields` with the key `Sub-port Id`.  
`CA %{INT:ca}` | `additional.fields.value.string_value` | Extracted from `message1` when `event_name` is `tmnxMkaSessionEstablished` and placed within the `additional fields` with the key `CA`.  
`EAPOL-destination %{MAC:dest_mac}` | `target.mac` | Extracted from `message1` when `event_name` is `tmnxMkaSessionEstablished`.  
`local port-id %{DATA:local_port_id}` | `target.resource.attribute.labels.value` | Extracted from `message1` for specific `event_name` values and placed within the `target.resource.attribute.labels` with the key `local_port_id`.  
`dest-mac-type %{NOTSPACE:mac_type}` | `target.resource.attribute.labels.value` | Extracted from `message1` for specific `event_name` values and placed within the `target.resource.attribute.labels` with the key `mac_type`.  
`remote system name %{HOSTNAME:dest_host}` | `target.hostname` | Extracted from `message1` for specific `event_name` values.  
`remote chassis-id %{DATA:dest_mac}` | `target.mac` | Extracted from `message1` for specific `event_name` values.  
`remote port-id %{DATA:port_id}` | `target.resource.attribute.labels.value` | Extracted from `message1` for specific `event_name` values and placed within the `target.resource.attribute.labels` with the key `port_id`.  
`remote-index %{INT:remote_index}` | `target.resource.attribute.labels.value` | Extracted from `message1` for specific `event_name` values and placed within the `target.resource.attribute.labels` with the key `remote_index`.  
`remote management address %{IP:dest_ip}` | `target.ip` | Extracted from `message1` for specific `event_name` values.  
`advRtr:%{HOSTNAME:dest_host}%{GREEDYDATA}, ip@:%{IP:dest_ip}/%{INT:dest_port}` | `target.hostname`, `target.ip`, `target.port` | Extracted from `message1` for specific `event_name` values.  
`SID:%{INT:sid}` | `network.session_id` | Extracted from `message1` for specific `event_name` values.  
`level:%{DATA:level}` | `target.resource.attribute.labels.value` | Extracted from `message1` for specific `event_name` values and placed within the `target.resource.attribute.labels` with the key `level`.  
`mtid:%{INT:mtid}` | `target.resource.attribute.labels.value` | Extracted from `message1` for specific `event_name` values and placed within the `target.resource.attribute.labels` with the key `mtid`.  
`type:%{WORD:type}` | `target.resource.attribute.labels.value` | Extracted from `message1` for specific `event_name` values and placed within the `target.resource.attribute.labels` with the key `type`.  
`flags:%{WORD:flag}` | `target.resource.attribute.labels.value` | Extracted from `message1` for specific `event_name` values and placed within the `target.resource.attribute.labels` with the key `flag`.  
`, algo:%{INT:algo}` | `target.resource.attribute.labels.value` | Extracted from `message1` for specific `event_name` values and placed within the `target.resource.attribute.labels` with the key `algo`.  
`Description:%{GREEDYDATA:desc}.` | `security_result.description` | Extracted from `message1` when `event_name` is `mafEntryMatch`.  
`SrcIP` | `principal.ip` | Extracted from the `kv_data` field when `event_name` is `mafEntryMatch`.  
`SrcIP: %{INT:src_port}` | `principal.port` | Extracted from the `kv_data` field when `event_name` is `mafEntryMatch`.  
`DstIP` | `target.ip` | Extracted from the `kv_data` field when `event_name` is `mafEntryMatch`.  
`DstIP: %{INT:dest_port}` | `target.port` | Extracted from the `kv_data` field when `event_name` is `mafEntryMatch`.  
`Protocol` | `network.ip_protocol` | Extracted from the `kv_data` field when `event_name` is `mafEntryMatch`.  
N/A | `metadata.vendor_name` | Set to `NOKIA_ROUTER`.  
N/A | `metadata.event_type` | Determined based on the presence and combination of extracted fields:   
\- `src_ip`, `dest_ip`, and `network` present -> NETWORK_CONNECTION  
\- `principal` present -> STATUS_UPDATE  
\- Otherwise -> GENERIC_EVENT  
`%{GREEDYDATA:description}` | `metadata.description` | Extracted from `message1` when `event_name` is `tmnxMkaSessionEstablished`.  
`src_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nokia-router-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
