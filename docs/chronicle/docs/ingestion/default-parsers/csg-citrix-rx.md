---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/csg-citrix-rx/
title: Collect Citrix Receiver logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:46.917233+00:00
---

# Collect Citrix Receiver logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/csg-citrix-rx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Citrix Receiver logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Citrix Receiver logs to Google Security Operations using the Bindplane agent.

Citrix Receiver (now Citrix Workspace app) is a client-side application that provides access to virtual desktops, applications, and data from Citrix Virtual Apps and Desktops environments. The logs capture session events, authentication, and client-side activity.

**Note:** Logging is disabled by default in Citrix Receiver and must be explicitly enabled via registry entries before log files are generated.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Citrix Receiver host
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Citrix environment with administrator permissions
  * Access to Citrix Receiver log files on the server or client file system



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

## Configure the Bindplane agent to ingest logs and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            filelog:
                include:
                    - 'C:\Users\*\AppData\Local\Citrix\Receiver\*.log'
                start_at: beginning
                poll_interval: 5s
        
        exporters:
            chronicle/citrix_rx:
                compression: gzip
                creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: CSG_CITRIX_RX
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/citrix_rx_to_chronicle:
                    receivers:
                        - filelog
                    exporters:
                        - chronicle/citrix_rx
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `include`: Paths to Citrix Receiver log files: 
      * **Windows** : `C:\Users\*\AppData\Local\Citrix\Receiver\*.log`
      * **Centralized collection** : Adjust the path if logs are collected to a central share
    * `start_at`: Set to `beginning` to read existing logs, or `end` to read only new entries
    * `poll_interval`: How often to check for new log data (default: `5s`)
  * **Exporter configuration:**

    * `citrix_rx`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `CSG_CITRIX_RX`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `citrix_rx_to_chronicle`: Descriptive name for the pipeline



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
             




## Enable Citrix Receiver logging and configure log collection

Logging is disabled by default in Citrix Receiver. You must enable it using registry entries before log files are generated.

### Enable logging on Windows

  1. Open **Registry Editor** (`regedit`) as an administrator on the Citrix Receiver client machine.
  2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Citrix\Receiver`.
  3. Create a new **String Value** named `EnableTracing` and set it to `true`.
  4. Create a new **String Value** named `TracePath` to specify the log output path. For example:

     * `C:\CitrixLogs\`
     * Alternatively, use the default path: `%USERPROFILE%\AppData\Local\Citrix\Receiver\`
  5. Restart the Citrix Receiver application for the changes to take effect.




### Verify log file generation

  1. After enabling logging, open the Citrix Receiver and connect to a published resource.
  2. Navigate to the log directory: 
     * **Default path** : `%USERPROFILE%\AppData\Local\Citrix\Receiver\`
     * **Custom path** : The path specified in the `TracePath` registry value.
  3. Verify that `.log` files are being created and contain session event data.
  4. Ensure the Bindplane agent has read permissions on the log directory and files.

**Note:** If the Bindplane agent runs on a centralized server, copy the Citrix Receiver logs from each client machine to a central directory and update the `include` path in the Bindplane agent configuration accordingly.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`creationTime` | `metadata.event_timestamp` | Parsed as `dd/M/yyyy HH:mm:ss`  
`timestamp` | `metadata.event_timestamp` | Parsed as `MMM d HH:mm:ss`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`logId` | `metadata.product_log_id` | Directly mapped  
`srcip` | `principal.asset.ip` | Merged  
`srcip` | `principal.ip` | Merged  
`userId` | `principal.user.userid` | Directly mapped  
`application` | `target.application` | Directly mapped  
`targetip` | `target.asset.ip` | Merged  
`targetip` | `target.ip` | Merged  
`resourcename` | `target.resource.name` | Directly mapped  
N/A | `metadata.event_type` | Constant: `NETWORK_CONNECTION`  
N/A | `metadata.product_name` | Constant: `CSG Citrix RX`  
N/A | `metadata.vendor_name` | Constant: `CSG Citrix RX`  
`logId` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`application` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`resourcename` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`srcip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`target` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`creationTime` | `event.idm.read_only_udm.target.resource.attribute.creation_time` | Mapped from changelog  
`user` | `event.idm.read_only_udm.principal.user.user` | Mapped from changelog  
`targetip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.timestamp` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/csg-citrix-rx-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
