---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arcsight-cef/
title: Collect ArcSight CEF logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:51:22.725326+00:00
---

# Collect ArcSight CEF logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arcsight-cef/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ArcSight CEF logs

**Parser Version:** 34.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ArcSight CEF logs to Google Security Operations using Bindplane agent.

ArcSight (now part of OpenText) uses the Common Event Format (CEF) for normalizing security events from multiple sources. The ArcSight SmartConnector collects events and forwards them in CEF format via syslog to downstream consumers including SIEM platforms.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the ArcSight SmartConnector host
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Access to the OpenText support portal to download SmartConnector
  * Administrative access to the SmartConnector server



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
            chronicle/arcsight_cef:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: ARCSIGHT_CEF
                raw_log_field: body
        
        service:
            pipelines:
                logs/arcsight_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/arcsight_cef
        




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
             




## Download ArcSight SmartConnector

  1. Sign in to the **OpenText support portal**.
  2. Find and download the latest ArcSight SmartConnector for Linux.
  3. Example filename: `ArcSight-Connector-Linux64-8.4.0.8499.0.bin`.



## Install the ArcSight SmartConnector

  1. Upload the `.bin` file to the SmartConnector server:
         
         scp ArcSight-Connector-Linux64-8.4.0.8499.0.bin user@your-smartconnector-host:/tmp
         

  2. Sign in to the **SmartConnector** server using SSH and run:
         
         cd /tmp
         chmod +x ArcSight-Connector-Linux64-8.4.0.8499.0.bin
         ./ArcSight-Connector-Linux64-8.4.0.8499.0.bin
         

  3. Follow the interactive installer:

     * Select installation directory (for example, `/opt/arcsight/connectors/current`).
     * Accept the license.
     * Select **Install connector** when prompted.



