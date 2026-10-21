---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/filezilla-ftp/
title: Collect FileZilla FTP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:50:26.402923+00:00
---

# Collect FileZilla FTP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/filezilla-ftp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect FileZilla FTP logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest FileZilla FTP logs to Google Security Operations using the Bindplane agent.

FileZilla is an open-source FTP server and client that generates log files containing connection details, file transfer operations, authentication events, and session activity. The parser extracts fields from log data using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * The Bindplane agent must be installed on the same host as FileZilla (or have access to the FileZilla log file path)
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the FileZilla application



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

## Configure the Bindplane agent to ingest FileZilla logs and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            filelog:
                file_path: '<PATH_TO>/filezilla-logs.log'
                log_type: 'file'
        
        exporters:
            chronicle/filezilla_ftp:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: FILEZILLA_FTP
                raw_log_field: body
        
        service:
            pipelines:
                logs/filezilla_ftp_to_chronicle:
                    receivers:
                        - filelog
                    exporters:
                        - chronicle/filezilla_ftp
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `file_path`: Full path to the FileZilla log file: 
      * **Linux** : for example, `/var/log/filezilla/filezilla-logs.log`
      * **Windows** : for example, `C:\Users\<username>\AppData\Local\FileZilla\filezilla-logs.log`
      * The exact path depends on the filename and location configured in FileZilla (see Configure logging in FileZilla)
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
             




## Configure logging in FileZilla

  1. Sign in to the server with **FileZilla**.
  2. Open the FileZilla software.
  3. Go to **Edit > Settings**.
  4. Select **Logging** from the menu.
  5. Provide the following configuration details: 
     * Select the checkbox **Show timestamps in messagebox**.
     * Select the checkbox **Log to file**.
     * **Filename** : Enter a filename and select the storage path (for example, `filezilla-logs`).
     * Optional: **Limit size of logfile** : Select this checkbox to limit the amount of space a log file can use.
     * Optional: **Limit** : Enter a max file size for your log file in Megabytes.
  6. Click **OK**.
  7. Restart FileZilla.

**Note:** The log file path configured in FileZilla must match the `file_path` value in the Bindplane agent `config.yaml`.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
data | read_only_udm.metadata.description | The raw log `data` field content.  
data | read_only_udm.metadata.event_timestamp.seconds | Extracted from the `data` field using a grok pattern and converted to epoch seconds.  
data | read_only_udm.network.http.response_code | Extracted from the `data` field using a grok pattern.  
data | read_only_udm.principal.hostname | Extracted from the `data` field using a grok pattern.  
data | read_only_udm.principal.port | Extracted from the `data` field using a grok pattern.  
data | read_only_udm.principal.user.userid | Extracted from the `data` field using a grok pattern, only if the value is not `not logged in`.  
data | read_only_udm.target.ip | Extracted from the `data` field using a grok pattern.  
data | read_only_udm.target.process.pid | Extracted from the `data` field using a grok pattern.  
| read_only_udm.metadata.event_type | Set to `NETWORK_FTP` if target.ip exists, otherwise set to `GENERIC_EVENT`.  
| read_only_udm.metadata.log_type | Set to `FILEZILLA_FTP`.  
| read_only_udm.metadata.product_name | Set to `FILEZILLA`.  
| read_only_udm.metadata.vendor_name | Set to `FILEZILLA`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/filezilla-ftp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
