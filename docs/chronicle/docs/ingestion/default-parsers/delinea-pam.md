---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-pam/
title: Collect Delinea PAM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:46:43.356283+00:00
---

# Collect Delinea PAM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-pam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Delinea PAM logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Delinea Privileged Access Manager (PAM) logs to Google Security Operations using the Bindplane agent.

Delinea PAM (Privilege Manager) generates syslog messages in CEF format for application actions, justification events, change history, password disclosures, and security events. The parser extracts fields and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Delinea PAM server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Delinea PAM web UI



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
            chronicle/delinea_pam:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: DELINEA_PAM
                raw_log_field: body
        
        service:
            pipelines:
                logs/delinea_pam_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/delinea_pam
        




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
             




## Configure syslog in Delinea Privilege Manager

**Note:** The **Send policy feedback** option needs to be enabled on **all policies** that are supposed to send syslog formatted events.

  1. Sign in to the **Delinea PAM** web UI.
  2. Go to **Admin > Configuration > Foreign Systems**.
  3. Click **Create** on **Syslog Page**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name for the server.
     * **Protocol** : Select **UDP** (you can also select **TCP** , depending on your Bindplane agent configuration).
     * **Host** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (`514` for UDP).
  5. Click **Save Changes**.



## Configure syslog server tasks in Delinea Privilege Manager

  1. Go to **Admin > Tasks > expand Server Tasks folder > expand Foreign Systems folder**.
  2. Select **Syslog**.
  3. Click **Create**.
  4. Template options: 
     * **Send SysLog Application Action Events** : Generic information about the application that ran, which policy was triggered, date, timestamp, computer, and user.
     * **Send SysLog Application Justification Events** : Events when a user runs an application requiring a justification workflow.
     * **Send SysLog Bad Rated Application Action Events** : Events when an application with a bad security rating is being installed or executed.
     * **Send SysLog Change History Events** : Change history events (first run sends all history; subsequent runs send only new events).
     * **Send SysLog Events** : All syslog events based on the options selected during syslog server setup.
     * **Send SysLog Newly Discovered File Events** : Newly discovered file events (requires Default File Inventory Policy and resource discovery schedules).
     * **Send SysLog Password Disclosure Events** : All password disclosure events.
  5. Provide the following configuration details: 
     * **Template** : Select a syslog template (for example, `Send Syslog Events` to send all the events).
     * **Name** : Enter a meaningful name for the task.
     * **Event Name** : Enter a name for the events.
     * **Event Severity** : Enter a severity level threshold for the events to be sent.
     * **Syslog System** : Select the syslog server foreign system Bindplane agent server you created in the previous step.
  6. Click **Create**.

**Note:** After creating the task, the **Scheduled Task page** is displayed, where you can run the task on demand or specify how often events are sent (hourly, every 30 minutes, or daily).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`CEF:0 | ... | column1`  
`CEF:0 | ... | column2`  
`CEF:0 | ... | column3`  
`CEF:0 | ... | column5`  
`CEF:0 | ... | column7`  
`%{HOSTNAME}` | `principal.hostname` | Extracted from the log message using the grok pattern "%{HOSTNAME}".  
`%{TIMESTAMP_ISO8601}` | `metadata.event_timestamp` | Extracted from the log message using the grok pattern "%{TIMESTAMP_ISO8601}".  
| `metadata.event_type` | Hardcoded to "STATUS_UPDATE" in the parser code.  
| `metadata.log_type` | Hardcoded to "DELINEA_PAM" in the parser code.  
`timestamp` | timestamp | The event timestamp is parsed from the "timestamp" field in the raw log, converting it to a UDM timestamp format.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/delinea-pam-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
