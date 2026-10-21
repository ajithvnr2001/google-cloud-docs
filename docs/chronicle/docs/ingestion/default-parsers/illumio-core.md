---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/illumio-core/
title: Collect Illumio Core logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:00:26.081720+00:00
---

# Collect Illumio Core logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/illumio-core/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Illumio Core logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Illumio Core logs to Google Security Operations using Bindplane.

The parser extracts fields from Illumio Core JSON, SYSLOG, SYSLOG+JSON and SYSLOG+CEF formatted logs. It uses grok and/or JSON parsing to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Illumio Policy Compute Engine (PCE) web console



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
            tcplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/chronicle_w_labels:
                compression: gzip
                creds_file_path: '/path/to/ingestion-authentication-file.json'
                customer_id: 'YOUR_CUSTOMER_ID'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: 'ILLUMIO_CORE'
                raw_log_field: body
                ingestion_labels:
        
        service:
            pipelines:
                logs/source0__chronicle_w_labels-0:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/chronicle_w_labels
        




### Configuration parameters

  * Replace the following placeholders:

    * **Receiver configuration:**

      * `tcplog`: Use `udplog` for UDP syslog or `tcplog` for TCP syslog
      * `0.0.0.0`: IP address to listen on (`0.0.0.0` to listen on all interfaces)
      * `514`: Port number to listen on (standard syslog port)
    * **Exporter configuration:**

      * `creds_file_path`: Full path to ingestion authentication file: 
        * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
        * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
      * `YOUR_CUSTOMER_ID`: Customer ID from the Get customer ID section
      * `endpoint`: Regional endpoint URL: 
        * **US** : `malachiteingestion-pa.googleapis.com`
        * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
        * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
        * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
      * `log_type`: Log type exactly as it appears in Chronicle (`ILLUMIO_CORE`)



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

      1. Press `Win+R`, type `services.msc`, and press **Enter**.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.

      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure Syslog forwarding on Illumio Core

  1. Sign in to the **Illumio Policy Compute Engine (PCE)** web console.
  2. Go to **Settings > Event Settings**.
  3. In the **Syslog Destinations** section, click **Add**.
  4. Provide the following configuration details: 
     * **Description** : Enter a descriptive name (for example, `Google-SecOps-Bindplane`).
     * **Remote Syslog Destination** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Protocol** : Select **TCP**.
     * **Severity** : Select **Informational** (or your preferred severity level, Level 6 is recommended for comprehensive logging).
     * **Format** : Select **CEF** (Common Event Format) for structured parsing.
  5. In the **Event Types** section, select the events to forward: 
     * **Organization Events** : Organization-level changes
     * **Auditable Events** : User and API audit trail
     * **Traffic Flow Events** : Network flow summaries
     * **Node Events** : VEN and workload status changes
  6. Click **Save**.
  7. Verify syslog messages are being sent by checking the Bindplane agent logs.



Alternatively, configure via API:
    
    
       curl -X POST "https://PCE_HOST:8443/api/v2/orgs/ORG_ID/settings/syslog/destinations" \
       -H "Content-Type: application/json" \
       -u "API_KEY:API_SECRET" \
       -d '{
          "description": "Google-SecOps-Bindplane",
          "remote_syslog": "BINDPLANE_IP",
          "remote_syslog_port": 514,
          "remote_syslog_protocol": 6,
          "severity": 6,
          "type": "cef"
       }'
    

  * Replace `PCE_HOST`, `ORG_ID`, `API_KEY`, `API_SECRET`, and `BINDPLANE_IP` with your values.



## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/illumio-core-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
