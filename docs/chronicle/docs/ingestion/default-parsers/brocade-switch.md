---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/brocade-switch/
title: Collect Brocade switch logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:58:27.134882+00:00
---

# Collect Brocade switch logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/brocade-switch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Brocade switch logs

**Parser Version:** 5.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Brocade switch logs to Google Security Operations using the Bindplane agent.

Brocade switches (Fibre Channel SAN switches) generate syslog messages for fabric events, zone changes, login/logout activity, and system events. The parser normalizes fields and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Brocade switch
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Brocade switch using SSH or Telnet



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**
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

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/brocade_switch:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: BROCADE_SWITCH
                raw_log_field: body
        
        service:
            pipelines:
                logs/brocade_switch_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/brocade_switch
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
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
           
           ```bash
           sudo systemctl status observiq-otel-collector
           ```
           

    2. Check logs for errors:
           
           ```bash
           sudo journalctl -u observiq-otel-collector -f
           ```
           

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
             




## Configure syslog export from a Brocade switch

  1. Connect to the Brocade switch using SSH or Telnet with the appropriate credentials.
  2. Run the following command to specify the **IP** address and **Port** of the syslog server (Bindplane):
         
         syslogadmin --set -ip <BINDPLANE_IP> -port 514
         

  3. Run the following command to display the configured syslog servers:
         
         syslogadmin --show -ip
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`application` | `additional.fields[].key`: "application"  
`additional.fields[].value.string_value`: | Value extracted from the `application@1588` field in the raw log when the KV_DATA field exists.  
`class` | `additional.fields[].key`: "class"  
`additional.fields[].value.string_value`: | Value extracted from the `class@1588` field in the raw log when the KV_DATA field exists.  
`domain` | `principal.administrative_domain` | Value extracted from the grok pattern matching the `domain` field.  
`Event` | `additional.fields[].key`: "event_category"  
`additional.fields[].value.string_value`: | Value extracted from the `arg0@1588` field in the raw log when the KV_DATA field exists.  
`event_id` | `metadata.product_log_id` | Value extracted from the grok pattern matching the `event_id` field.  
`event_type` | `metadata.product_event_type` | Value extracted from the grok pattern matching the `event_type` field.  
`flags` | `additional.fields[].key`: "flags"  
`additional.fields[].value.string_value`: | Value extracted from the grok pattern matching the `flags` field.  
`Info` | `metadata.description` | Value extracted from the `Info` field, parsed using grok.  
`interface` | `app_protocol_src` | Value extracted from the `interface@1588` field in the raw log when the KV_DATA field exists. Used to derive `network.application_protocol`.  
`ip` | `principal.ip` | Value extracted from the `ip` field, parsed using grok. Merged into `principal.ip` if it's not the same as the IP extracted from the `Info` field.  
`Info`, `IP Addr` | `principal.ip` | Value extracted from the `IP Addr` field within the `Info` field, parsed using grok.  
`log` | `additional.fields[].key`: "log"  
`additional.fields[].value.string_value`: | Value extracted from the `log@1588` field in the raw log when the KV_DATA field exists.  
`msg` | `metadata.description` | Value extracted from the `msg` field, parsed using grok.  
`msgid` | `additional.fields[].key`: "msgid"  
`additional.fields[].value.string_value`: | Value extracted from the `msgid@1588` field in the raw log when the KV_DATA field exists.  
`prin_host` | `principal.hostname`  
`principal.asset.hostname` | Value extracted from the grok pattern matching the `prin_host` field.  
`product_version` | `metadata.product_version` | Value extracted from the grok pattern matching the `product_version` field.  
`repeat_count` | `additional.fields[].key`: "repeat_count"  
`additional.fields[].value.string_value`: | Value extracted from the `msg` field, parsed using grok.  
`role`, `user_role` | `principal.user.attribute.roles[].name` | Value extracted from the `role@1588` or `user_role` field. If the value is "admin", it's replaced with "Admin".  
`sequence_number` | `additional.fields[].key`: "sequence_number"  
`additional.fields[].value.string_value`: | Value extracted from the grok pattern matching the `sequence_number` field.  
`severity` | `security_result.severity` | Value extracted from the `severity` field, parsed using grok. Mapped to UDM severity values (INFORMATIONAL, ERROR, CRITICAL, MEDIUM).  
`Status` | `security_result.summary` | Value extracted from the `Status` field.  
`switch_name` | `additional.fields[].key`: "switch_name"  
`additional.fields[].value.string_value`: | Value extracted from the grok pattern matching the `switch_name` field.  
`target_application` | `target.application` | Value extracted from the grok pattern matching the `target_application` field.  
`time` | `additional.fields[].key`: "time"  
`additional.fields[].value.string_value`: | Value extracted from the `time` field within the `kv_data3` field.  
`timestamp` | `metadata.event_timestamp.seconds` | Value extracted from the `timestamp` field, parsed using the date filter.  
`user` | `principal.user.userid`  
`principal.user.user_display_name` | Value extracted from the `user` or `user@1588` field, parsed using grok. Copied from `principal.hostname`. Copied from `principal.ip`. Copied from `metadata.product_event_type` or set to "STATUS_UPDATE" based on conditions. Copied from the log's `create_time.nanos`. Determined by parser logic based on the values of `has_principal`, `has_target`, `has_userid`, and `event_type`. Can be "SYSTEM_AUDIT_LOG_UNCATEGORIZED", "STATUS_UPDATE", or "GENERIC_EVENT". Hardcoded to "BROCADE_SWITCH". Hardcoded to "BROCADE". Hardcoded to "BROCADE_SWITCH". Derived from the `interface` field or set to "SSH" if the `interface` field contains "SSH".  
`CLI` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`prin_host` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/brocade-switch-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
