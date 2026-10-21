---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/airwatch/
title: Collect Omnissa Workspace ONE UEM (formerly VMware AirWatch) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:22:40.064879+00:00
---

# Collect Omnissa Workspace ONE UEM (formerly VMware AirWatch) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/airwatch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Omnissa Workspace ONE UEM (formerly VMware AirWatch) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can ingest Omnissa Workspace ONE UEM (formerly known as VMware AirWatch) logs to Google Security Operations using Bindplane.

Omnissa Workspace ONE UEM is an enterprise mobility management (EMM) platform that provides unified endpoint management across mobile, desktop, rugged, and IoT devices. It enables IT administrators to enroll, configure, secure, and manage corporate and employee-owned devices from a single console.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Omnissa Workspace ONE UEM
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Omnissa Workspace ONE UEM console with administrator role



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

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /status observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            tcplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/airwatch:
                compression: gzip
                creds_file_path: '<PLACEHOLDER_CREDS_FILE_PATH>'
                customer_id: '<PLACEHOLDER_CUSTOMER_ID>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: AIRWATCH
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/airwatch_to_chronicle:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/airwatch
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: TCP syslog receiver for reliable log delivery from Workspace ONE UEM
    * `0.0.0.0:514`: IP address and port to listen on. Replace the port as required in your infrastructure
  * **Exporter configuration:**

    * `<PLACEHOLDER_CREDS_FILE_PATH>`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<PLACEHOLDER_CUSTOMER_ID>`: Google SecOps customer ID
    * `malachiteingestion-pa.googleapis.com`: Regional endpoint URL. Replace with the appropriate endpoint for your region: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux: 

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows:

  1. Choose one of the following options:

     * Command Prompt or PowerShell as administrator:
    
    net stop observiq-otel-collector && net start observiq-otel-collector
    

     * Services console: 
       1. Press `Win+R`, type `services.msc`, and press Enter.
       2. Locate **observIQ OpenTelemetry Collector**.
       3. Right-click and select **Restart**.
  2. Verify the service is running:
         
         sc query observiq-otel-collector
         

  3. Check logs for errors:
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         




## Configure syslog forwarding in Omnissa Workspace ONE UEM

  1. Sign in to the **Omnissa Workspace ONE UEM** console.
  2. Go to **Groups & Settings > All Settings > System > Enterprise Integration > Syslog**.
  3. Select **Override** for the **Current Setting** if inheriting from a parent organization group.
  4. Set **Syslog Integration** to **Enabled**.
  5. Provide the following configuration details: 
     * **Hostname** : Enter the IP address or FQDN of the Bindplane agent host.
     * **Protocol** : Select **TCP**.
     * **Port** : Enter the Bindplane agent port number (for example, `514`).
     * **Syslog Facility** : Leave as default or select the appropriate facility for your environment.
     * **Message Tag** : Enter `Airwatch`.
     * **Message Content** : Leave as default.
  6. Go to the **Advanced** tab.
  7. Provide the following configuration details: 
     * **Console Events** : Select **Enable**.
     * **Select Console Events to Send to Syslog** : Click **Select All**.
     * **Device Events** : Select **Enable**.
     * **Select Device Events to Send to Syslog** : Click **Select All**.
  8. Click **Save**.
  9. Click **Test Connection** to verify that syslog events are being forwarded to the Bindplane agent.



For more information, see [Omnissa Workspace ONE UEM Troubleshooting and Logging Guide](https://docs.omnissa.com/bundle/TroubleshootingandLoggingGuideV2306/page/ConfigureSyslog.html).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`AdminAccount` | `principal.user.userid` | The value is taken from the `AdminAccount` field in the raw log.  
`Application` | `target.application` | The value is taken from the `Application` field in the raw log.  
`Event` | `metadata.product_event_type` | The value is taken from the `Event` field in the raw log.  
`EventSource` | `principal.application` | The value is taken from the `EventSource` field in the raw log.  
`FriendlyName` | `principal.asset.hostname` | The value is taken from the `FriendlyName` field in the raw log.  
`GroupName` | `target.group.group_display_name` | The value is taken from the `GroupName` field in the raw log.  
`Severity` | `security_result.severity` | Mapped based on severity value: `Information` maps to `INFORMATIONAL`, `Warning` maps to `MEDIUM`, `Critical` maps to `HIGH`.  
| `metadata.product_name` | Set to `AIRWATCH`.  
| `metadata.vendor_name` | Set to `VMware`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/airwatch-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
