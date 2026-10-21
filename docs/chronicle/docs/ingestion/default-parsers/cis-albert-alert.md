---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cis-albert-alert/
title: Collect CIS Albert alert logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:51:58.331142+00:00
---

# Collect CIS Albert alert logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cis-albert-alert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CIS Albert alert logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest CIS Albert alert logs to Google Security Operations using the Bindplane agent.

CIS Albert is a managed intrusion detection service from the Center for Internet Security (CIS) designed for state, local, tribal, and territorial (SLTT) government organizations. Albert sensors monitor network traffic and generate alerts about malicious activity, including IP-based and DNS-based threat detection with an average SOC response time of under five minutes.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the CIS Albert sensor
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * An active CIS Albert subscription with access to the CIS Portal
  * Privileged access to configure syslog forwarding on the Albert sensor or CIS Portal



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
            chronicle/cis_albert:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: CIS_ALBERT_ALERT
                raw_log_field: body
        
        service:
            pipelines:
                logs/cis_albert_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/cis_albert
        




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
             




## Configure CIS Albert syslog forwarding

Albert sensors generate alerts that are analyzed by the CIS Security Operations Center (SOC). To forward these alerts to the Bindplane agent, coordinate with CIS to configure syslog output from your Albert sensor.

  1. Sign in to the [CIS Portal](https://www.cisecurity.org/).
  2. Navigate to **My Organization > Manage Products, Services and Resources**.
  3. Contact CIS SOC to request syslog forwarding configuration for your Albert sensor.
  4. Provide the following details to the CIS SOC: 
     * **Syslog Server** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514`.
     * **Protocol** : Select **UDP**.
     * **Format** : Request **BSD** (RFC 3164) syslog format.
  5. Request that all alert categories are forwarded, including: 
     * IP-based alerts
     * DNS-based alerts
     * SOC alert notifications
  6. Verify logs are being received by checking the Bindplane agent logs.

**Note:** Albert is a managed IDS service. Syslog forwarding configuration may require coordination with the CIS SOC team. Each Albert subscription includes 32 ANET query credits per month for querying historical data.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
sensor | intermediary.hostname | Value copied directly  
description | metadata.description | Value copied directly  
event_id, has_principal, has_target, sourceip, src_ip | metadata.event_type | Set based on event_id values or presence of principals/targets  
event_id | metadata.product_log_id | Value copied directly, converted to string  
target_port | network.application_protocol | Set to "HTTP" if target_port == 80, "HTTPS" if == 443  
analisys_extension | network.http.user_agent | Extracted from analisys_extension using grok pattern  
protocol | network.ip_protocol | Value copied directly  
hostname | observer.hostname | Value copied directly  
src_ip, sourceip | principal.asset.ip | Value from src_ip if not empty, else sourceip  
sensor | principal.hostname | Value copied directly  
src_ip, sourceip | principal.ip | Value from src_ip if not empty, else sourceip  
principal_port | principal.port | Value copied directly, converted to integer  
logical_sensor_id | principal.resource.id | Value copied directly  
category | security_result.category | Value from category, set based on event_id  
analysis | security_result.description | Value copied directly  
queue, activity_summary, siem_event_id, previous_escalations, status | security_result.detection_fields | Merged from labels created from queue, activity_summary, siem_event_id, previous_escalations, status  
severity, event_id | security_result.severity | Set based on severity value or event_id  
description | security_result.summary | Value copied directly  
analisys_extension | security_result.threat_id | Extracted from analisys_extension using grok pattern  
description, threat_name | security_result.threat_name | Value from threat_name if extracted, else description  
extension, analisys_extension | security_result.url_back_to_product | Constructed from extracted URL  
target_ip | target.asset.ip | Value copied directly  
target_hostname | target.hostname | Value copied directly  
target_ip | target.ip | Value copied directly  
target_port | target.port | Value copied directly, converted to integer  
| metadata.vendor_name | Set to "CIS"  
| metadata.product_name | Set to "Albert"  
`sourceip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`sourceip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`description` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`event_id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`queue` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`activity_summary` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`siem_event_id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`previous_escalations` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`status` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`logical_sensor_id` | `event.idm.read_only_udm.principal.resource.id` | Mapped from changelog  
`analysis` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cis-albert-alert-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
