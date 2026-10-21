---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/revivesec/
title: Collect ReviveSec logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:33:32.988002+00:00
---

# Collect ReviveSec logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/revivesec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ReviveSec logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ReviveSec logs to Google Security Operations using the Bindplane agent.

ReviveSec is a security analytics platform by Revive Security Ltd (Israel) that specializes in Check Point firewall health monitoring, proactive fault detection, and endpoint monitoring. The platform deploys lightweight agents on Windows and Linux machines that monitor processes, files, network connections, DNS, and USB devices.

## Before you begin

  * Make sure you have the following prerequisites:

  * A Google SecOps instance

  * Windows Server 2016 or later, or Linux host with `systemd`

  * Network connectivity between the Bindplane agent and the ReviveSec server

  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements

  * Privileged access to the ReviveSec portal with administrator permissions




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
            filelog:
                include:
                    - /path/to/revivesec/logs/*.json
                    - /path/to/revivesec/logs/*.csv
                start_at: beginning
        
        exporters:
            chronicle/revivesec:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: REVIVESEC
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/revivesec_to_chronicle:
                    receivers:
                        - filelog
                    exporters:
                        - chronicle/revivesec
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths or glob patterns to monitor: 
      * Adjust the path to match your ReviveSec log file location
      * Use glob patterns (for example, `*.json`, `*.csv`) to match multiple files
    * `start_at`: Set to `beginning` to read existing log files from the start, or `end` to only read new entries
  * **Exporter configuration:**

    * `revivesec`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `REVIVESEC`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `revivesec_to_chronicle`: Descriptive name for the pipeline



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
             




## Export ReviveSec logs for collection

  1. Sign in to the ReviveSec administration portal.
  2. Navigate to the **Analytics** or **Reports** section.
  3. Select the desired report type (health check, compliance, endpoint activity, or firewall analytics).
  4. Apply date range filters as needed.
  5. Click **Export** and select the output format: 
     * **JSON** : Recommended for SIEM ingestion.
     * **CSV** : Tabular format for structured data.
  6. Save the exported files to the directory monitored by the Bindplane agent (for example, `/path/to/revivesec/logs/`).
  7. (Optional) Configure scheduled reports (daily, weekly, or monthly) to automatically export data to the monitored directory. Contact ReviveSec support for details on automated export options and API access.

**Note:** Ensure the Bindplane agent has read access to the directory where ReviveSec log files are saved.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`country_label` | `additional.fields` | Merged  
`hit_count_label` | `additional.fields` | Merged  
`linkInfo_label` | `additional.fields` | Merged  
`proxy_label` | `additional.fields` | Merged  
`signature_label` | `additional.fields` | Merged  
`signature_status_label` | `additional.fields` | Merged  
`svc_num_label` | `additional.fields` | Merged  
`desc` | `metadata.description` | Directly mapped  
`description` | `metadata.description` | Directly mapped  
`description_gateway` | `metadata.description` | Directly mapped  
`description_signature` | `metadata.description` | Directly mapped  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`product_event` | `metadata.product_event_type` | Directly mapped  
`domain` | `principal.asset.hostname` | Directly mapped  
`info_ip` | `principal.asset.ip` | Merged  
`ipadd` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`domain` | `principal.hostname` | Directly mapped  
`info_ip` | `principal.ip` | Merged  
`ipadd` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`country_name` | `principal.location.country_or_region` | Directly mapped  
`port` | `principal.port` | Directly mapped  
`link_url` | `principal.url` | Directly mapped  
`display_name` | `principal.user.user_display_name` | Directly mapped  
`username` | `principal.user.userid` | Directly mapped  
`domain_name` | `target.asset.hostname` | Directly mapped  
`ipadd` | `target.asset.ip` | Merged  
`domain_name` | `target.hostname` | Directly mapped  
`ipadd` | `target.ip` | Merged  
N/A | `metadata.event_type` | Constant: `NETWORK_CONNECTION`  
N/A | `metadata.product_name` | Constant: `REVIVESEC`  
N/A | `metadata.vendor_name` | Constant: `REVIVESEC`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/revivesec-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
