---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/opnsense/
title: Collect OPNsense firewall logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:27.410365+00:00
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
          chronicle/opnsense:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
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
          chronicle/opnsense:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: OPNSENSE
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

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
