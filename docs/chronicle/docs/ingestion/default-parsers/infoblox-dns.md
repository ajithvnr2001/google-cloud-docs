---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/infoblox-dns/
title: Collect Infoblox DNS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:03:36.658943+00:00
---

# Collect Infoblox DNS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/infoblox-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Infoblox DNS logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Infoblox DNS logs to Google Security Operations using the Bindplane agent.

The parser extracts fields from Infoblox DNS SYSLOG and CEF formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Infoblox Grid Manager web interface



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
            chronicle/chronicle_w_labels:
                compression: gzip
                creds_file_path: '/path/to/ingestion-authentication-file.json'
                customer_id: 'YOUR_CUSTOMER_ID'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: 'INFOBLOX_DNS'
                raw_log_field: body
                ingestion_labels:
        
        service:
            pipelines:
                logs/source0__chronicle_w_labels-0:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/chronicle_w_labels
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: Use `udplog` for UDP syslog or `tcplog` for TCP syslog
    * `0.0.0.0`: IP address to listen on (`0.0.0.0` to listen on all interfaces)
    * `514`: Port number to listen on (standard syslog port)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `YOUR_CUSTOMER_ID`: Customer ID from the Get customer ID section
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `log_type`: Log type exactly as it appears in Chronicle (`INFOBLOX_DNS`)



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
             




## Configure Syslog forwarding on Infoblox DNS

Use this section for on-premises Infoblox NIOS. For Infoblox BloxOne (cloud) deployments, use the **Configure Infoblox BloxOne (Data Connector)** section that follows instead.

  1. Sign in to the **Infoblox Grid Manager** web interface.
  2. Go to **Grid > Grid Manager > Members**.
  3. Select the member to configure and click **Edit**.
  4. Go to the **Monitoring** tab.
  5. Under **Syslog** , click **Add** to add a new syslog server.
  6. Provide the following configuration details: 
     * **Address** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Transport** : Select **UDP**.
     * **Node ID** : Select the Infoblox node (for HA pairs).
     * **Severity** : Select **Info** (or your preferred severity level).
     * **Facility** : Select **local0** (or your preferred facility).
  7. Enable the following log categories: 
     * **DNS queries** : Check **Log DNS Queries** under **Grid DNS Properties > Logging**.
     * **DNS responses** : Check **Log DNS Responses**.
     * **DHCP** : Enable DHCP logging under **Grid DHCP Properties**.
     * **Audit** : Enable audit logging under **Grid Properties > Monitoring**.
  8. Click **Save & Close**.
  9. Restart the DNS service if required.
  10. Verify syslog messages are being sent by checking the Bindplane agent logs.



## Configure Infoblox BloxOne (Data Connector) to forward DNS logs

For Infoblox BloxOne (cloud) deployments, use the Infoblox Data Connector to forward DNS query and response logs as CEF over syslog to the Bindplane agent you configured earlier.

