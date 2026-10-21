---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/comodo-av/
title: Collect Xcitium Endpoint Security logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:27:03.459796+00:00
---

# Collect Xcitium Endpoint Security logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/comodo-av/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Xcitium Endpoint Security logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Xcitium Endpoint Security (formerly Comodo) logs to Google Security Operations using the Bindplane agent.

Xcitium Endpoint Security is an endpoint protection platform that combines antivirus, firewall, intrusion prevention, and containment technologies to protect endpoints from known and unknown threats. It uses a default-deny approach with auto-containment to isolate unrecognized files and processes, preventing them from causing damage while they are analyzed.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Xcitium-managed endpoints
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Xcitium Endpoint Manager console (formerly Comodo ITSM / ITarian)
  * Administrator role in Xcitium Endpoint Manager to modify configuration profiles and portal settings



## Get Google SecOps Ingestion Authentication File

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where the Bindplane agent will be installed.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



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
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/comodo_av:
                compression: gzip
                creds_file_path: '/path/to/ingestion-authentication-file.json'
                customer_id: 'your-customer-id'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: COMODO_AV
                raw_log_field: body
                ingestion_labels:
        
        service:
            pipelines:
                logs/comodo_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/comodo_av
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: The IP address and port to listen on. Use `0.0.0.0` to listen on all interfaces. Default syslog port is `514`.
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the ingestion authentication file. 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID from the Google SecOps console.
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for the complete list.



### Save the configuration file

  * After editing, save the file:

    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`.
    * **Windows** : Click **File** > **Save**.



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
             




## Configure Xcitium Endpoint Security syslog forwarding

Xcitium Endpoint Manager provides two levels of syslog forwarding. Configure both to ensure comprehensive log coverage.

### Configure endpoint-level syslog forwarding (Xcitium Client - Security logs)

  1. Sign in to the **Xcitium Endpoint Manager** console.
  2. Go to **Configuration Templates** > **Profiles**.
  3. Click the Windows profile you want to modify, or create a new profile.
  4. Click **Add Profile Section** > **Logging Settings**.
  5. In the **Xcitium Client - Security** section, enable **Write to Syslog Server**.
  6. Provide the following configuration details: 
     * **Host** : Enter the IP address or hostname of the Bindplane agent host.
     * **Port** : Enter the port number configured in the Bindplane agent (for example, `514`).
  7. Optionally, enable **Write to Log File (CEF Format)** to keep a local copy of logs in Common Event Format.
  8. In the **Communication Client** section, enable **Write to Syslog Server**.
  9. Provide the following configuration details: 
     * **Host** : Enter the IP address or hostname of the Bindplane agent host.
     * **Port** : Enter the port number configured in the Bindplane agent (for example, `514`).
  10. Select the event types for which logs are collected: 
     * Monitoring logs
     * Script logs
     * OS patch logs
     * Third party application update logs
     * Application installation logs
     * Uninstall logs
     * Event Detection and Response (EDR) agent communication logs
     * Xcitium Client - Security (XCS) communication logs
     * Remote Control Communication Logs
     * Operational Logs
  11. Click **Save**.



### Configure portal-level syslog forwarding (audit logs)

  1. Sign in to the **Xcitium Endpoint Manager** console.
  2. Go to **Settings** > **Portal Set-Up** > **Logging Settings**.
  3. Click **Edit**.
  4. Enable **Write to syslog server**.
  5. Provide the following configuration details: 
     * **Host** : Enter the IP address or hostname of the Bindplane agent host.
     * **Port** : Enter the port number configured in the Bindplane agent (for example, `514`).
  6. Click **Save**.

**Note:** The portal-level logging settings feature may need to be enabled by your Xcitium account manager. Contact Xcitium support if the option is not available.



For more information, see the [Xcitium Endpoint Manager Logging Settings documentation](https://help.comodo.com/topic-463-1-1029-15685-Logging-Settings.html) and [Configure Audit Log Settings](https://help.comodo.com/topic-463-1-1029-15794-Configure-Audit-Log-Settings.html).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`event_type` | `metadata.event_type` | Renamed/mapped  
`data5` | `principal.application` | Directly mapped  
`data3` | `principal.asset.platform_software.platform_version` | Directly mapped  
`dvchost` | `principal.hostname` | Directly mapped  
`dvc` | `principal.ip` | Merged  
`data4` | `principal.user.product_object_id` | Directly mapped  
`filePath` | `target.file.full_path` | Directly mapped  
`fname` | `target.process.parent_process.file.full_path` | Directly mapped  
`suser` | `target.user.userid` | Directly mapped  
N/A | `metadata.product_name` | Constant: `COMODO_AV`  
N/A | `metadata.vendor_name` | Constant: `COMODO`  
N/A | `principal.ip` | Constant: `dvc`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
