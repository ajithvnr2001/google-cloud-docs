---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arista-switch/
title: Collect Arista switch logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:02:55.100870+00:00
---

# Collect Arista switch logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arista-switch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Arista switch logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Arista switch logs to Google Security Operations using Bindplane agent.

Arista EOS (Extensible Operating System) runs on Arista network switches and generates syslog messages for system events, interface changes, authentication, AAA accounting, and protocol state changes. The parser handles both JSON and syslog formats.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Arista switch
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Arista EOS 4.23.x or later
  * Privileged access on the Arista EOS switch



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

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure Bindplane agent to ingest syslog and send to Google SecOps

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
            chronicle/arista_switch:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: ARISTA_SWITCH
                raw_log_field: body
        
        service:
            pipelines:
                logs/arista_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/arista_switch
        




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
             




## Configure syslog on the Arista switch

  1. Sign in to the **Arista** switch.
  2. Enter configuration mode:
         
         Arista# configure terminal
         

  3. Configure the syslog destination to send logs to the Bindplane agent:
         
         Arista(config)# logging host <bindplane-server-ip> <port-number> protocol udp
         Arista(config)# logging trap informational
         Arista(config)# copy running-config startup-config
         

     * Replace `<bindplane-server-ip>` with the Bindplane agent IP address.
     * Replace `<port-number>` with the port configured to listen (for example, `514`).
  4. (Optional) Enable command execution logging for AAA accounting:
         
         Arista(config)# aaa accounting commands all console start-stop logging
         Arista(config)# aaa accounting commands all default start-stop logging
         Arista(config)# aaa accounting exec console start-stop logging
         Arista(config)# aaa accounting exec default start-stop logging
         Arista(config)# copy running-config startup-config
         

  5. (Optional) Enable authentication success and failure logging:
         
         Arista(config)# aaa authentication policy on-success log
         Arista(config)# aaa authentication policy on-failure log
         Arista(config)# copy running-config startup-config
         




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`appname` | `target.application` | Directly mapped from the `appname` field.  
`description` | `metadata.description` | Directly mapped from the `description` field, which is extracted from the `message` field using grok patterns based on the `product_event_type`.  
`dst_ip` | `target.ip`, `target.asset.ip` | Directly mapped from the `dst_ip` field, which is extracted from the `message` field using grok patterns.  
`dst_mac` | `target.mac` | Directly mapped from the `dst_mac` field, which is extracted from the `message` field using grok patterns.  
`dst_port` | `target.port` | Directly mapped from the `dst_port` field, which is extracted from the `message` field using grok patterns.  
`facility` | `additional.fields[facility].string_value` | Directly mapped from the `facility` field.  
`hostname` | `principal.hostname`, `principal.asset.hostname` | Directly mapped from the `hostname` field.  
`inner_msg` | `metadata.description` | Directly mapped from the `inner_msg` field, which is extracted from the `message` field using grok patterns.  
`ip_protocol` | `network.ip_protocol` | Directly mapped from the `ip_protocol` field, which is extracted from the `message` field using grok patterns. If the value is "tcp", it's converted to "TCP". If the event type is "NO_IGMP_QUERIER", it's set to "IGMP".  
`pid` | `principal.process.pid` | Directly mapped from the `pid` field, which is extracted from the `message` field using grok patterns.  
`prin_ip` | `principal.ip`, `principal.asset.ip` | Directly mapped from the `prin_ip` field, which is extracted from the `message` field using grok patterns.  
`product_event_type` | `metadata.product_event_type` | Directly mapped from the `product_event_type` field, which is extracted from the `message` field using grok patterns.  
`proto` | `network.application_protocol` | If the `proto` field is "sshd", the UDM field is set to "SSH".  
`severity` | `security_result.severity`, `security_result.severity_details` | The `security_result.severity` is derived from the `severity` field based on these mappings: "DEFAULT", "DEBUG", "INFO", "NOTICE" -> "INFORMATIONAL"; "WARNING", "ERROR", "ERR", "WARN" -> "MEDIUM"; "CRITICAL", "ALERT", "EMERGENCY" -> "HIGH". The raw value of `severity` is mapped to `security_result.severity_details`.  
`session_id` | `network.session_id` | Directly mapped from the `session_id` field, which is extracted from the `message` field using grok patterns.  
`source_ip` | `principal.ip`, `principal.asset.ip` | Directly mapped from the `source_ip` field, which is extracted from the `message` field using grok patterns.  
`source_port` | `principal.port` | Directly mapped from the `source_port` field, which is extracted from the `message` field using grok patterns.  
`src_ip` | `principal.ip`, `principal.asset.ip` | Directly mapped from the `src_ip` field, which is extracted from the `message` field using grok patterns.  
`table_name` | `target.resource.name` | Directly mapped from the `table_name` field, which is extracted from the `message` field using grok patterns. If this field is populated, `target.resource.resource_type` is set to "TABLE".  
`target_host` | `target.hostname`, `target.asset.hostname` | Directly mapped from the `target_host` field, which is extracted from the `message` field using grok patterns.  
`target_ip` | `target.ip`, `target.asset.ip` | Directly mapped from the `target_ip` field, which is extracted from the `message` field using grok patterns.  
`target_package` | `target.process.command_line` | Directly mapped from the `target_package` field, which is extracted from the `message` field using grok patterns.  
`target_port` | `target.port` | Directly mapped from the `target_port` field, which is extracted from the `message` field using grok patterns.  
`timestamp` | `metadata.event_timestamp` | Directly mapped from the `timestamp` field after being parsed into a timestamp object.  
`user` | `principal.user.userid` | Directly mapped from the `user` field, which is extracted from the `message` field using grok patterns.  
`user_name` | `target.user.userid` | Directly mapped from the `user_name` field, which is extracted from the `message` field using grok patterns.  
`vrf` | `additional.fields[vrf].string_value` | Directly mapped from the `vrf` field, which is extracted from the `message` field using grok patterns. Derived from a combination of `has_principal`, `has_target`, `user`, `message`, `product_event_type`, and `description` fields using complex conditional logic as described in the parser code. Default value is "GENERIC_EVENT". Hardcoded to "ARISTA_SWITCH". Hardcoded to "Arista Switch". Hardcoded to "Arista". Set to "BLOCK" if the `description` field contains "connection rejected".  
`dpid` | `additional.fields[DPID].string_value` | Directly mapped from the `dpid` field.  
`intf` | `additional.fields[intf].string_value` | Directly mapped from the `intf` field.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arista-switch-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
