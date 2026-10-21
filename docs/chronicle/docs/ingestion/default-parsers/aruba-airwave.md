---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-airwave/
title: Collect Aruba AirWave logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:30.082507+00:00
---

# Collect Aruba AirWave logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-airwave/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Aruba AirWave logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Aruba AirWave logs to Google Security Operations using the Bindplane agent.

Aruba AirWave is an on-premises wireless management platform developed by HPE Aruba Networking. It provides centralized monitoring, configuration, and troubleshooting for wired and wireless network infrastructure, including access points, controllers, and switches. AirWave generates event logs, audit logs, and RAPIDS (Rogue Access Point Detection Software) alerts that capture network operations, administrative actions, and security events.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Aruba AirWave server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Aruba AirWave Management Platform with administrator credentials
  * UDP port 514 open between the AirWave server and the Bindplane agent host



## Get a Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



## Get a Google SecOps customer ID

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
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/aruba_airwave:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: ARUBA_AIRWAVE
                raw_log_field: body
        
        service:
            pipelines:
                logs/aruba_airwave:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/aruba_airwave
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
      * `syslog` for RFC 3164/5424 syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `<customer_id>`: Customer ID from the earlier step
    * `malachiteingestion-pa.googleapis.com`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * Adjust the `creds_file_path` depending on the platform: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`



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
             




## Configure Aruba AirWave syslog forwarding

Configure the Aruba AirWave Management Platform to forward event and audit logs to the Bindplane agent using the built-in External Logging feature.

  1. Sign in to the **Aruba AirWave Management Platform** web interface.
  2. Go to **AMP Setup > General**.
  3. Scroll down to the **External Logging** section.
  4. In the **Syslog Server** field, enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
  5. In the **Syslog Port** field, enter `514`.

**Note:** The port value must match the `listen_address` port configured in the Bindplane agent `config.yaml` file.
  6. In the **Include Event Log Messages** dropdown, select **Yes**.

  7. In the **Event Log Facility** dropdown, select a facility identifier (for example, `local0`).

**Note:** Facility identifiers `local0` through `local7` are available as custom identifiers. Avoid using `local5` because on some systems `ftpd` defaults to using this facility. Messages tagged with these identifiers can be sorted by the syslog server into separate log files.
  8. In the **Include Audit Log Messages** dropdown, select **Yes**.

  9. In the **Audit Log Facility** dropdown, select a different facility identifier from the Event Log Facility (for example, `local1`).

  10. Click **Send Test Message** to verify that the syslog server receives test messages from AirWave.

  11. Click **Save**.

**Note:** After saving, everything written to the AirWave Event Log and audit logs will be forwarded to the Bindplane agent. You can find the AirWave Event Log at **System > Event Log** in the AirWave web interface, and at `/var/log/amp_events` from the AirWave command line.



For more information, see the [Aruba AirWave Viewing Syslog Messages documentation](https://arubanetworking.hpe.com/techdocs/AirWave/82151/webhelp/Content/Getting%20Started/Chapter3_Monitoring/Viewing_Syslog_Msgs.htm).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`column3_label` | `additional.fields` | Merged  
`version_label` | `additional.fields` | Merged  
`inter_host` | `intermediary.asset.hostname` | Directly mapped  
`inter_host` | `intermediary.hostname` | Directly mapped  
`description` | `metadata.description` | Directly mapped  
`entry.eap_friendly_name` | `metadata.description` | Renamed/mapped  
`msg` | `metadata.description` | Directly mapped  
`datestamp` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss`  
`entry.timestamp` | `metadata.event_timestamp` | Parsed as `MM/dd/yyyy HH:mm:ss.SSS`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`session_status` | `metadata.event_type` | Mapped: `opened` → `USER_LOGIN`, `closed` → `USER_LOGOUT`  
`device_event_class_id` | `metadata.product_event_type` | Directly mapped  
`event_name_1` | `metadata.product_event_type` | Directly mapped  
`device_product` | `metadata.product_name` | Directly mapped  
`entry.event_source` | `metadata.product_name` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`device_vendor` | `metadata.vendor_name` | Directly mapped  
`domain` | `principal.administrative_domain` | Directly mapped  
`hostname` | `principal.asset.hostname` | Directly mapped  
`column4` | `principal.asset.ip` | Merged  
`hostname` | `principal.hostname` | Directly mapped  
`column4` | `principal.ip` | Merged  
`entry.client_ip` | `principal.ip` | Merged  
`prin_ip` | `principal.ip` | Merged  
`entry.calling_station_id` | `principal.mac` | Merged  
`pid1` | `principal.process.pid` | Directly mapped  
`nas_port_label` | `principal.user.attribute.labels` | Merged  
`credentials` | `principal.user.user_display_name` | Renamed/mapped  
`entry.user_name` | `principal.user.userid` | Renamed/mapped  
`suser` | `principal.user.userid` | Directly mapped  
`user_id` | `principal.user.userid` | Renamed/mapped  
`sr_category` | `security_result.category` | Merged  
`severity_value` | `security_result.severity` | Mapped: `"1", "2", "3"` → `INFORMATIONAL`, `4` → `ERROR`, `5` → `CRITICAL`  
`scan_type` | `security_result.summary` | Directly mapped  
`target_hostname` | `target.asset.hostname` | Directly mapped  
`entry.nas_id` | `target.hostname` | Renamed/mapped  
`target_hostname` | `target.hostname` | Directly mapped  
`target_name` | `target.hostname` | Renamed/mapped  
`entry.nas_ip` | `target.ip` | Merged  
`target_ip` | `target.ip` | Merged  
`mac_address` | `target.mac` | Merged  
`target_resource` | `target.resource.id` | Directly mapped  
`column6` | `target.resource.name` | Directly mapped  
`username` | `target.user.user_display_name` | Directly mapped  
`client_friendly_name` | `target.user.userid` | Renamed/mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_event_type` | Constant: `Access-Request`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-airwave-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
