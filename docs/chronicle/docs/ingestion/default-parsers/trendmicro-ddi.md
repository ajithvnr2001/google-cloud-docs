---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-ddi/
title: Collect Trend Micro DDI logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:47.506797+00:00
---

# Collect Trend Micro DDI logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-ddi/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trend Micro DDI logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trend Micro Deep Discovery Inspector (DDI) logs to Google Security Operations using the Bindplane agent.

Trend Micro Deep Discovery Inspector is a network appliance that monitors all ports and network protocols for advanced threats. It generates CEF-formatted syslog messages for Virtual Analyzer analysis results, integrated product detections, ICAP pre-scan events, system events, and alert events. The parser extracts fields from CEF-formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Trend Micro DDI appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to an instance of Trend Micro Deep Discovery Inspector



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
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/trendmicro_ddi:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: TRENDMICRO_DDI
            raw_log_field: body
        
        service:
          pipelines:
            logs/trendmicro_ddi_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/trendmicro_ddi
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
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
          chronicle/trendmicro_ddi:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: TRENDMICRO_DDI
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
             




## Configure syslog in Trend Micro Deep Discovery Inspector

  1. Sign in to the **Trend Micro Deep Discovery Inspector** web UI.
  2. Go to **Administration > Integrated Products/Services > Syslog**.
  3. Click **Add** to add a new Syslog server.
  4. Provide the following configuration details: 
     * **Enable** the Syslog profile.
     * **Profile name** : Enter a unique and meaningful name.
     * **Server address** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (for example, `UDP: 514`).
     * **Protocol** : Select **UDP** (or other protocol based on your Bindplane configuration).
     * **Facility** : Enter **Local0**.
     * **Severity** : Select **Informational**.
     * **Format** : Select **CEF**.
     * **Logs scope** : Select **Virtual Analyzer analysis logs** , **Integrated product detection logs** , **ICAP pre-scan logs** , **System event logs** , and **Alert event logs**.
  5. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`message` | `about` | Mapped: `CEF:` → `about`  
