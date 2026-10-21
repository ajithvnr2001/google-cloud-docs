---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-edgeconnect-sdwan/
title: Collect Aruba EdgeConnect SD-WAN logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:30:42.046072+00:00
---

# Collect Aruba EdgeConnect SD-WAN logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-edgeconnect-sdwan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Aruba EdgeConnect SD-WAN logs

**Parser Version:** 6.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Aruba EdgeConnect SD-WAN logs to Google Security Operations using the Bindplane agent.

The Aruba EdgeConnect SD-WAN platform generates syslog messages for network traffic flows, security events, and system operations. The parser handles both key-value and unstructured syslog formats and maps extracted fields to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Aruba EdgeConnect appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Aruba Central or SD-WAN Orchestrator



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
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/aruba_edgeconnect_sdwan:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: ARUBA_EDGECONNECT_SDWAN
                raw_log_field: body
        
        service:
            pipelines:
                logs/aruba_edgeconnect_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/aruba_edgeconnect_sdwan
        




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
             




## Configure syslog in Aruba Central

  1. Sign in to the **Aruba Central** web UI.
  2. Go to **Manage > Devices > Gateways**.
  3. Select a **Gateway** under **Device Name**. The dashboard context for the gateway device is displayed.
  4. In **Manage** , click **Device**. The gateway configuration page is displayed.
  5. Click **System > Logging**.
  6. Click **+** in the **Syslog Servers** section.
  7. Provide the following configuration details: 
     * **IP address** : Enter the Bindplane agent IP address.
     * **Category** : Select **security** (you can repeat the process later to add other categories).
     * **Logging facility** : Select **Local0**.
     * **Logging level** : Select **Informational**.
     * **Format** : Select **cef**.
  8. Click **Save Settings**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`Action` | `security_result.action_details` | Directly mapped from the `Action` field.  
