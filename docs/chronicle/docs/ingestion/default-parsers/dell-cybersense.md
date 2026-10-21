---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-cybersense/
title: Collect Dell CyberSense logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:08:13.759793+00:00
---

# Collect Dell CyberSense logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-cybersense/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Dell CyberSense logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Dell CyberSense logs to Google Security Operations using the Bindplane agent.

Dell CyberSense (part of Dell PowerProtect) is a cyber recovery solution that detects ransomware and data corruption. The system generates syslog messages in standard syslog and CEF formats for audit events, indexing jobs, and infection detection. The parser extracts fields and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Dell PowerProtect system
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * CLI access to the Dell PowerProtect system



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
            chronicle/dell_cybersense:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: DELL_CYBERSENSE
                raw_log_field: body
        
        service:
            pipelines:
                logs/dell_cybersense_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/dell_cybersense
        




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
             




## Configure syslog for Dell CyberSense

  1. Sign in to the **Dell PowerProtect** using CLI.
  2. Edit the `/etc/audisp/plugins.d/syslog.conf` file so that `active = yes`, and then save and exit the file.
  3. Open the rsyslog configuration file using `vi`, enter the following content, and then save and exit the file (`:wq`):
         
         $ModLoad imfile
         $InputFileName /var/log/audit/audit.log
         $InputFileTag tag_audit_log:
         $InputFileStateFile audit_log
         $InputFileSeverity info
         $InputFileFacility local6
         $InputRunFileMonitor
         *.* @<Bindplane_IP>:514
         

     * Replace `<Bindplane_IP>` with the Bindplane agent IP address.
  4. Restart the rsyslog service:
         
         service rsyslog restart
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`crjobids_label` | `additional.fields` | Merged  
`crpolicy_label` | `additional.fields` | Merged  
`infected_list` | `additional.fields` | Merged  
`lanjobdefname_label` | `additional.fields` | Merged  
`lanjobinstid_label` | `additional.fields` | Merged  
`tty_label` | `additional.fields` | Merged  
`msg` | `metadata.description` | Directly mapped  
`ts` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event_type` | `metadata.event_type` | Directly mapped  
`device_event_class_id` | `metadata.product_event_type` | Directly mapped  
`event_name` | `metadata.product_event_type` | Directly mapped  
`device_product` | `metadata.product_name` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`device_vendor` | `metadata.vendor_name` | Directly mapped  
`session` | `network.session_id` | Directly mapped  
`client_IP` | `principal.asset.hostname` | Directly mapped  
`hostname` | `principal.asset.hostname` | Directly mapped  
`%{client_IP}` | `principal.asset.ip` | Merged  
`client_IP` | `principal.asset.ip` | Mapped when `client_IP` != ``  
`path` | `principal.file.full_path` | Directly mapped  
`client_IP` | `principal.hostname` | Directly mapped  
`hostname` | `principal.hostname` | Directly mapped  
`%{client_IP}` | `principal.ip` | Merged  
`client_IP` | `principal.ip` | Mapped when `client_IP` != ``  
`cradmin` | `principal.process.command_line` | Directly mapped  
`URL` | `principal.url` | Directly mapped  
`crjobids_label` | `security_result.detection_fields` | Merged  
`engine_id_label` | `security_result.detection_fields` | Merged  
`severity` | `security_result.severity` | Mapped: `"EMERGENCY","ALERT","CRITICAL"` → `CRITICAL`, `WARN` → `HIGH`, `NOTICE` → `MEDIUM`,...  
`host` | `target.asset.hostname` | Directly mapped  
`host` | `target.hostname` | Directly mapped  
`dbname` | `target.resource.name` | Directly mapped  
`dbuuid` | `target.resource.product_object_id` | Directly mapped  
N/A | `metadata.product_name` | Constant: `DELL_CYBERSENSE`  
N/A | `metadata.vendor_name` | Constant: `DELL_CYBERSENSE`  
N/A | `security_result.severity` | Constant: `CRITICAL`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-cybersense-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
