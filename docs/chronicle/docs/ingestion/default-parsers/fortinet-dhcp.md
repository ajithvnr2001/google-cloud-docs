---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-dhcp/
title: Collect Fortinet DHCP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:05:13.748725+00:00
---

# Collect Fortinet DHCP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-dhcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fortinet DHCP logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Fortinet DHCP logs to Google Security Operations using the Bindplane agent.

Fortinet FortiGate DHCP server logs capture IP address assignments, lease events, and DHCP relay operations within FortiGate firewall infrastructure. The logs are generated in key-value format by the on-premises FortiGate appliance.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the FortiGate appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Fortinet FortiGate administrator interface



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
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi&quot; /quiet
         

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
            chronicle/fortinet_dhcp:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
            <    custome>r_id: 'customer_id'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: FORTINET_DHCP
                raw_log_field: body
        
        service:
            pipelines:
                logs/fortinet_dhcp_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/fortinet_dhcp
        




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
             




## Configure Fortinet FortiGate DHCP syslog forwarding

  1. Sign in to the **FortiGate** web interface.
  2. Go to **Log & Report > Log Settings**.
  3. Scroll down to the **Remote Logging and Archiving** section.
  4. Under **Send Logs to Syslog** , enable syslog forwarding.
  5. Provide the following configuration details: 
     * **IP Address/FQDN** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Minimum Log Level** : Select **Information** or **Notification**.
     * **Facility** : Select **local7**.
  6. Alternatively, configure syslog forwarding via FortiGate CLI:
         
         config log syslogd setting
             set status enable
             set server "<bindplane-ip>"
             set port 514
             set facility local7
             set source-ip ""
             set format default
         end
         

     * Replace `<bindplane-ip>` with the IP address of the Bindplane agent host.
  7. To ensure DHCP logs are included, verify the log filter settings:
         
         config log syslogd filter
             set severity information
             set forward-traffic enable
             set local-traffic enable
             set event enable
         end
         

  8. Verify that logs are being sent by checking the Bindplane agent logs.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`appcat_label` | `additional.fields` | Merged  
`received_packets_field` | `additional.fields` | Merged  
`sent_packets_field` | `additional.fields` | Merged  
`host_name` | `intermediary.hostname` | Directly mapped  
`description` | `metadata.description` | Directly mapped  
`logdesc` | `metadata.description` | Directly mapped  
`msg` | `metadata.description` | Directly mapped  
`subtype` | `metadata.description` | Directly mapped  
`type` | `metadata.description` | Directly mapped  
`logtime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`event_type` | `metadata.event_type` | Renamed/mapped  
`subtype` | `metadata.product_event_type` | Directly mapped  
`type` | `metadata.product_event_type` | Directly mapped  
`logid` | `metadata.product_log_id` | Directly mapped  
`logdesc` | `network.application_protocol` | Mapped: `Release/Ack` → `DHCP`  
`service` | `network.application_protocol` | Directly mapped  
`mac` | `network.dhcp.chaddr` | Directly mapped  
`ip` | `network.dhcp.ciaddr` | Directly mapped  
`lease` | `network.dhcp.lease_time_seconds` | Renamed/mapped  
`logdesc` | `network.dhcp.type` | Mapped: `Ack` → `ACK`, `Release` → `RELEASE`  
`ip` | `network.dhcp.yiaddr` | Directly mapped  
`direction` | `network.direction` | Mapped: `"incoming", "inbound"` → `INBOUND`, `"outgoing", "outbound"` → `OUTBOUND`  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`rcvdbyte` | `network.received_bytes` | Renamed/mapped  
`sentbyte` | `network.sent_bytes` | Renamed/mapped  
`duration` | `network.session_duration.seconds` | Directly mapped  
`sessionid` | `network.session_id` | Directly mapped  
`hostname` | `principal.hostname` | Directly mapped  
`interface` | `principal.hostname` | Directly mapped  
`ip` | `principal.ip` | Merged  
`srcip` | `principal.ip` | Merged  
`srccountry` | `principal.location.country_or_region` | Directly mapped  
`mac` | `principal.mac` | Merged  
`srcport` | `principal.port` | Directly mapped  
`devid` | `principal.resource.id` | Directly mapped  
`devname` | `principal.resource.name` | Directly mapped  
`srcuuid` | `principal.user.product_object_id` | Directly mapped  
`user_name` | `principal.user.user_display_name` | Directly mapped  
`vd` | `principal.user.userid` | Directly mapped  
`security_result_action` | `security_result.action` | Merged  
`action` | `security_result.action_details` | Directly mapped  
`category_details` | `security_result.category_details` | Merged  
`craction_labels` | `security_result.detection_fields` | Merged  
`dstintf_labels` | `security_result.detection_fields` | Merged  
`dstintfrole_labels` | `security_result.detection_fields` | Merged  
`srcintf_label` | `security_result.detection_fields` | Merged  
`srcintfrole_label` | `security_result.detection_fields` | Merged  
`policyid` | `security_result.rule_id` | Directly mapped  
`policyname` | `security_result.rule_name` | Directly mapped  
`policytype` | `security_result.rule_type` | Directly mapped  
`level` | `security_result.severity` | Mapped: `information` → `INFORMATIONAL`  
`crscore` | `security_result.severity_details` | Directly mapped  
`level` | `security_result.severity_details` | Directly mapped  
`application` | `target.application` | Directly mapped  
`service` | `target.application` | Directly mapped  
`dstip` | `target.ip` | Merged  
`dstcountry` | `target.location.country_or_region` | Directly mapped  
`dstport` | `target.port` | Directly mapped  
`profile` | `target.resource.name` | Directly mapped  
`url` | `target.url` | Directly mapped  
`dstuuid` | `target.user.product_object_id` | Directly mapped  
N/A | `metadata.product_name` | Constant: `FORTINET_DHCP`  
N/A | `metadata.vendor_name` | Constant: `FORTINET`  
N/A | `network.application_protocol` | Constant: `DHCP`  
N/A | `network.dhcp.type` | Constant: `ACK`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `principal.resource.resource_type` | Constant: `DEVICE`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
N/A | `target.resource.resource_type` | Constant: `ACCESS_POLICY`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-dhcp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
