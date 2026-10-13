---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arbor-edge-defense/
title: Collect NETSCOUT Arbor Edge Defense logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:26.197727+00:00
---

# Collect NETSCOUT Arbor Edge Defense logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arbor-edge-defense/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect NETSCOUT Arbor Edge Defense logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest NETSCOUT Arbor Edge Defense (AED) logs to Google Security Operations using Bindplane.

NETSCOUT Arbor Edge Defense is a network security appliance that sits at the perimeter between your internal network and the internet. It provides automated DDoS protection, threat intelligence-based blocking, and reputation analysis to stop inbound and outbound threats before they can impact network availability or compromise resources.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and NETSCOUT Arbor Edge Defense appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the NETSCOUT Arbor Edge Defense web UI with administrator role



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
        
        sudo systemctl status observiq-otel-collector
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/arbor_edge_defense:
                compression: gzip
                creds_file_path: '<PLACEHOLDER_CREDS_FILE_PATH>'
                customer_id: '<PLACEHOLDER_CUSTOMER_ID>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: ARBOR_EDGE_DEFENSE
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/arbor_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/arbor_edge_defense
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: UDP syslog receiver for NETSCOUT Arbor Edge Defense log forwarding
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
         




## Configure syslog export on NETSCOUT Arbor Edge Defense

  1. Sign in to the **NETSCOUT Arbor Edge Defense** web UI.
  2. Go to **Administration > Notifications > Notification Destinations**.
  3. Click **Add** to create a new syslog destination.
  4. Provide the following configuration details:

     * **Host** : Enter the IP address or hostname of the Bindplane agent host.
     * **Protocol** : Select **UDP**.
     * **Syslog Format** : Select **CEF**.
**Note:** The Legacy syslog format is not supported. Use CEF (Common Event Format) or LEEF (Log Event Extended Format).
  5. Click **Save**.

  6. Click **Config Commit** to apply the configuration changes.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`src_ip` | `principal.ip` | The value is taken from the `src_ip` field.  
`src_port` | `principal.port` | The value is taken from the `src_port` field and converted to an integer.  
`dst_ip` | `target.ip` | The value is taken from the `dst_ip` field.  
`dst_port` | `target.port` | The value is taken from the `dst_port` field and converted to an integer.  
`protocol` | `network.ip_protocol` | The value is taken from the `protocol` field and mapped to the IP protocol.  
`action` | `security_result.action` | Mapped based on the action: `blocked` maps to `BLOCK`, `passed` maps to `ALLOW`.  
`alert_type` | `security_result.category_details` | The value is taken from the `alert_type` field.  
`severity` | `security_result.severity` | Mapped based on the severity level.  
`description` | `metadata.description` | The value is taken from the `description` field.  
| `metadata.event_type` | Derived from available fields: `NETWORK_CONNECTION` if source and destination IP are present; otherwise `GENERIC_EVENT`.  
| `metadata.product_name` | Set to `Arbor Edge Defense`.  
| `metadata.vendor_name` | Set to `NETSCOUT`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arbor-edge-defense-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
