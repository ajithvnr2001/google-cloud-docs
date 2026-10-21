---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ordr-iot/
title: Collect Ordr IoT logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:34:13.993152+00:00
---

# Collect Ordr IoT logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ordr-iot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Ordr IoT logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Ordr SCE logs to Google Security Operations using Bindplane.

Ordr Systems Control Engine (SCE) is a connected device security platform that provides visibility and threat detection across IoT, OT, and IoMT devices. It supports forwarding security alerts, device events, and alarm data to external SIEM platforms via syslog in CEF (Common Event Format). Ordr was acquired by Palo Alto Networks in 2024.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Ordr SCE appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Ordr SCE management console with administrator permissions



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
            chronicle/ordr_iot:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: ORDR_IOT
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/ordr_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/ordr_iot
        




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

    * `ordr_iot`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `ORDR_IOT`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `ordr_to_chronicle`: Descriptive name for the pipeline



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
         




## Configure Ordr SCE syslog forwarding

  1. Sign in to the **Ordr SCE** management console with administrator credentials.
  2. Go to **Settings > Integrations > SIEM**.
  3. Click **Add** or **Configure** to set up a new syslog integration.
  4. Provide the following configuration details: 
     * **Syslog Server IP/Hostname** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (must match the Bindplane agent receiver port).
     * **Protocol** : Select **UDP** (must match the Bindplane agent receiver type).
     * **Format** : Select **CEF** (Common Event Format).
  5. Select the event types to forward (for example, alarms, security events, device classification events).
  6. Click **Save** to apply the configuration.
  7. Verify that syslog messages are being received by checking the Bindplane agent logs.

**Note:** Ordr SCE also integrates with Splunk, QRadar, and other SIEM platforms directly. Check the Ordr integrations page for platform-specific connectors. Refer to updated Palo Alto Networks documentation for the latest integration options.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
additional_alarmHash, additional_connectionState, additional_reference | additional.fields | Additional metadata fields not covered by the UDM schema.  
deviceDescr, desc | metadata.description | Description of the event.  
has_principal, has_target | metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION).  
eventType | metadata.product_event_type | Product-specific event type.  
protocol | network.ip_protocol | IP protocol used in the network connection.  
principal | principal | The principal entity involved in the event.  
deviceType | principal.asset.category | Category of the asset.  
modelNameNo, manufacturer, mfgName | principal.asset.hardware | Hardware information for the asset.  
fqdn, deviceName | principal.asset.hostname | Hostname of the asset.  
ipAddress, srcIp | principal.asset.ip | IP address of the asset.  
fqdn, deviceName | principal.hostname | Hostname associated with the principal.  
ipAddress, srcIp | principal.ip | IP address associated with the principal.  
srcHost, srcMac, deviceId, equipMac, clientId | principal.mac | MAC address associated with the principal.  
osType | principal.platform | Operating system platform.  
osVersion | principal.platform_version | Version of the operating system platform.  
srcPort | principal.port | Port number associated with the principal.  
groupList, deviceGroup | principal.user.group_identifiers | List of group identifiers for the user.  
alarmType, alarmCategory, riskState, level, severityLevel | security_result | Security result information.  
dstHost | target.asset.hostname | Hostname of the target asset.  
dstIp, ip | target.asset.ip | IP address of the target asset.  
dstHost | target.hostname | Hostname of the target.  
dstIp, ip | target.ip | IP address of the target.  
dstPort | target.port | Port number of the target.  
| metadata.vendor_name | Vendor/company name.  
| metadata.product_name | Product name.  
`timestamp` | `metadata.event_timestamp` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ordr-iot-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