## Configure ArcSight SmartConnector to send CEF to syslog

  1. In the **SmartConnector host** , launch the destination wizard:
         
         cd /opt/arcsight/connectors/current/bin
         ./arcsight connectors
         

  2. In the wizard, do the following:

     * Select **Add Destination**.
     * Select **CEF Syslog**.
  3. Provide the following configuration details:

     * **Host/IP** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (for example, `514`).
     * **Protocol** : Select **UDP**.
  4. Finish the setup and restart the connector:
         
         ./arcsight agents
         

  5. Run a check for connectivity (look for: `Successfully connected to syslog: X.X.X.X:514`):
         
         tail -f /opt/arcsight/connectors/current/logs/agent.log
         




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
act | security_result.action_details | Directly mapped from the `act` field.  
agt | principal.ip | Directly mapped from the `agt` field.  
agt | principal.asset.ip | Directly mapped from the `agt` field.  
app | network.application_protocol | Directly mapped from the `app` field.  
art | metadata.event_timestamp.seconds | Directly mapped from the `art` field.  
cs2 | additional.fields.value.string_value | Directly mapped from the `cs2` field when `cs2Label` is `EventlogCategory`.  
cs2Label | additional.fields.key | Directly mapped from the `cs2Label` field when its value is `EventlogCategory`.  
cs3 | additional.fields.value.string_value | Directly mapped from the `cs3` field when `cs3Label` is `Process ID`.  
cs3Label | additional.fields.key | Directly mapped from the `cs3Label` field when its value is `Process ID`.  
cs5 | additional.fields.value.string_value | Directly mapped from the `cs5` field when `cs5Label` is `Authentication Package Name`.  
cs5Label | additional.fields.key | Directly mapped from the `cs5Label` field when its value is `Authentication Package Name`.  
cs6 | additional.fields.value.string_value | Directly mapped from the `cs6` field when `cs6Label` is `Logon GUID`.  
cs6Label | additional.fields.key | Directly mapped from the `cs6Label` field when its value is `Logon GUID`.  
dhost | about.hostname | Directly mapped from the `dhost` field.  
dhost | target.hostname | Directly mapped from the `dhost` field.  
dntdom | about.administrative_domain | Directly mapped from the `dntdom` field.  
dntdom | target.administrative_domain | Directly mapped from the `dntdom` field.  
dproc | about.process.command_line | Directly mapped from the `dproc` field.  
dproc | target.process.command_line | Directly mapped from the `dproc` field.  
dst | principal.ip | Directly mapped from the `dst` field.  
dst | principal.asset.ip | Directly mapped from the `dst` field.  
dst | target.ip | Directly mapped from the `dst` field.  
duid | target.user.userid | Directly mapped from the `duid` field.  
duser | target.user.user_display_name | Directly mapped from the `duser` field.  
dvc | about.ip | Directly mapped from the `dvc` field.  
dvchost | about.hostname | Directly mapped from the `dvchost` field.  
eventId | additional.fields.value.string_value | Directly mapped from the `eventId` field.  
externalId | metadata.product_log_id | Directly mapped from the `externalId` field.  
fname | additional.fields.value.string_value | Directly mapped from the `fname` field.  
msg | metadata.description | Directly mapped from the `msg` field.  
proto | network.ip_protocol | Directly mapped from the `proto` field. Translates protocol names to their respective constants (e.g., `tcp` to `TCP`).  
rt | metadata.event_timestamp.seconds | Directly mapped from the `rt` field.  
shost | about.hostname | Directly mapped from the `shost` field.  
shost | principal.hostname | Directly mapped from the `shost` field.  
src | principal.ip | Directly mapped from the `src` field.  
src | principal.asset.ip | Directly mapped from the `src` field.  
src | target.ip | Directly mapped from the `src` field.  
sproc | principal.process.command_line | Directly mapped from the `sproc` field.  
spt | principal.port | Directly mapped from the `spt` field.  
spt | target.port | Directly mapped from the `spt` field.  
additional.EventRecordID | additional.fields.value.string_value | Directly mapped from the `ad.EventRecordID` field.  
additional.ThreadID | additional.fields.value.string_value | Directly mapped from the `ad.ThreadID` field.  
additional.Opcode | additional.fields.value.string_value | Directly mapped from the `ad.Opcode` field.  
additional.ProcessID | additional.fields.value.string_value | Directly mapped from the `ad.ProcessID` field.  
additional.TargetDomainName | additional.fields.value.string_value | Directly mapped from the `ad.TargetDomainName` field.  
additional.Version | additional.fields.value.string_value | Directly mapped from the `ad.Version` field.  
deviceExternalId | about.asset.hardware.serial_number | Directly mapped from the `deviceExternalId` field.  
deviceInboundInterface | additional.fields.value.string_value | Directly mapped from the `deviceInboundInterface` field.  
deviceOutboundInterface | additional.fields.value.string_value | Directly mapped from the `deviceOutboundInterface` field.  
PanOSConfigVersion | security_result.detection_fields.value | Directly mapped from the `PanOSConfigVersion` field.  
PanOSContentVersion | security_result.detection_fields.value | Directly mapped from the `PanOSContentVersion` field.  
PanOSDGHierarchyLevel1 | security_result.detection_fields.value | Directly mapped from the `PanOSDGHierarchyLevel1` field.  
PanOSDestinationLocation | target.location.country_or_region | Directly mapped from the `PanOSDestinationLocation` field.  
PanOSRuleUUID | metadata.product_log_id | Directly mapped from the `PanOSRuleUUID` field.  
PanOSThreatCategory | security_result.category_details | Directly mapped from the `PanOSThreatCategory` field.  
PanOSThreatID | security_result.threat_id | Directly mapped from the `PanOSThreatID` field.  
| about.asset.asset_id | Generated by concatenating `Palo Alto Networks.`, the vendor name (`LF`), and the `deviceExternalId` field.  
| extensions.auth.type | Set to `AUTHTYPE_UNSPECIFIED` if the `event_name` field contains `logged on`.  
| metadata.description | If the `description` field contains `by` followed by an IP address, the IP address is extracted and mapped to `principal.ip` and `principal.asset.ip`.  
| metadata.event_type | Determined based on a series of conditional checks on various fields, including `event_name`, `principal_*`, `target_*`, and `device_event_class_id`. The logic determines the most appropriate event type based on the available information.  
| metadata.log_type | Set to `ARCSIGHT_CEF`.  
| metadata.product_event_type | Generated by concatenating `\[`, the `device_event_class_id` field, `\] -`, and the `name` field.  
| metadata.product_name | Set to `NGFW` if the `product_name` field is `LF`.  
| principal.asset.ip | If the `description` field contains `by` followed by an IP address, the IP address is extracted and mapped to `principal.ip` and `principal.asset.ip`.  
| principal.ip | If the `description` field contains `by` followed by an IP address, the IP address is extracted and mapped to `principal.ip` and `principal.asset.ip`.  
| security_result.action | Set to `ALLOW` if the `act` field is `alert`, otherwise set to `BLOCK`.  
| security_result.severity | Set to `HIGH` if the `sev` field is greater than or equal to 7, otherwise set to `LOW`.  
`PanOSFileType` | `event.idm.read_only_udm.target.file.mime_type` | Mapped from changelog  
`PanOSEmailSubject` | `event.idm.read_only_udm.network.email.subject` | Mapped from changelog  
`PanOSNSSAINetworkSliceType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PanOSURLCounter` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PanOSReportID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PanOSDGHierarchyLevel2` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PanOSVirtualSystemName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PanOSSigFlags` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PanOSPartialHash` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cn3` | `network.duration.seconds` | Mapped from changelog  
`PanOSTenantID` | `additional.fields` | Mapped from changelog  
`cn3` | `additional.fields` | Mapped from changelog  
`PanOSCortexDataLakeTenantID` | `additional.fields` | Mapped from changelog  
`target_user` | `target.user.userid` | Mapped from changelog  
`principal_ip` | `principal.ip` | Mapped from changelog  
`PanOSStage", "PanOSConnectionError", and "PanOSEventDetails` | `additional.fields` | Mapped from changelog  
`outcome` | `security_result.action_details` | Mapped from changelog  
`PanOSDescription` | `metadata.description` | Mapped from changelog  
`PanOSSourceUser` | `principal.user.userid` | Mapped from changelog  
`app` | `target.application` | Mapped from changelog  
`flexString2", "PanOSFileHash", and "filePath` | `additional.fields` | Mapped from changelog  
`threat_name` | `security_result.threat_name` | Mapped from changelog  
`principal_ip1` | `principal.ip` | Mapped from changelog  
`metadata.event_type` | `NETWORK_CONNECTION` | Mapped from changelog  
`deviceOutboundInterface", "deviceInboundInterface` | `additional.fields` | Mapped from changelog  
`query` | `additional fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arcsight-cef-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
