---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-netweaver/
title: Collect SAP NetWeaver logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:57:19.960712+00:00
---

# Collect SAP NetWeaver logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-netweaver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect SAP NetWeaver logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest SAP NetWeaver logs to Google Security Operations using the Bindplane agent.

SAP NetWeaver is an application server platform that generates security audit logs, system logs, and gateway events. The Bindplane agent collects SAP NetWeaver log files directly from the local file system.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the SAP NetWeaver application server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the SAP NetWeaver application server with administrator permissions



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
                    - /usr/sap/<SID>/DVEBMGS00/log/*.log
                start_at: beginning
        
        exporters:
            chronicle/sap_netweaver:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: SAP_NETWEAVER
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/sap_netweaver_to_chronicle:
                    receivers:
                        - filelog
                    exporters:
                        - chronicle/sap_netweaver
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths to monitor. Default SAP NetWeaver log locations: 
      * **Linux** : `/usr/sap/<SID>/DVEBMGS00/log/*.log`
      * **Windows** : `C:\usr\sap\<SID>\DVEBMGS00\log\*.log`
      * Replace `<SID>` with your SAP System ID (for example, `PRD`, `QAS`, `DEV`)
    * `start_at`: Set to `beginning` to read existing logs or `end` to only read new entries
  * **Exporter configuration:**

    * `sap_netweaver`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for the complete list
    * `SAP_NETWEAVER`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `sap_netweaver_to_chronicle`: Descriptive name for the pipeline



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
             




## Configure SAP NetWeaver logging

  1. Sign in to the **SAP** system using SAP GUI with an administrator account.
  2. Run transaction **RZ10** to access the profile parameter editor.
  3. Select the instance profile for your SAP application server.
  4. Verify or configure the following logging parameters: 
     * **rslg/log_file** : Specifies the system log path (for example, `/usr/sap/<SID>/DVEBMGS00/log/SLOG<instance>`).
     * **rsau/local/file** : Specifies the security audit log path.
     * **gw/logging** : Set to `1` to enable gateway logging.
  5. Click **Save** and activate the profile.
  6. Restart the SAP application server to apply the profile changes.
  7. Verify the log file locations on the server: 
     * **System logs** : `/usr/sap/<SID>/DVEBMGS00/log/SLOG*`
     * **Security audit logs** : `/usr/sap/<SID>/DVEBMGS00/log/audit_*`
     * **Gateway logs** : `/usr/sap/<SID>/DVEBMGS00/log/dev_rd*`
  8. Ensure the Bindplane agent `include` paths in `config.yaml` match the actual log file locations on your SAP NetWeaver server.

**Note:** Replace `<SID>` with your SAP System ID. The Bindplane agent service account must have read access to the SAP log directory. You can add multiple paths to the `include` list to capture different log types simultaneously.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
MessageData | metadata.description | Description of the event  
| metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
EventReceivedTime | metadata.ingested_timestamp | Timestamp when the event was ingested  
MessageID | metadata.product_log_id | Product-specific log identifier  
Program | principal.application | Application name  
ProcessID | principal.process.pid | Process ID  
Username | principal.user.userid | User ID  
SourceModuleName | target.resource.name | Resource name  
SourceModuleType | target.resource.resource_subtype | Resource subtype  
| metadata.vendor_name | Vendor/company name  
| metadata.product_name | Product name  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-netweaver-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