**Note:** Select **CEF** as the syslog format. The Google SecOps Infoblox DNS parser supports SYSLOG and CEF formats; it does not parse LEEF.

  1. Deploy the Infoblox Data Connector if you have not already, following the [Deploying the Data Connector Solution](https://docs.infoblox.com/space/BloxOneCloud/35429862) guide.
  2. Sign in to the **Infoblox Portal**.
  3. Go to **Integrations > Data Connectors**.
  4. On the **Destination Configuration** tab, from the **Create** drop-down list, select **Syslog**.
  5. In the **Create Syslog Destination Configuration** wizard, provide the following configuration details: 
     * **Name** : Enter a name that distinguishes this destination (for example, `secops-bindplane`).
     * **State** : Enable the destination using the slider.
     * **Format** : Select **CEF**.
     * **FQDN/IP** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter the port that your Bindplane syslog receiver listens on (for example, `514`).
     * **Protocol** : Select the protocol that matches your Bindplane syslog receiver (**UDP** or **TCP**).
  6. Click **Save & Close**.
  7. Select the **Source** tab and confirm a DNS query and response source is available. **Infoblox Threat Defense** is pre-configured and needs no setup. For **Universal DDI** or on-prem **NIOS** DNS sources, configure the source here first, following the [Configuring Sources](https://docs.infoblox.com/space/BloxOneCloud/35366317) guide.
  8. Select the **Traffic Flow Configuration** tab, click **Create** , and provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `dns-to-secops`).
     * **Source** : Select the DNS query and response source (**Infoblox Threat Defense** Query/Response Log, or **Universal DDI** DNS Query/Response Log).
     * **Destination** : Select the syslog destination you created.
     * **Service Instance** : Select the Data Connector service instance (optionally add a secondary instance for failover).
     * **State** : Enable the traffic flow using the slider.
  9. Click **Save & Close**.

**Note:** Only one syslog traffic flow is supported per Data Connector. DNS query and response data is exported in CEF, which the Google SecOps Infoblox DNS parser maps to UDM. It may take a few minutes for logs to begin streaming to the Bindplane agent.

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
`_field` | `additional.fields` | Merged  
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
`allow_recursion_label` | `additional.fields` | Merged  
`auth_type_label` | `additional.fields` | Merged  
`create_ptr_for_bulk_hosts_label` | `additional.fields` | Merged  
`create_ptr_for_hosts_label` | `additional.fields` | Merged  
`cs2` | `additional.fields` | Mapped: `arc_test` → `additional_cs2`  
`cs5_label` | `additional.fields` | Merged  
`ddns_principal_group_label` | `additional.fields` | Merged  
`exclude_subobj_label` | `additional.fields` | Merged  
`is_multimaster_label` | `additional.fields` | Merged  
`locked_label` | `additional.fields` | Merged  
`message` | `additional.fields` | Mapped values (34 total, e.g. `CEF:` → `additional_eventId`, `CEF:` → `additional_devicePayl...  
`mgm_private_label` | `additional.fields` | Merged  
`ms_ad_integrated_label` | `additional.fields` | Merged  
`network_view_label` | `additional.fields` | Merged  
`object_type` | `additional.fields` | Mapped values (12 total, e.g. `DnsView` → `allow_recursion_label`, `DnsView` → `ddns_princip...  
`use_ssh_keys_label` | `additional.fields` | Merged  
`view_label` | `additional.fields` | Merged  
`zone_format_label` | `additional.fields` | Merged  
`_intermediary` | `intermediary` | Merged  
`message` | `intermediary` | Mapped: `CEF:` → `_intermediary`  
`description` | `metadata.description` | Directly mapped  
`msg` | `metadata.description` | Renamed/mapped  
`Generated` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`Received` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`datetime` | `metadata.event_timestamp` | Parsed as `dd-MMM-yyyy HH:mm:ss.SSS`  
`rt` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`syslog_timestamp` | `metadata.event_timestamp` | Parsed as `MMM d HH:mm:ss`  
`event_name` | `metadata.event_type` | Mapped: `"LogSpyware","LogPredictiveMachineLearning"` → `SCAN_UNCATEGORIZED`  
`event_type` | `metadata.event_type` | Renamed/mapped  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`message` | `metadata.event_type` | Mapped: `CEF:` → `PROCESS_UNCATEGORIZED`, `CEF:` → `SCAN_UNCATEGORIZED`, `CEF:` → `USER_UNCA...  
`device_event_class_id` | `metadata.product_event_type` | Directly mapped  
`event_name` | `metadata.product_event_type` | Directly mapped  
`evt_type` | `metadata.product_event_type` | Directly mapped  
`object_type` | `metadata.product_event_type` | Directly mapped  
`externalId` | `metadata.product_log_id` | Directly mapped  
`device_product` | `metadata.product_name` | Directly mapped  
`message` | `metadata.product_name` | Mapped: `CEF:` → `Infoblox DNS`  
`device_version` | `metadata.product_version` | Directly mapped  
`device_vendor` | `metadata.vendor_name` | Renamed/mapped  
`message` | `metadata.vendor_name` | Mapped: `CEF:` → `INFOBLOX`  
`app_protocol_output` | `network.application_protocol` | Directly mapped  
`message` | `network.application_protocol` | Mapped: `CEF:` → `DNS`  
`deviceDirection` | `network.direction` | Mapped: `0` → `INBOUND`, `1` → `OUTBOUND`  
`message` | `network.direction` | Mapped: `CEF:` → `INBOUND`, `CEF:` → `OUTBOUND`  
`answers1` | `network.dns.answers` | Merged  
`answers2` | `network.dns.answers` | Merged  
`dns_answer` | `network.dns.answers` | Merged  
`message` | `network.dns.answers` | Mapped: `CEF:` → `dns_answer`, `CEF:` → `answers1`, `CEF:` → `answers2`  
`msg2` | `network.dns.answers` | Mapped: `;` → `dns_answer`  
`authority` | `network.dns.authority` | Merged  
`dns_authority` | `network.dns.authority` | Merged  
`message` | `network.dns.authority` | Mapped: `CEF:` → `dns_authority`, `CEF:` → `authority`  
`dns_question` | `network.dns.questions` | Merged  
`message` | `network.dns.questions` | Mapped: `CEF:` → `dns_question`  
`dns.response_code` | `network.dns.response_code` | Renamed/mapped  
`requestMethod` | `network.http.method` | Renamed/mapped  
`requestClientApplication` | `network.http.user_agent` | Renamed/mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`protocol` | `network.ip_protocol` | Directly mapped  
`in` | `network.received_bytes` | Renamed/mapped  
`out` | `network.sent_bytes` | Renamed/mapped  
`sntdom` | `principal.administrative_domain` | Renamed/mapped  
`sourceServiceName` | `principal.application` | Renamed/mapped  
`src_host` | `principal.asset.hostname` | Directly mapped  
`src_ip` | `principal.asset.hostname` | Directly mapped  
`message` | `principal.asset.ip` | Mapped: `CEF:` → `src_ip`  
`src_ip` | `principal.asset.ip` | Merged  
`Group_name` | `principal.group.group_display_name` | Directly mapped  
`Gruppenavn` | `principal.group.group_display_name` | Directly mapped  
`Device_name` | `principal.hostname` | Directly mapped  
`Enhetsnavn` | `principal.hostname` | Directly mapped  
`shost` | `principal.hostname` | Renamed/mapped  
`src_host` | `principal.hostname` | Directly mapped  
`src_ip` | `principal.hostname` | Directly mapped  
`message` | `principal.ip` | Mapped: `CEF:` → `principal_ip`, `CEF:` → `shost`, `CEF:` → `src_ip`  
`principal_ip` | `principal.ip` | Merged  
`shost` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`InfobloxB1Region` | `principal.location.country_or_region` | Directly mapped  
`mac` | `principal.mac` | Merged  
`message` | `principal.mac` | Mapped: `CEF:` → `mac`  
`message` | `principal.nat_ip` | Mapped: `CEF:` → `sourceTranslatedAddress`  
`sourceTranslatedAddress` | `principal.nat_ip` | Merged  
`sourceTranslatedPort` | `principal.nat_port` | Renamed/mapped  
`spt` | `principal.port` | Renamed/mapped  
`src_port` | `principal.port` | Directly mapped  
`sproc` | `principal.process.command_line` | Renamed/mapped  
`spid` | `principal.process.pid` | Renamed/mapped  
`message` | `principal.user.attribute.roles` | Mapped: `CEF:` → `principal_role`  
`principal_role` | `principal.user.attribute.roles` | Merged  
`suser` | `principal.user.user_display_name` | Directly mapped  
`actor_details` | `principal.user.userid` | Directly mapped  
`suid` | `principal.user.userid` | Renamed/mapped  
`message` | `security_result` | Mapped: `CEF:` → `security_result`, `CEF:` → `sec_result`  
`sec_result` | `security_result` | Merged  
`_action` | `security_result.action` | Merged  
`act` | `security_result.action` | Mapped: `accept` → `_action`, `deny` → `_action`  
`message` | `security_result.action` | Mapped: `CEF:` → `_action`  
`Action_Taken` | `security_result.action_details` | Directly mapped  
`act` | `security_result.action_details` | Directly mapped  
`cat` | `security_result.category_details` | Merged  
`message` | `security_result.category_details` | Mapped: `CEF:` → `cat`  
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
`mwProfile` | `security_result.rule_name` | Directly mapped  
`message` | `security_result.severity` | Mapped: `CEF:` → `LOW`, `CEF:` → `MEDIUM`, `CEF:` → `HIGH`, `CEF:` → `CRITICAL`  
`severity` | `security_result.severity` | Mapped: `"0", "1", "2", "3", "LOW"` → `LOW`, `"4", "5", "6", "MEDIUM", "SUBSTANTIAL", "INFO"...  
`Result` | `security_result.summary` | Directly mapped  
`appcategory` | `security_result.summary` | Directly mapped  
`reason` | `security_result.summary` | Renamed/mapped  
`Spyware` | `security_result.threat_name` | Directly mapped  
`Unknown_Threat` | `security_result.threat_name` | Directly mapped  
`Virus_Malware_Name` | `security_result.threat_name` | Directly mapped  
`oldFilePath` | `src.file.full_path` | Renamed/mapped  
`oldFileSize` | `src.file.size` | Renamed/mapped  
`message` | `src.resource.attribute.permissions` | Mapped: `CEF:` → `old_permissions`  
`old_permissions` | `src.resource.attribute.permissions` | Merged  
`dntdom` | `target.administrative_domain` | Renamed/mapped  
`destinationServiceName` | `target.application` | Renamed/mapped  
`dst_ip` | `target.asset.hostname` | Directly mapped  
`dst_ip1` | `target.asset.hostname` | Directly mapped  
`dst_ip1` | `target.asset.ip` | Merged  
`message` | `target.asset.ip` | Mapped: `CEF:` → `dst_ip1`  
`message` | `target.asset.mac` | Mapped: `CEF:` → `target_mac`  
`target_mac` | `target.asset.mac` | Mapped: `^([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}$` → `target_mac`  
`dst_ip` | `target.hostname` | Directly mapped  
`dst_ip1` | `target.hostname` | Directly mapped  
`fqdn` | `target.hostname` | Directly mapped  
`temp_dhost` | `target.hostname` | Directly mapped  
`IPv6_Address` | `target.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`dst_ip1` | `target.ip` | Merged  
`ipv6` | `target.ip` | Mapped: `-` → `IPv6_Address`  
`message` | `target.ip` | Mapped: `CEF:` → `dst_ip`, `CEF:` → `IPv6_Address`, `CEF:` → `dst_ip1`  
`mac_address` | `target.mac` | Merged  
`message` | `target.mac` | Mapped: `CEF:` → `mac_address`, `CEF:` → `target_mac`  
`target_mac` | `target.mac` | Mapped: `^([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}$` → `target_mac`  
`destination_translated_address` | `target.nat_ip` | Merged  
`message` | `target.nat_ip` | Mapped: `CEF:` → `destination_translated_address`  
`destinationTranslatedPort` | `target.nat_port` | Renamed/mapped  
`dpt` | `target.port` | Renamed/mapped  
`dst_port` | `target.port` | Directly mapped  
`dproc` | `target.process.command_line` | Renamed/mapped  
`File_name` | `target.process.file.full_path` | Directly mapped  
`Infected_Resource` | `target.process.file.full_path` | Directly mapped  
`Object` | `target.process.file.full_path` | Directly mapped  
`Objekt` | `target.process.file.full_path` | Directly mapped  
`dpid` | `target.process.pid` | Renamed/mapped  
`message` | `target.resource.attribute.labels` | Mapped: `CEF:` → `resource_Type_label`  
`resource_Type_label` | `target.resource.attribute.labels` | Merged  
`name` | `target.resource.name` | Directly mapped  
`object_name` | `target.resource.name` | Directly mapped  
`request` | `target.url` | Directly mapped  
`message` | `target.user.attribute.roles` | Mapped: `CEF:` → `target_role`  
`target_role` | `target.user.attribute.roles` | Merged  
`group_id` | `target.user.group_identifiers` | Merged  
`message` | `target.user.group_identifiers` | Mapped: `CEF:` → `group_id`  
`object_type` | `target.user.group_identifiers` | Mapped: `AdminMember` → `group_id`  
`CustomerName` | `target.user.user_display_name` | Directly mapped  
`name` | `target.user.user_display_name` | Renamed/mapped  
`temp_duser` | `target.user.user_display_name` | Directly mapped  
`Bruker` | `target.user.userid` | Directly mapped  
`User_value` | `target.user.userid` | Directly mapped  
`object_name` | `target.user.userid` | Directly mapped  
`temp_duid` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `PROCESS_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `Infoblox DNS`  
N/A | `metadata.vendor_name` | Constant: `INFOBLOX`  
N/A | `network.application_protocol` | Constant: `DNS`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `security_result.severity` | Constant: `LOW`  
`dns_domain` | `dns.answers.name` | Mapped from changelog  
`ttl_data` | `dns.answers.ttl` | Mapped from changelog  
`dns_query_type` | `dns.answer.type` | Mapped from changelog  
`dns_class` | `dns.answer.class` | Mapped from changelog  
`intermediary_ip" or "intermediary_host` | `dns.answer.data` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/infoblox-dns-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