`deviceNtDomain` | `about.administrative_domain` | Renamed/mapped  
`deviceExternalId` | `about.asset.asset_id` | Directly mapped  
`device_product` | `about.asset.asset_id` | Directly mapped  
`device_vendor` | `about.asset.asset_id` | Directly mapped  
`fileHash` | `about.file.full_path` | Directly mapped  
`filePath` | `about.file.full_path` | Renamed/mapped  
`_hash` | `about.file.sha256` | Renamed/mapped  
`fileHash` | `about.file.sha256` | Renamed/mapped  
`fsize` | `about.file.size` | Renamed/mapped  
`dvchost` | `about.hostname` | Renamed/mapped  
`ips` | `about.ip` | Merged  
`message` | `about.ip` | Mapped: `CEF:` → `ips`  
`dvc_mac` | `about.mac` | Mapped: `slot` → `mac_address`  
`dvcmac` | `about.mac` | Merged  
`mac_address` | `about.mac` | Merged  
`message` | `about.mac` | Mapped: `CEF:` → `mac_address`, `CEF:` → `dvcmac`  
`deviceTranslatedAddress` | `about.nat_ip` | Merged  
`message` | `about.nat_ip` | Mapped: `CEF:` → `deviceTranslatedAddress`  
`Emne` | `about.process.command_line` | Directly mapped  
`Path` | `about.process.command_line` | Directly mapped  
`Subject` | `about.process.command_line` | Directly mapped  
`deviceProcessName` | `about.process.command_line` | Renamed/mapped  
`dvcpid` | `about.process.pid` | Renamed/mapped  
`message` | `about.resource.attribute.permissions` | Mapped: `CEF:` → `permissions`  
`permissions` | `about.resource.attribute.permissions` | Merged  
`additional_cfp1` | `additional.fields` | Merged  
`additional_cfp2` | `additional.fields` | Merged  
`additional_cfp3` | `additional.fields` | Merged  
`additional_cfp4` | `additional.fields` | Merged  
`additional_cn1` | `additional.fields` | Merged  
`additional_cn2` | `additional.fields` | Merged  
`additional_cn3` | `additional.fields` | Merged  
`additional_cs1` | `additional.fields` | Merged  
`additional_cs2` | `additional.fields` | Merged  
`additional_cs3` | `additional.fields` | Merged  
`additional_cs4` | `additional.fields` | Merged  
`additional_cs5` | `additional.fields` | Merged  
`additional_cs6` | `additional.fields` | Merged  
`additional_cs7` | `additional.fields` | Merged  
`additional_devicePayloadId` | `additional.fields` | Merged  
`additional_eventId` | `additional.fields` | Merged  
`additional_flexString1` | `additional.fields` | Merged  
`additional_fname` | `additional.fields` | Merged  
`appGroup_label` | `additional.fields` | Merged  
`cn4_label` | `additional.fields` | Merged  
`cn5_label` | `additional.fields` | Merged  
`cnt_label` | `additional.fields` | Merged  
`compressed_file_hash_label` | `additional.fields` | Merged  
`cs10_label` | `additional.fields` | Merged  
`cs2` | `additional.fields` | Mapped: `arc_test` → `additional_cs2`  
`cs5_label` | `additional.fields` | Merged  
`cs8_label` | `additional.fields` | Merged  
`cs9_label` | `additional.fields` | Merged  
`device_mac_address_label` | `additional.fields` | Merged  
`evt_cat_label` | `additional.fields` | Merged  
`fileType_label` | `additional.fields` | Merged  
`message` | `additional.fields` | Mapped values (33 total, e.g. `CEF:` → `additional_eventId`, `CEF:` → `additional_devicePayl...  
`pcomp_label` | `additional.fields` | Merged  
`ptype_label` | `additional.fields` | Merged  
`vlan_info` | `additional.fields` | Merged  
`msg` | `metadata.description` | Renamed/mapped  
`Generated` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`Received` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`date_value` | `metadata.event_timestamp` | Parsed as `MMM dd yyyy HH:mm:ss ZZ`  
`rt` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`event_name` | `metadata.event_type` | Mapped: `"LogSpyware","LogPredictiveMachineLearning"` → `SCAN_UNCATEGORIZED`  
`message` | `metadata.event_type` | Mapped values (5 total, e.g. `CEF:` → `PROCESS_UNCATEGORIZED`, `CEF:` → `SCAN_UNCATEGORIZED`...  
`principal_present` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`device_event_class_id` | `metadata.product_event_type` | Directly mapped  
`event_name` | `metadata.product_event_type` | Directly mapped  
`externalId` | `metadata.product_log_id` | Directly mapped  
`device_product` | `metadata.product_name` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`device_vendor` | `metadata.vendor_name` | Renamed/mapped  
`app_protocol_output` | `network.application_protocol` | Directly mapped  
`deviceDirection` | `network.direction` | Mapped: `0` → `INBOUND`, `1` → `OUTBOUND`  
`message` | `network.direction` | Mapped: `CEF:` → `INBOUND`, `CEF:` → `OUTBOUND`  
`message` | `network.dns.questions` | Mapped: `CEF:` → `question`  
`question` | `network.dns.questions` | Merged  
`requestMethod` | `network.http.method` | Renamed/mapped  
`requestClientApplication` | `network.http.user_agent` | Renamed/mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`in` | `network.received_bytes` | Renamed/mapped  
`out` | `network.sent_bytes` | Renamed/mapped  
`sntdom` | `principal.administrative_domain` | Renamed/mapped  
`sourceServiceName` | `principal.application` | Renamed/mapped  
`Group_name` | `principal.group.group_display_name` | Directly mapped  
`Gruppenavn` | `principal.group.group_display_name` | Directly mapped  
`Device_name` | `principal.hostname` | Directly mapped  
`Enhetsnavn` | `principal.hostname` | Directly mapped  
`shost` | `principal.hostname` | Renamed/mapped  
`message` | `principal.ip` | Mapped: `CEF:` → `principal_ip`, `CEF:` → `shost`  
`principal_ip` | `principal.ip` | Merged  
`shost` | `principal.ip` | Merged  
`deviceMacAddress` | `principal.mac` | Merged  
`mac` | `principal.mac` | Merged  
`message` | `principal.mac` | Mapped: `CEF:` → `mac`, `CEF:` → `deviceMacAddress`  
`message` | `principal.nat_ip` | Mapped: `CEF:` → `sourceTranslatedAddress`  
`sourceTranslatedAddress` | `principal.nat_ip` | Merged  
`sourceTranslatedPort` | `principal.nat_port` | Renamed/mapped  
`spt` | `principal.port` | Renamed/mapped  
`sproc` | `principal.process.command_line` | Renamed/mapped  
`spid` | `principal.process.pid` | Renamed/mapped  
`message` | `principal.user.attribute.roles` | Mapped: `CEF:` → `principal_role`  
`principal_role` | `principal.user.attribute.roles` | Merged  
`suser` | `principal.user.user_display_name` | Directly mapped  
`suid` | `principal.user.userid` | Renamed/mapped  
`message` | `security_result` | Mapped: `CEF:` → `security_result`  
`_action` | `security_result.action` | Merged  
`act` | `security_result.action` | Mapped: `accept` → `_action`, `deny` → `_action`  
`message` | `security_result.action` | Mapped: `CEF:` → `_action`  
`Action_Taken` | `security_result.action_details` | Directly mapped  
`act` | `security_result.action_details` | Directly mapped  
`cat` | `security_result.category_details` | Merged  
`message` | `security_result.category_details` | Mapped: `CEF:` → `cat`  
`deviceRiskConfidenceLevel` | `security_result.confidence_score` | Directly mapped  
`message` | `security_result.confidence_score` | Mapped: `CEF:` → `float`  
`Scan_Type` | `security_result.description` | Directly mapped  
`Type` | `security_result.description` | Directly mapped  
`msg_data_2` | `security_result.description` | Directly mapped  
`infection_channel_label` | `security_result.detection_fields` | Merged  
`message` | `security_result.detection_fields` | Mapped values (7 total, e.g. `CEF:` → `operation_label`, `CEF:` → `operasjon_label`, `CEF:` ...  
`operasjon_label` | `security_result.detection_fields` | Merged  
`operation_label` | `security_result.detection_fields` | Merged  
`permission_label` | `security_result.detection_fields` | Merged  
`spyware_Grayware_Type_label` | `security_result.detection_fields` | Merged  
`threat_probability_label` | `security_result.detection_fields` | Merged  
`tillatelse_label` | `security_result.detection_fields` | Merged  
`ruleId` | `security_result.rule_id` | Directly mapped  
`mwProfile` | `security_result.rule_name` | Directly mapped  
`ruleName` | `security_result.rule_name` | Directly mapped  
`hostSeverity` | `security_result.severity` | Mapped: `"0", "1", "2", "3"` → `LOW`, `"4", "5", "6"` → `MEDIUM`, `"7", "8"` → `HIGH`, `"9",...  
`message` | `security_result.severity` | Mapped: `CEF:` → `LOW`, `CEF:` → `MEDIUM`, `CEF:` → `HIGH`, `CEF:` → `CRITICAL`  
`severity` | `security_result.severity` | Mapped: `"0", "1", "2", "3", "LOW"` → `LOW`, `"4", "5", "6", "MEDIUM", "SUBSTANTIAL", "INFO"...  
`Result` | `security_result.summary` | Directly mapped  
`appcategory` | `security_result.summary` | Directly mapped  
`reason` | `security_result.summary` | Renamed/mapped  
`Spyware` | `security_result.threat_name` | Directly mapped  
`Unknown_Threat` | `security_result.threat_name` | Directly mapped  
`Virus_Malware_Name` | `security_result.threat_name` | Directly mapped  
`malType` | `security_result.threat_name` | Directly mapped  
`oldFilePath` | `src.file.full_path` | Renamed/mapped  
`oldFileSize` | `src.file.size` | Renamed/mapped  
`message` | `src.resource.attribute.permissions` | Mapped: `CEF:` → `old_permissions`  
`old_permissions` | `src.resource.attribute.permissions` | Merged  
`dntdom` | `target.administrative_domain` | Renamed/mapped  
`destinationServiceName` | `target.application` | Renamed/mapped  
`temp_dhost` | `target.hostname` | Directly mapped  
`IPv6_Address` | `target.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`ipv6` | `target.ip` | Mapped: `-` → `IPv6_Address`  
`message` | `target.ip` | Mapped: `CEF:` → `dst_ip`, `CEF:` → `IPv6_Address`  
`mac_address` | `target.mac` | Merged  
`message` | `target.mac` | Mapped: `CEF:` → `mac_address`  
`destination_translated_address` | `target.nat_ip` | Merged  
`message` | `target.nat_ip` | Mapped: `CEF:` → `destination_translated_address`  
`destinationTranslatedPort` | `target.nat_port` | Renamed/mapped  
`dpt` | `target.port` | Renamed/mapped  
`dproc` | `target.process.command_line` | Renamed/mapped  
`File_name` | `target.process.file.full_path` | Directly mapped  
`Infected_Resource` | `target.process.file.full_path` | Directly mapped  
`Object` | `target.process.file.full_path` | Directly mapped  
`Objekt` | `target.process.file.full_path` | Directly mapped  
`dpid` | `target.process.pid` | Renamed/mapped  
`message` | `target.resource.attribute.labels` | Mapped: `CEF:` → `resource_Type_label`  
`resource_Type_label` | `target.resource.attribute.labels` | Merged  
`request` | `target.url` | Directly mapped  
`message` | `target.user.attribute.roles` | Mapped: `CEF:` → `target_role`  
`target_role` | `target.user.attribute.roles` | Merged  
`CustomerName` | `target.user.user_display_name` | Directly mapped  
`temp_duser` | `target.user.user_display_name` | Directly mapped  
`Bruker` | `target.user.userid` | Directly mapped  
`User_value` | `target.user.userid` | Directly mapped  
`temp_duid` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `PROCESS_UNCATEGORIZED`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `security_result.severity` | Constant: `LOW`  
`reason` | `event.idm.read_only_udm.network.dns.questions.name` | Mapped from changelog  
`deviceMacAddress` | `event.idm.read_only_udm.principal.mac` | Mapped from changelog  
`deviceRiskConfidenceLevel` | `event.idm.read_only_udm.security_result.confidence_score` | Mapped from changelog  
`ruleId` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`ruleName` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`hostSeverity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`malType` | `event.idm.read_only_udm.security_result.threat_name` | Mapped from changelog  
`vLANId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cnt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`evtCat` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`deviceGUID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ptype` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs9` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs10` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`pComp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cn4` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cn5` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs8` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`fileType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`appGroup` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`compressedFileHash` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-ddi-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
