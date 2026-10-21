---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/versa-sase/
title: Collect Versa Networks Secure Access Service Edge (SASE) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:57:40.973801+00:00
---

# Collect Versa Networks Secure Access Service Edge (SASE) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/versa-sase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Versa Networks Secure Access Service Edge (SASE) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Versa Networks Secure Access Service Edge (SASE) logs to Google Security Operations using the Bindplane agent.

Versa Networks SASE is a unified security and networking platform that generates syslog messages for firewall events, threat logs, application classification, URL filtering, IDS/IPS detections, and alarm events. The parser extracts key-value pairs from syslog messages and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Versa Analytics node
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Versa SASE



## Get Google SecOps credentials for the Bindplane agent

To authenticate the Bindplane agent to Google SecOps, choose one of the following methods:

  * **New deployments** : Use the Chronicle API (Option 1).
  * **Legacy deployments** : Continue using the ingestion authentication file (Option 2) until the Ingestion API is discontinued on July 20, 2027.



### Option 1: Create a service account for the Chronicle API (recommended)

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/) and select the Google Cloud project that is linked to your Google SecOps instance.
  2. Go to **IAM & Admin > Service Accounts**.
  3. Click **Create service account**.
  4. Provide the following configuration details: 
     * **Service account name** : Enter a name for the account (for example, `bindplane-ingest`).
     * **Service account description** : Enter a description (for example, `Bindplane agent log ingestion`).
  5. Click **Create and continue**.
  6. In the **Grant this service account access to project** section, click **Select a role** and select **Chronicle Editor**.
  7. Click **Continue** , and then click **Done**.
  8. Click the service account you created, and then go to the **Keys** tab.
  9. Click **Add key > Create new key**.
  10. Select **JSON** and click **Create**. The key file is downloaded to your computer.
  11. Save the key file as `ingestion-auth.json` in the Bindplane collector directory (`/opt/observiq-otel-collector/ingestion-auth.json` on Linux or `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json` on Windows), or update `creds_file_path` in `config.yaml` to match the path where you save it.
  12. Go to **IAM & Admin > Settings** and copy the **Project number**. You'll need it for the exporter configuration.

**Note:** The JSON key is a credential. Restrict access to the file on the Bindplane host and rotate the key according to your organization's policy.

### Option 2: Download the ingestion authentication file (legacy)

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This file authenticates the agent to the legacy Ingestion API (`malachiteingestion-pa.googleapis.com`), which Google has scheduled for end of life on July 20, 2027. Plan to move to Option 1 before that date.

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

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/versa_firewall:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: VERSA_FIREWALL
            raw_log_field: body
        
        service:
          pipelines:
            logs/versa_firewall_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/versa_firewall
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
      * Versa uses TCP transport, so `tcplog` receiver is required
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/versa_firewall:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: VERSA_FIREWALL
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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
             




## Configure Versa Networks SASE

Administrators must configure remote collectors on each Versa Analytics node to forward logs to third-party systems.

### Enable log forwarding

  1. Sign in to the **Versa analytics server**.
  2. Go to **CLI** by running the `cli` command.
  3. Switch to **Configuration mode** by running the `configure` command, and then enter `load merge terminal`.
  4. Copy and paste the following commands to set up log forwarding (replace `<collector_ip>` and `<collector_port>` with the IP address and port of your syslog collector):
         
         set system analytics log-collector-exporter destination-address <collector_ip>
         set system analytics log-collector-exporter destination-port <collector_port>
         set system analytics log-collector-exporter transport tcp
         set system analytics log-collector-exporter log-types firewall-log
         set system analytics log-collector-exporter log-types threat-log
         commit
         

  5. Save the configuration:
         
         save
         

**Note:** If no log type is specified, it streams all log-type events.



### Enable session ID logging

To log IP-related information, enable session ID logging:

  1. Sign in to **Versa Director**.
  2. Switch to **Director View**.
  3. Go to **Configuration > Devices > Tenant > Device** to access **Appliance View**.
  4. Select **Configuration > Others > System > Configuration > Configuration**.
  5. In the **Parameters** pane, click **Edit**.
  6. In the **Edit parameters** window, select **LEF**.
  7. In the **Firewall** section, select the **Include session ID logging** checkbox.
  8. Click **OK**.

