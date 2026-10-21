---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/opnsense/
title: Collect OPNsense firewall logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:18:05.438478+00:00
---

# Collect OPNsense firewall logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/opnsense/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect OPNsense firewall logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest OPNsense firewall logs to Google Security Operations using the Bindplane agent.

OPNsense is an open-source firewall and routing platform that generates syslog messages for firewall rule matches, network connections, and system events. The parser extracts fields from CSV-formatted filterlog messages using grok and CSV parsing and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the OPNsense firewall
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the OPNsense web interface



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.

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
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/opnsense:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: OPNSENSE
                raw_log_field: body
        
        service:
            pipelines:
                logs/opnsense_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/opnsense
        




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
             




## Add syslog server configuration to OPNsense

  1. Sign in to the **OPNsense** web interface.
  2. Go to **System > Settings > Logging**.
  3. In the **Remote Logging** section, enable **Send logs to remote syslog server** by checking the box.
  4. In the **Remote Syslog Servers** field, enter the IP address of the syslog server, including the port (for example, `10.10.10.10:514`).
  5. Select **Local0** as the syslog facility.
  6. Set syslog level as **Alert**.
  7. Click **Save** to apply the changes.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`column1` | `security_result.rule_id` | Directly mapped from `column1`.  
`column10` | `additional.fields[].key`: "tos"  
`additional.fields[].value.string_value`: Value of `column10` | Directly mapped from `column10`, nested under `additional.fields` with key "tos".  
`column12` | `additional.fields[].key`: "ttl"  
`additional.fields[].value.string_value`: Value of `column12` | Directly mapped from `column12`, nested under `additional.fields` with key "ttl".  
`column13` | `additional.fields[].key`: "Id"  
`additional.fields[].value.string_value`: Value of `column13` | Directly mapped from `column13`, nested under `additional.fields` with key "Id".  
`column14` | `additional.fields[].key`: "offset"  
`additional.fields[].value.string_value`: Value of `column14` | Directly mapped from `column14`, nested under `additional.fields` with key "offset".  
`column15` | `additional.fields[].key`: "flags"  
`additional.fields[].value.string_value`: Value of `column15` | Directly mapped from `column15`, nested under `additional.fields` with key "flags".  
`column17` | `network.ip_protocol` | Directly mapped from `column17` after converting to uppercase.  
`column18` | `network.received_bytes` | Directly mapped from `column18` after converting to unsigned integer.  
`column19` | `principal.ip` | Directly mapped from `column19`.  
`column20` | `target.ip` | Directly mapped from `column20`.  
`column21` | `principal.port` (if `column17` is TCP or UDP)  
`additional.fields[].key`: "data_length"  
`additional.fields[].value.string_value`: Extracted value (if `column17` is ICMP, GRE, ESP, or IGMP) | If `column17` is TCP/UDP, directly mapped from `column21` and converted to integer. Otherwise, the "datalength" value is extracted using grok and placed in `additional.fields` with key "data_length".  
`column22` | `target.port` | Directly mapped from `column22` if `column17` is TCP or UDP, and converted to integer.  
`column24` | `additional.fields[].key`: "tcp_flags"  
`additional.fields[].value.string_value`: Value of `column24` | Directly mapped from `column24` if `column17` is TCP, nested under `additional.fields` with key "tcp_flags".  
`column29` | `additional.fields[].key`: "tcp_options"  
`additional.fields[].value.string_value`: Value of `column29` | Directly mapped from `column29` if `column17` is TCP, nested under `additional.fields` with key "tcp_options".  
`column4` | `additional.fields[].key`: "tracker"  
`additional.fields[].value.string_value`: Value of `column4` | Directly mapped from `column4`, nested under `additional.fields` with key "tracker".  
`column5` | `additional.fields[].key`: "interface"  
`additional.fields[].value.string_value`: Value of `column5` | Directly mapped from `column5`, nested under `additional.fields` with key "interface".  
`column6` | `security_result.rule_type` | Directly mapped from `column6`.  
`column7` | `security_result.action` | Mapped from `column7`. If "block", converted to uppercase "BLOCK". If "pass", set to "ALLOW".  
`column8` | `network.direction` | Mapped from `column8`. If "in", set to "INBOUND". If "out", set to "OUTBOUND".  
`domain` | `principal.administrative_domain` | Directly mapped from the grok-extracted `domain`. Set to "NETWORK_CONNECTION" if both principal and target IP addresses are present, otherwise "GENERIC_EVENT". Hardcoded to "OPNSENSE". Hardcoded to "OPNSENSE".  
`message` | Various fields | Parsed using grok and csv filters to extract various fields. See other rows for specific mappings.  
`ts` | `metadata.event_timestamp.seconds`, `timestamp.seconds` | Parsed from the message field using grok and then converted to a timestamp. The seconds value is used to populate both `metadata.event_timestamp.seconds` and `timestamp.seconds`.  
`application` | `principal.application` | Directly mapped from the grok-extracted `application`.  
`column27` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column2` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column3` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column11` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column26` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column28` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column25` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column16` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column9` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/opnsense-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
