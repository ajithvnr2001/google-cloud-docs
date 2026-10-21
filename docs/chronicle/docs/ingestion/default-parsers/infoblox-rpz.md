---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/infoblox-rpz/
title: Collect Infoblox RPZ logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:47:39.543565+00:00
---

# Collect Infoblox RPZ logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/infoblox-rpz/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Infoblox RPZ logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Infoblox RPZ logs to Google Security Operations using the Bindplane agent.

Infoblox Response Policy Zone (RPZ) is a DNS security feature that blocks DNS queries to malicious domains based on threat intelligence feeds and custom policies. It generates syslog-formatted logs for RPZ policy hits and blocked queries.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Infoblox NIOS appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Infoblox Grid Manager or NIOS appliance



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane will be installed.

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
            chronicle/infoblox_rpz:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: INFOBLOX_RPZ
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/rpz_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/infoblox_rpz
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `infoblox_rpz`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `INFOBLOX_RPZ`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `rpz_to_chronicle`: Descriptive name for the pipeline



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
             




## Configure Infoblox RPZ syslog forwarding

  1. Sign in to the **Infoblox Grid Manager**.
  2. Go to **Grid > Grid Properties > Monitoring**.
  3. Under **Syslog** , click **Add** to configure an external syslog server.
  4. Provide the following configuration details: 
     * **Syslog Server Address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (must match the Bindplane agent receiver port).
     * **Protocol** : Select **UDP**.
     * **Severity** : Select **Info** or higher to capture RPZ events.
  5. Click **Save & Close**.
  6. Ensure that RPZ query logging is enabled on the relevant DNS views: 
     1. Go to **Data Management > DNS > Zones**.
     2. Select the RPZ zone.
     3. Verify that **Logging** is enabled for RPZ policy hits.
  7. Verify that syslog messages are being received by checking the Bindplane agent logs.

**Note:** Infoblox NIOS forwards RPZ logs via syslog in standard syslog format. Ensure that RPZ query logging is enabled on all DNS views where RPZ policies are applied.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`serverIp` | `intermediary.asset.ip` | Merged  
`serverIp` | `intermediary.ip` | Merged  
`descrip` | `metadata.description` | Directly mapped  
`msg` | `metadata.description` | Directly mapped  
`syslogTimestamp` | `metadata.event_timestamp` | Parsed as `dd-MMM-yyyy HH:mm:ss.SSS`  
`ts` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss`  
`event_type` | `metadata.event_type` | Directly mapped  
`device_event_class_id` | `metadata.product_event_type` | Directly mapped  
`evt_type` | `metadata.product_event_type` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`dns` | `network.dns` | Renamed/mapped  
`protocol` | `network.ip_protocol` | Directly mapped  
`dnsDomain` | `principal.asset.hostname` | Directly mapped  
`clientIp` | `principal.asset.ip` | Merged  
`dnsDomain` | `principal.hostname` | Directly mapped  
`clientIp` | `principal.ip` | Merged  
`srcPort` | `principal.port` | Directly mapped  
`severity` | `security_result.severity` | Mapped values (5 total, e.g. `"0", "1", "2", "3", "LOW"` → `LOW`, `"informational", "INFORMA...  
`dnsServerIp` | `target.asset.ip` | Merged  
`dnsServerIp` | `target.ip` | Merged  
N/A | `metadata.product_event_type` | Constant: `DNS Query`  
N/A | `metadata.product_name` | Constant: `NIOS`  
N/A | `metadata.vendor_name` | Constant: `INFOBLOX`  
N/A | `network.application_protocol` | Constant: `DNS`  
N/A | `security_result.severity` | Constant: `LOW`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/infoblox-rpz-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