**Note:** In Releases 21.1.1 and newer, session identification is automatically enabled.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`accCkt` | `additional.fields[].key`: "accCkt"  
`additional.fields[].value.string_value`: `accCkt` | Value taken directly from the `accCkt` field.  
`accCktId` | `additional.fields[].key`: "accCktId"  
`additional.fields[].value.string_value`: `accCktId` | Value taken directly from the `accCktId` field.  
`accCktName` | `additional.fields[].key`: "accCktName"  
`additional.fields[].value.string_value`: `accCktName` | Value taken directly from the `accCktName` field.  
`accessType` | `additional.fields[].key`: "accessType"  
`additional.fields[].value.string_value`: `accessType` | Value taken directly from the `accessType` field.  
`action` | `security_result.action`: `action` | If `action`, `type`, `idpAction`, `avAction`, or `urlAction` are "allow" then `ALLOW`. If `action`, `type`, `idpAction`, `avAction`, or `urlAction` are "reject", "drop", "block", "deny" then `BLOCK`. If `idpAction` is anything else then `UNKNOWN_ACTION`.  
`alarmCause` | `security_result.detection_fields[].key`: "alarmCause"  
`security_result.detection_fields[].value`: `alarmCause` | Value taken directly from the `alarmCause` field.  
`alarmClass` | `security_result.detection_fields[].key`: "alarmClass"  
`security_result.detection_fields[].value`: `alarmClass` | Value taken directly from the `alarmClass` field.  
`alarmClearable` | `security_result.detection_fields[].key`: "alarmClearable"  
`security_result.detection_fields[].value`: `alarmClearable` | Value taken directly from the `alarmClearable` field.  
`alarmEventType` | `metadata.product_event_type`: `alarmEventType` | Value taken directly from the `alarmEventType` field.  
`alarmKey` | `security_result.detection_fields[].key`: "alarmKey"  
`security_result.detection_fields[].value`: `alarmKey` | Value taken directly from the `alarmKey` field.  
`alarmKind` | `security_result.detection_fields[].key`: "alarmKind"  
`security_result.detection_fields[].value`: `alarmKind` | Value taken directly from the `alarmKind` field.  
`alarmOwner` | `security_result.detection_fields[].key`: "alarmOwner"  
`security_result.detection_fields[].value`: `alarmOwner` | Value taken directly from the `alarmOwner` field.  
`alarmSeqNo` | `security_result.detection_fields[].key`: "alarmSeqNo"  
`security_result.detection_fields[].value`: `alarmSeqNo` | Value taken directly from the `alarmSeqNo` field.  
`alarmSeverity` | `security_result.severity_details`: `alarmSeverity` | Value taken directly from the `alarmSeverity` field.  
`alarmText` | `security_result.summary`: `alarmText` | Value taken directly from the `alarmText` field, with double quotes removed.  
`alarmType` | `security_result.description`: `alarmType` | Value taken directly from the `alarmType` field.  
`appFamily` | `metadata.product_event_type`: `appFamily`  
`security_result.detection_fields[].key`: "appFamily"  
`security_result.detection_fields[].value`: `appFamily` | Value taken directly from the `appFamily` field.  
`appId` | `security_result.detection_fields[].key`: "Application ID"  
`security_result.detection_fields[].value`: `appId` | Value taken directly from the `appId` field.  
`appIdStr` | `security_result.detection_fields[].key`: "appIdStr"  
`security_result.detection_fields[].value`: `appIdStr` | Value taken directly from the `appIdStr` field.  
`applianceName` | `principal.hostname`: `applianceName` | Value taken directly from the `applianceName`, `siteName`, or `site` field.  
`appProductivity` | `security_result.detection_fields[].key`: "appProductivity"  
`security_result.detection_fields[].value`: `appProductivity` | Value taken directly from the `appProductivity` field.  
`appRisk` | `security_result.severity_details`: `appRisk` | Value taken directly from the `appRisk` field.  
`appSubFamily` | `security_result.detection_fields[].key`: "appSubFamily"  
`security_result.detection_fields[].value`: `appSubFamily` | Value taken directly from the `appSubFamily` field.  
`avAccuracy` | `additional.fields[].key`: "avAccuracy"  
`additional.fields[].value.string_value`: `avAccuracy` | Value taken directly from the `avAccuracy` field.  
`avAction` | `security_result.action`: `avAction` | See `action` for logic.  
`avMalwareName` | `security_result.threat_name`: `avMalwareName` | Value taken directly from the `avMalwareName` field.  
`avMalwareType` | `security_result.category_details`: `avMalwareType` | Value taken directly from the `avMalwareType` field.  
`classMsg` | `security_result.description`: `classMsg` | Value taken directly from the `classMsg` field, with double quotes removed.  
`clientIPv4Address` | `target.ip`: `clientIPv4Address` | Value taken directly from the `clientIPv4Address` field.  
`destIp` | `target.ip`: `destIp`  
`destinationIPv4Address`: `destIp` | Value taken directly from the `destIp` field.  
`destinationIPv4Address` | `target.ip`: `destinationIPv4Address` | Value taken directly from the `destinationIPv4Address` or derived from `networkPrefix` field.  
`destinationIPv6Address` | `target.ip`: `destinationIPv6Address` | Value taken directly from the `destinationIPv6Address` field.  
`destinationPort` | `target.port`: `destinationPort` | Value taken directly from the `destinationPort` field and converted to integer.  
`destinationTransportPort` | `target.port`: `destinationTransportPort` | Value taken directly from the `destinationTransportPort` field and converted to integer.  
`deviceKey` | `about.resource.attribute.labels[].key`: "deviceKey"  
`about.resource.attribute.labels[].value`: `deviceKey` | Value taken directly from the `deviceKey` field if not "Unknown".  
`deviceName` | `about.resource.attribute.labels[].key`: "deviceName"  
`about.resource.attribute.labels[].value`: `deviceName` | Value taken directly from the `deviceName` field if not "Unknown".  
`duration` | `network.session_duration.seconds`: `duration` | Value taken directly from the `duration` field and converted to integer.  
`egressInterfaceName` | `additional.fields[].key`: "egressInterfaceName"  
`additional.fields[].value.string_value`: `egressInterfaceName` | Value taken directly from the `egressInterfaceName` field.  
`event.type` | `metadata.event_type`: `event.type` | If both `applianceName` (or `sourceIPv4Address` or `user` or `sourceIPv6Address`) and `destinationIPv4Address` (or `remoteSite` or `destinationIPv6Address` or `clientIPv4Address` or `hostname`) are present, then `NETWORK_CONNECTION`. Otherwise, `STATUS_UPDATE`. If `applianceName` is empty, then `GENERIC_EVENT`.  
`eventType` | `principal.resource.attribute.labels[].key`: "eventType"  
`principal.resource.attribute.labels[].value`: `eventType` | Value taken directly from the `eventType` field.  
`family` | `security_result.detection_fields[].key`: "family"  
`security_result.detection_fields[].value`: `family` | Value taken directly from the `family` field.  
`fc` | `security_result.detection_fields[].key`: "ForwardingClass"  
`security_result.detection_fields[].value`: `fc` | Value taken directly from the `fc` field.  
`fileTransDir` | `additional.fields[].key`: "fileTransDir"  
`additional.fields[].value.string_value`: `fileTransDir` | Value taken directly from the `fileTransDir` field.  
`filename` | `target.file.names`: `filename` | Value taken directly from the `filename` field.  
`flowCookie` | `metadata.collected_timestamp`: `flowCookie` | Value taken directly from the `flowCookie` field and converted to timestamp using UNIX format.  
`flowId` | `principal.resource.product_object_id`: `flowId` | Value taken directly from the `flowId` field.  
`forwardForwardingClass` | `security_result.detection_fields[].key`: "forwardForwardingClass"  
`security_result.detection_fields[].value`: `forwardForwardingClass` | Value taken directly from the `forwardForwardingClass` field.  
`fromCountry` | `principal.location.country_or_region`: `fromCountry`  
`target.location.country_or_region`: `fromCountry` | Value taken directly from the `fromCountry` field.  
`fromUser` | `principal.user.userid`: `fromUser` | Value taken directly from the `fromUser` field if not empty, "unknown", or "Unknown".  
`fromZone` | `additional.fields[].key`: "fromZone"  
`additional.fields[].value.string_value`: `fromZone` | Value taken directly from the `fromZone` field.  
`generateTime` | `metadata.collected_timestamp`: `generateTime` | Value taken directly from the `generateTime` field and converted to timestamp using UNIX format.  
`hostname` | `target.hostname`: `hostname` | Value taken directly from the `hostname` field.  
`httpUrl` | `target.url`: `httpUrl` | Value taken directly from the `httpUrl` field.  
`icmpTypeIPv4` | `additional.fields[].key`: "icmpTypeIPv4"  
`additional.fields[].value.string_value`: `icmpTypeIPv4` | Value taken directly from the `icmpTypeIPv4` field.  
`idpAction` | `security_result.action`: `idpAction` | See `action` for logic.  
`ingressInterfaceName` | `additional.fields[].key`: "ingressInterfaceName"  
`additional.fields[].value.string_value`: `ingressInterfaceName` | Value taken directly from the `ingressInterfaceName` field.  
`ipsApplication` | `additional.fields[].key`: "ipsApplication"  
`additional.fields[].value.string_value`: `ipsApplication` | Value taken directly from the `ipsApplication` field.  
`ipsDirection` | `security_result.detection_fields[].key`: "ipsDirection"  
`security_result.detection_fields[].value`: `ipsDirection` | Value taken directly from the `ipsDirection` field.  
`ipsProfile` | `security_result.detection_fields[].key`: "ipsProfile"  
`security_result.detection_fields[].value`: `ipsProfile` | Value taken directly from the `ipsProfile` field.  
`ipsProfileRule` | `security_result.rule_name`: `ipsProfileRule` | Value taken directly from the `ipsProfileRule` field.  
`ipsProtocol` | `network.ip_protocol`: `ipsProtocol` | Value taken directly from the `ipsProtocol` field.  
`log_type` | `metadata.description`: `log_type`  
`metadata.log_type`: `log_type` | Value taken directly from the `log_type` field.  
`mstatsTimeBlock` | `metadata.collected_timestamp`: `mstatsTimeBlock` | Value taken directly from the `mstatsTimeBlock` field and converted to timestamp using UNIX format.  
`mstatsTotRecvdOctets` | `network.received_bytes`: `mstatsTotRecvdOctets` | Value taken directly from the `mstatsTotRecvdOctets` field and converted to unsigned integer.  
`mstatsTotSentOctets` | `network.sent_bytes`: `mstatsTotSentOctets` | Value taken directly from the `mstatsTotSentOctets` field and converted to unsigned integer.  
`mstatsTotSessCount` | `additional.fields[].key`: "mstatsTotSessCount"  
`additional.fields[].value.string_value`: `mstatsTotSessCount` | Value taken directly from the `mstatsTotSessCount` field.  
`mstatsTotSessDuration` | `network.session_duration.seconds`: `mstatsTotSessDuration` | Value taken directly from the `mstatsTotSessDuration` field and converted to integer.  
`mstatsType` | `security_result.category_details`: `mstatsType` | Value taken directly from the `mstatsType` field.  
`networkPrefix` | `target.ip`: `networkPrefix`  
`target.port`: `networkPrefix` | IP address extracted from the `networkPrefix` field. Port extracted from the `networkPrefix` field and converted to integer.  
`protocolIdentifier` | `network.ip_protocol`: `protocolIdentifier` | Value taken directly from the `protocolIdentifier` field, converted to integer, and mapped to IP protocol name using a lookup.  
`recvdOctets` | `network.received_bytes`: `recvdOctets` | Value taken directly from the `recvdOctets` field and converted to unsigned integer.  
`recvdPackets` | `network.received_packets`: `recvdPackets` | Value taken directly from the `recvdPackets` field and converted to integer.  
`remoteSite` | `target.hostname`: `remoteSite` | Value taken directly from the `remoteSite` field.  
`reverseForwardingClass` | `security_result.detection_fields[].key`: "reverseForwardingClass"  
`security_result.detection_fields[].value`: `reverseForwardingClass` | Value taken directly from the `reverseForwardingClass` field.  
`risk` | `security_result.risk_score`: `risk` | Value taken directly from the `risk` field and converted to float.  
`rule` | `security_result.rule_name`: `rule` | Value taken directly from the `rule` field.  
`sentOctets` | `network.sent_bytes`: `sentOctets` | Value taken directly from the `sentOctets` field and converted to unsigned integer.  
`sentPackets` | `network.sent_packets`: `sentPackets` | Value taken directly from the `sentPackets` field and converted to integer.  
`serialNum` | `security_result.detection_fields[].key`: "serialNum"  
`security_result.detection_fields[].value`: `serialNum` | Value taken directly from the `serialNum` field.  
`signatureId` | `security_result.detection_fields[].key`: "signatureID"  
`security_result.detection_fields[].value`: `signatureId` | Value taken directly from the `signatureId` field.  
`signatureMsg` | `security_result.detection_fields[].key`: "signatureMsg"  
`security_result.detection_fields[].value`: `signatureMsg` | Value taken directly from the `signatureMsg` field.  
`signaturePriority` | `security_result.severity`: `signaturePriority` | If `signaturePriority` is "low" (case-insensitive), then `LOW`. If `signaturePriority` is "medium" (case-insensitive), then `MEDIUM`. If `signaturePriority` is "high" (case-insensitive), then `HIGH`.  
`site` | `principal.hostname`: `site`  
`applianceName`: `site` | Value taken directly from the `site` field.  
`siteId` | `additional.fields[].key`: "siteId"  
`additional.fields[].value.string_value`: `siteId` | Value taken directly from the `siteId` field.  
`siteName` | `principal.hostname`: `siteName`  
`applianceName`: `siteName` | Value taken directly from the `siteName` field.  
`sourceIPv4Address` | `principal.ip`: `sourceIPv4Address` | Value taken directly from the `sourceIPv4Address` field.  
`sourceIPv6Address` | `principal.ip`: `sourceIPv6Address` | Value taken directly from the `sourceIPv6Address` field.  
`sourcePort` | `principal.port`: `sourcePort` | Value taken directly from the `sourcePort` field and converted to integer.  
`sourceTransportPort` | `principal.port`: `sourceTransportPort` | Value taken directly from the `sourceTransportPort` field and converted to integer.  
`subFamily` | `security_result.detection_fields[].key`: "subFamily"  
`security_result.detection_fields[].value`: `subFamily` | Value taken directly from the `subFamily` field.  
`tcpConnAborted` | `additional.fields[].key`: "tcpConnAborted"  
`additional.fields[].value.string_value`: `tcpConnAborted` | Value taken directly from the `tcpConnAborted` field if not empty or "0".  
`tcpConnRefused` | `additional.fields[].key`: "tcpConnRefused"  
`additional.fields[].value.string_value`: `tcpConnRefused` | Value taken directly from the `tcpConnRefused` field if not empty or "0".  
`tcpPktsFwd` | `network.sent_packets`: `tcpPktsFwd` | Value taken directly from the `tcpPktsFwd` field and converted to integer.  
`tcpPktsRev` | `network.received_packets`: `tcpPktsRev` | Value taken directly from the `tcpPktsRev` field and converted to integer.  
`tcpReXmitFwd` | `additional.fields[].key`: "tcpReXmitFwd"  
`additional.fields[].value.string_value`: `tcpReXmitFwd` | Value taken directly from the `tcpReXmitFwd` field if not empty or "0".  
`tcpReXmitRev` | `additional.fields[].key`: "tcpReXmitRev"  
`additional.fields[].value.string_value`: `tcpReXmitRev` | Value taken directly from the `tcpReXmitRev` field if not empty or "0".  
`tcpSAA` | `additional.fields[].key`: "tcpSAA"  
`additional.fields[].value.string_value`: `tcpSAA` | Value taken directly from the `tcpSAA` field if not empty or "0".  
`tcpSSA` | `additional.fields[].key`: "tcpSSA"  
`additional.fields[].value.string_value`: `tcpSSA` | Value taken directly from the `tcpSSA` field if not empty or "0".  
`tcpSessCnt` | `additional.fields[].key`: "tcpSessCnt"  
`additional.fields[].value.string_value`: `tcpSessCnt` | Value taken directly from the `tcpSessCnt` field.  
`tcpSessDur` | `network.session_duration.seconds`: `tcpSessDur` | Value taken directly from the `tcpSessDur` field and converted to integer.  
`tcpSynAckReXmit` | `additional.fields[].key`: "tcpSynAckReXmit"  
`additional.fields[].value.string_value`: `tcpSynAckReXmit` | Value taken directly from the `tcpSynAckReXmit` field if not empty or "0".  
`tcpSynReXmit` | `additional.fields[].key`: "tcpSynReXmit"  
`additional.fields[].value.string_value`: `tcpSynReXmit` | Value taken directly from the `tcpSynReXmit` field if not empty or "0".  
`tcpTWHS` | `additional.fields[].key`: "tcpTWHS"  
`additional.fields[].value.string_value`: `tcpTWHS` | Value taken directly from the `tcpTWHS` field if not empty or "0".  
`tenantId` | `principal.resource.attribute.labels[].key`: "tenantId"  
`principal.resource.attribute.labels[].value`: `tenantId` | Value taken directly from the `tenantId` field.  
`tenantName` | `observer.hostname`: `tenantName` | Value taken directly from the `tenantName` field.  
`threatType` | `security_result.detection_fields[].key`: "threatType"  
`security_result.detection_fields[].value`: `threatType` | Value taken directly from the `threatType` field.  
`toCountry` | `target.location.country_or_region`: `toCountry` | Value taken directly from the `toCountry` field.  
`toZone` | `additional.fields[].key`: "toZone"  
`additional.fields[].value.string_value`: `toZone` | Value taken directly from the `toZone` field.  
`traffType` | `additional.fields[].key`: "traffType"  
`additional.fields[].value.string_value`: `traffType` | Value taken directly from the `traffType` field.  
`ts` | `metadata.event_timestamp`: `ts` | Value taken directly from the `ts` field and converted to timestamp.  
`type` | `security_result.action`: `type` | See `action` for logic.  
`urlAction` | `security_result.action`: `urlAction` | See `action` for logic.  
`urlActionMessage` | `security_result.summary`: `urlActionMessage` | Value taken directly from the `urlActionMessage` field.  
`urlCategory` | `principal.resource.attribute.labels[].key`: "urlCategory"  
`principal.resource.attribute.labels[].value`: `urlCategory` | Value taken directly from the `urlCategory` field.  
`urlProfile` | `additional.fields[].key`: "urlProfile"  
`additional.fields[].value.string_value`: `urlProfile` | Value taken directly from the `urlProfile` field.  
`urlReputation` | `security_result.severity_details`: `urlReputation` | Value taken directly from the `urlReputation` field.  
`user` | `principal.ip`: `user` | Value taken directly from the `user` field.  
`vsnId` | `principal.resource.attribute.labels[].key`: "vsnId"  
`principal.resource.attribute.labels[].value`: `vsnId` | Value taken directly from the `vsnId` field. Hardcoded value. Hardcoded value.  
`applianceName` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`postNATSourceIPv4Address` | `event.idm.read_only_udm.principal.nat_ip` | Mapped from changelog  
`postNATDestinationIPv4Address` | `event.idm.read_only_udm.target.nat_ip` | Mapped from changelog  
`postNAPTsourceTransportPort` | `event.idm.read_only_udm.principal.nat_port` | Mapped from changelog  
`postNAPTdestinationTransportPort` | `event.idm.read_only_udm.target.nat_port` | Mapped from changelog  
`natRuleName` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`natEvent` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`log_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`flowCookie` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`flowId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sourceNatPoolName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`destNatPoolName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`deviceKey` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`deviceName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`observationTimeMilliseconds` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`threatSeverity` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`dnsfBadCname` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`dnsfEvType` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`dnsfDomain` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`dnsfMsgType` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`dnsfProfileName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`dnsfIpReputation` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`dnsfAction` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`HitCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`groupId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`signatureRev` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`packetTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`moduleId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dnsfBadResolvedV4Addr` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`dnsfIpGeoLocation` | `event.idm.read_only_udm.target.location.country_or_region` | Mapped from changelog  
`sourceIPv4Address` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`destinationIPv4Address` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`host` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`eipProfileName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`traffScope` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`srcSGT` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`destSGT` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ucsBand` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ucsReason` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`urlLookupSrc` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`protocolInfo` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ecsBand` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ecsReason` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`appAuth` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ucsScore` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`policyActionName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`policyActionModule` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ecsScore` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`applianceId` | `event.idm.read_only_udm.intermediary.asset.product_object_id` | Mapped from changelog  
`inter_hostname` | `event.idm.ready_only_udm.intermediary.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/versa-firewall-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