`Application` | `network.application_protocol` | If the `Application` field contains "dhcp" (case-insensitive), the value is set to "DHCP".  
`Application` | `intermediary.application` | Directly mapped from the `Application` field.  
`Direction` | `network.direction` | Directly mapped from the `Direction` field, converted to uppercase. If the value is not "INBOUND", "OUTBOUND", or "BROADCAST", it's set to "UNKNOWN_DIRECTION".  
`DstAddr` | `target.ip` | Directly mapped from the `DstAddr` field.  
`DstPort` | `target.port` | Directly mapped from the `DstPort` field, converted to an integer.  
`Flow-ID` | `metadata.id` | Directly mapped from the `Flow-ID` field.  
`FromZone` | `target.resource.attribute.labels` | Creates a label with key "FromZone" and value from the `FromZone` field.  
`Host` | `intermediary.hostname` | Directly mapped from the `Host` field.  
`Protocol` | `network.ip_protocol` | Directly mapped from the `Protocol` field, converted to uppercase, and then parsed using an include file (`parse_ip_protocol.include`) to get the protocol name.  
`Reason` | `security_result.category_details` | Directly mapped from the `Reason` field.  
`Reason` | `security_result.category` | If the `Reason` field contains "policy deny", the value is set to "POLICY_VIOLATION".  
`SrcAddr` | `principal.ip` | Directly mapped from the `SrcAddr` field.  
`SrcPort` | `principal.port` | Directly mapped from the `SrcPort` field, converted to an integer.  
`Tag` | `security_result.rule_name` | Directly mapped from the `Tag` field.  
`ToZone` | `target.resource.attribute.labels` | Creates a label with key "ToZone" and value from the `ToZone` field.  
`description` | `metadata.description` | Directly mapped from the `description` field, which is extracted from the log message when the `kv_data` field is empty.  
`intermediary_pid` | `intermediary.process.pid` | Directly mapped from the `intermediary_pid` field.  
`timestamp` | `metadata.event_timestamp` | Directly mapped from the `timestamp` field extracted from the log message. Set to "NETWORK_CONNECTION" if both `SrcAddr` and `DstAddr` are present, otherwise set to "GENERIC_EVENT". Hardcoded to "ARUBA_EDGECONNECT_SDWAN". Hardcoded to "ARUBA_EDGECONNECT_SDWAN".  
`IPTos` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tcpFlags` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`OutputInt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`InputInt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ingressVrfId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`egressVrfId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vrfName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Overlay` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`proc` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rxOctets` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`txOctets` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`flowId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cpu_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`thread_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`startTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`endTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rxPkts` | `event.idm.read_only_udm.network.received_packets` | Mapped from changelog  
`txPkts` | `event.idm.read_only_udm.network.sent_packets` | Mapped from changelog  
`tid` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`userDevice` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`dstRole` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`userName` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`srcRole` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`host` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`Action` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`src_host` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`target_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`dns_questions` | `event.idm.read_only_udm.network.dns.questions` | Mapped from changelog  
`product_event_type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`principal_ip` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`principal_ip` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`column1_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column2_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column3_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column4_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column5_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column6_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column7_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column8_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column9_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column10_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column11_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column12_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column13_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column14_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column15_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column16_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column17_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column18_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column19_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column20_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column21_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column22_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column23_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column24_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column25_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column26_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column27_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column28_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column29_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column30_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column31_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column32_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column33_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column34_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column35_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column36_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column37_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column38_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column39_tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column1_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column2_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column2_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column3_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column3_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column4_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column4_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column5_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column5_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column6_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column6_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column7_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column7_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column8_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column8_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column9_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column9_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column10_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column10_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column11_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column11_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column12_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column12_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column13_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column13_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column14_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column14_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column15_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column15_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column16_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column16_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column17_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column17_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column18_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column18_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column19_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column19_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column20_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column20_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column21_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column21_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column22_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column22_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column23_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column23_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column24_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column24_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column25_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column25_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column26_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column26_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column27_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column27_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column28_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column28_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column29_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column29_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column30_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column30_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column31_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column31_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column32_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column32_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column33_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column33_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column34_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column34_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column35_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column35_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column36_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column36_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column37_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column37_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column38_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column38_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column39_variable1` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column39_variable2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column1_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column2_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column3_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column3_dst_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column4_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column5_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column6_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column7_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column8_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column9_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column10_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column11_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column12_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column13_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column14_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column15_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column16_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column17_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column18_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column19_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column20_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column21_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column22_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column23_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column24_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column25_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column26_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column27_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column28_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column29_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column30_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column31_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column32_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column33_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column34_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column35_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column36_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column37_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column38_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column39_src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column1_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column2_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column4_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column5_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column6_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column7_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column8_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column9_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column10_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column11_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column12_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column13_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column14_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column15_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column16_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column17_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column18_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column19_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column20_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column21_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column22_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column23_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column24_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column25_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column26_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column27_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column28_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column29_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column30_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column31_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column32_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column33_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column34_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column35_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column36_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column37_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column38_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column39_dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column1_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column2_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column3_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column4_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column5_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column6_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column7_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column8_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column9_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column10_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column11_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column12_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column13_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column14_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column15_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column16_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column17_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column18_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column19_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column20_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column21_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column22_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column23_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column24_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column25_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column26_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column27_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column28_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column29_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column30_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column31_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column32_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column33_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column34_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column35_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column36_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column37_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column38_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column39_tunnel_interface` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`log_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog_ver` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`meta_sequenceId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sp_id` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`component` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`isInSync_` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`p_meta_sequenceId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`result` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`p_sp_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`p_service` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Registered_events` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`UniqueConfigEventsToSync` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`canRecoverConfigEvents` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`firstConfig_changeSet` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`firstConfig_config` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`firstConfig_state` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`lastConfig_changeSet` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`lastConfig_config` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`lastConfig_state` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`isInSync` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`UniqueStateEventsToSync` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`canRecoverStateEvents` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`firstState_baseUrl` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`firstState_config` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`firstState_state` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`firstState_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`lastState_config` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`lastState_state` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`duration` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`config_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`log_level_num` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`nepk` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`firstState_url` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`lastState_changeSet` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`lastState_baseUrl` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`lastState_url` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`lastState_op` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`lastState_serial` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`lastState_name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`name` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`taskStatus` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`logLevel` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`firstConfig_baseUrl` | `event.idm.read_only_udm.about.resource.name` | Mapped from changelog  
`firstConfig_url` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`firstConfig_op` | `event.idm.read_only_udm.about.labels` | Mapped from changelog  
`firstConfig_serial` | `event.idm.read_only_udm.about.labels` | Mapped from changelog  
`lastConfig_baseUrl` | `event.idm.read_only_udm.about.labels` | Mapped from changelog  
`lastConfig_url` | `event.idm.read_only_udm.about.labels` | Mapped from changelog  
`lastConfig_op` | `event.idm.read_only_udm.about.labels` | Mapped from changelog  
`lastConfig_serial` | `event.idm.read_only_udm.about.labels` | Mapped from changelog  
`firstState_changeSet` | `event.idm.read_only_udm.about.labels` | Mapped from changelog  
`firstState_op` | `event.idm.read_only_udm.about.labels` | Mapped from changelog  
`firstState_serial` | `event.idm.read_only_udm.about.labels` | Mapped from changelog  
`OnGms_1` | `event.idm.read_only_udm.about.labels` | Mapped from changelog  
`OnApp_1` | `event.idm.read_only_udm.about.labels` | Mapped from changelog  
`Diff_1` | `event.idm.read_only_udm.about.labels` | Mapped from changelog  
`summary` | `security_result.summary` | Mapped from changelog  
`userid` | `principal.user.userid` | Mapped from changelog  
`hostname` | `target.hostname` | Mapped from changelog  
`command` | `principal.process.command_line` | Mapped from changelog  
`principal_ip` | `principal.asset.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-edgeconnect-sdwan-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
