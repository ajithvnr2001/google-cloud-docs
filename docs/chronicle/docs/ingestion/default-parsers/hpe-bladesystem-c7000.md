---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hpe-bladesystem-c7000/
title: Collect HPE BladeSystem c7000 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:02:29.772877+00:00
---

# Collect HPE BladeSystem c7000 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hpe-bladesystem-c7000/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect HPE BladeSystem c7000 logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest HPE BladeSystem c7000 logs to Google Security Operations using the Bindplane agent.

HPE BladeSystem c7000 is a blade server enclosure that generates syslog messages for hardware events, component status changes, configuration changes, and system alerts. The parser extracts fields from syslog-formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the HPE BladeSystem c7000
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the HPE BladeSystem Onboard Administrator or StorageGRID Manager



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
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/hpe_bladesystem_c7000:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: HPE_BLADESYSTEM_C7000
                raw_log_field: body
        
        service:
            pipelines:
                logs/hpe_bladesystem_c7000_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/hpe_bladesystem_c7000
        




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
             




## Configure syslog directly in HPE BladeSystem

  1. Sign in to the **BladeSystem** UI.
  2. Go to **Configuration > System Log**.
  3. Click the **Log Options** tab.
  4. Select the **Enable remote system logging** checkbox.
  5. Provide the following configuration details: 
     * **Syslog Server Address** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (default port is `514`).
     * **Protocol** : The protocol is always **UDP**.
  6. Click **Test Remote Log** and verify logs are received.
  7. Click **Apply** to save.



## Configure syslog in StorageGRID Software

You can configure both the audit message levels within StorageGRID and set up external syslog servers for forwarding these messages.

### Configure StorageGRID audit message levels

  1. Sign in to the **GRID Manager** web UI.
  2. Go to **Configuration > Monitoring > Audit and syslog server**.
  3. For each category of audit message, select the **Normal** audit level from the list.
  4. Click **Save**.



### Configure StorageGRID external syslog server

  1. From the **Audit and syslog server** page, click **Configure external syslog server**.
  2. Provide the following configuration details: 
     * Enter the Bindplane agent IP address.
     * Enter the Bindplane agent port number (default port is `514`).
     * Select the **UDP** or **TCP** protocol, depending on your Bindplane agent configuration.
  3. Click **Continue**.



### Configure syslog events

  1. From the **Manage syslog content** step of the wizard, select each type of audit information you want to send to the external syslog server: 
     * Send audit logs
     * Send security events
     * Send application logs
     * Send access logs
  2. For **Severity** , select **Passthrough** or **7** (Informational).
  3. For **Facility** , select **Passthrough**.
  4. Click **Continue**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`command` | `principal.process.command_line` | Directly mapped from the raw log field "command".  
`component` | `metadata.product_event_type` | Directly mapped from the raw log field "component".  
`component_name` | `additional.fields[0].value.string_value` | Directly mapped from the raw log field "component_name".  
`description` | `security_result.description` | Directly mapped from the raw log field "description" after optional grok parsing.  
`description` | `security_result.detection_fields[0].value` | Extracted from the "description" field using a grok pattern. Represents the current state.  
`description` | `security_result.detection_fields[1].value` | Extracted from the "description" field using a grok pattern. Represents the previous state.  
`description` | `security_result.detection_fields[2].value` | Extracted from the "description" field using a grok pattern. Represents the cause of the state change.  
`event_timestamp` | `metadata.event_timestamp` | Directly mapped from the raw log field "event_timestamp" after date parsing.  
`hostname` | `principal.hostname` | Directly mapped from the raw log field "hostname".  
`hostname` | `principal.asset.hostname` | Copied from the mapped "principal.hostname" field.  
`internal_code` | `additional.fields[1].value.string_value` | Directly mapped from the raw log field "internal_code".  
`priority_id` | `additional.fields[2].value.string_value` | Directly mapped from the raw log field "priority_id".  
| `additional.fields[0].key` | Static value: "Component Name".  
| `additional.fields[1].key` | Static value: "Internal Code".  
| `additional.fields[2].key` | Static value: "Priority Id".  
| `metadata.event_type` | Set to "STATUS_UPDATE" if "principal.hostname" is successfully extracted, otherwise set to "GENERIC_EVENT".  
| `metadata.vendor_name` | Static value: "HP".  
| `metadata.product_name` | Static value: "HPE BladeSystem c7000".  
| `metadata.log_type` | Static value: "HPE_BLADESYSTEM_C7000".  
| `security_result.severity` | Mapped from the "severity" field based on the following logic:- "Critical" -> "CRITICAL"- "Major" -> "HIGH"- "Warning" -> "MEDIUM"- "Info", "Minor" -> "LOW"- Default -> "UNKNOWN_SEVERITY"  
| `security_result.detection_fields[0].key` | Static value: "Current State".  
| `security_result.detection_fields[1].key` | Static value: "Previous State".  
| `security_result.detection_fields[2].key` | Static value: "Cause".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hpe-bladesystem-c7000-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
