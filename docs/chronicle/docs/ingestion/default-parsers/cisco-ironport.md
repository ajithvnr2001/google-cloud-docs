---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ironport/
title: Collect Cisco Secure Email and Web logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:09:00.896997+00:00
---

# Collect Cisco Secure Email and Web logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ironport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Secure Email and Web logs

**Parser Version:** 19.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Secure Email and Web (formerly IronPort) logs to Google Security Operations using the Bindplane agent.

Cisco Secure Email and Web is a security gateway solution that protects organizations from email-borne threats such as spam, phishing, malware, and data loss. It provides advanced threat protection, content filtering, encryption, and URL defense for both inbound and outbound email and web traffic. The gateway runs Cisco AsyncOS and supports centralized logging with multiple retrieval methods including syslog push.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Cisco Secure Email and Web management console (administrator role)
  * Network connectivity between the Cisco Secure Email and Web appliance and the Bindplane agent host on the configured syslog port



## Get Google SecOps Ingestion Authentication File

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
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            tcplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/cisco_ironport:
                compression: gzip
                creds_file_path: '/path/to/ingestion-authentication-file.json'
                customer_id: 'YOUR_CUSTOMER_ID'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: 'CISCO_IRONPORT'
                raw_log_field: body
                ingestion_labels:
        
        service:
            pipelines:
                logs/cisco_ironport_to_chronicle:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/cisco_ironport
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: Use `tcplog` for TCP syslog (recommended for Cisco Secure Email and Web) or `udplog` for UDP syslog
    * `0.0.0.0`: IP address to listen on (`0.0.0.0` to listen on all interfaces)
    * `514`: Port number to listen on (standard syslog port)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `YOUR_CUSTOMER_ID`: Customer ID from the Get customer ID section
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `log_type`: Log type exactly as it appears in Chronicle (`CISCO_IRONPORT`) 



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
             




## Configure Cisco Secure Email and Web syslog forwarding

  1. Sign in to the **Cisco Secure Email and Web** management console.
  2. Go to **System Administration > Log Subscriptions**.
  3. Click **Add Log Subscription**.
  4. Provide the following configuration details: 
     * **Log Type** : Select the log type to forward (for example, **Text Mail Logs**).
     * **Log Name** : Enter a descriptive name (for example, `secops-mail-logs`).
     * **Log Level** : Select **Informational**.
     * **Retrieval Method** : Select **Syslog Push**.
     * **Hostname** : Enter the IP address or hostname of the Bindplane agent host.
     * **Port** : Enter `514` (or the port configured in the Bindplane agent).
     * **Protocol** : Select **TCP**. Note: Select the same protocol configured in the Bindplane agent receiver (`tcplog` for TCP, `udplog` for UDP).
     * **Facility** : Select **LOG_MAIL** for mail-related logs or **LOG_LOCAL0** through **LOG_LOCAL7** for other log types.
  5. Click **Submit**.
  6. Repeat steps 3-5 for each log type you want to forward. Available log types include: 
     * Text Mail Logs
     * System Logs
     * Anti-Spam Logs
     * Anti-Virus Logs
     * AMP Engine Logs
     * Content Filter Logs
     * Message Tracking Logs
     * LDAP Debug Logs
     * Safelist/Blocklist Logs
     * Reporting Logs
     * Updater Logs Note: Authentication Logs and Bounce Logs do not support the Syslog Push retrieval method.
  7. Click **Commit Changes** to apply the configuration.
  8. Verify logs are being sent by checking the Bindplane agent logs.



For more information, see the [Cisco Secure Email Gateway user guide](https://www.cisco.com/c/en/us/support/security/email-security-appliance/series.html).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`about` | `about` | Merged  
`about1` | `about` | Merged  
`deviceNtDomain` | `about.administrative_domain` | Renamed/mapped  
`deviceExternalId` | `about.asset.asset_id` | Directly mapped  
`device_product` | `about.asset.asset_id` | Directly mapped  
`device_vendor` | `about.asset.asset_id` | Directly mapped  
`fileHash` | `about.file.full_path` | Directly mapped  
`filePath` | `about.file.full_path` | Renamed/mapped  
`file_name` | `about.file.full_path` | Directly mapped  
`AMP.fileHash` | `about.file.sha256` | Directly mapped  
`_hash` | `about.file.sha256` | Renamed/mapped  
`fileHash` | `about.file.sha256` | Renamed/mapped  
`fsize` | `about.file.size` | Renamed/mapped  
`dvchost` | `about.hostname` | Renamed/mapped  
`ips` | `about.ip` | Merged  
`dvcmac` | `about.mac` | Merged  
`mac_address` | `about.mac` | Merged  
`deviceTranslatedAddress` | `about.nat_ip` | Merged  
`Emne` | `about.process.command_line` | Directly mapped  
`Path` | `about.process.command_line` | Directly mapped  
`Subject` | `about.process.command_line` | Directly mapped  
`deviceProcessName` | `about.process.command_line` | Renamed/mapped  
`dvcpid` | `about.process.pid` | Renamed/mapped  
`permissions` | `about.resource.attribute.permissions` | Merged  
`ESAURLDetails` | `about.url` | Directly mapped  
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
`cs5_label` | `additional.fields` | Merged  
`cs_uri_label` | `additional.fields` | Merged  
`internal_id_label` | `additional.fields` | Merged  
`s_hierarchy_label` | `additional.fields` | Merged  
`sc_bytes_label` | `additional.fields` | Merged  
`intermediary` | `intermediary` | Merged  
`ESAHeloDomain` | `intermediary.administrative_domain` | Directly mapped  
`syslog_program` | `intermediary.application` | Directly mapped  
`hostname` | `intermediary.asset.hostname` | Directly mapped  
`column3` | `intermediary.hostname` | Directly mapped  
`hostname` | `intermediary.hostname` | Directly mapped  
`s_computerName` | `intermediary.hostname` | Directly mapped  
`intermediary_ip` | `intermediary.ip` | Merged  
`msg` | `metadata.description` | Renamed/mapped  
`msg2` | `metadata.description` | Directly mapped  
`device_event_class_id` | `metadata.product_event_type` | Directly mapped  
`event_name` | `metadata.product_event_type` | Directly mapped  
`product_event` | `metadata.product_event_type` | Directly mapped  
`externalId` | `metadata.product_log_id` | Directly mapped  
`device_product` | `metadata.product_name` | Directly mapped  
`device_product_name` | `metadata.product_name` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`device_vendor` | `metadata.vendor_name` | Renamed/mapped  
`network` | `network` | Renamed/mapped  
`app_protocol_output` | `network.application_protocol` | Directly mapped  
`from` | `network.email.from` | Directly mapped  
`mailfrom.sender` | `network.email.from` | Directly mapped  
`message_id` | `network.email.mail_id` | Directly mapped  
`subject` | `network.email.subject` | Merged  
`to` | `network.email.to` | Merged  
`cs_method` | `network.http.method` | Directly mapped  
`http_method` | `network.http.method` | Directly mapped  
`requestMethod` | `network.http.method` | Renamed/mapped  
`cs_user_agent` | `network.http.parsed_user_agent` | Renamed/mapped  
`http_response_code` | `network.http.response_code` | Directly mapped  
`response_code` | `network.http.response_code` | Directly mapped  
`cs_user_agent` | `network.http.user_agent` | Directly mapped  
`requestClientApplication` | `network.http.user_agent` | Renamed/mapped  
`useragent` | `network.http.user_agent` | Directly mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`in` | `network.received_bytes` | Renamed/mapped  
`received_bytes` | `network.received_bytes` | Directly mapped  
`out` | `network.sent_bytes` | Renamed/mapped  
`total_bytes` | `network.sent_bytes` | Renamed/mapped  
`ESATLSInCipher` | `network.tls.cipher` | Directly mapped  
`sntdom` | `principal.administrative_domain` | Renamed/mapped  
`sourceServiceName` | `principal.application` | Renamed/mapped  
`principal_host` | `principal.asset.hostname` | Directly mapped  
`c_ip` | `principal.asset.ip` | Merged  
`cs_x_forwarded_for` | `principal.asset.ip` | Merged  
`source_ip` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`Group_name` | `principal.group.group_display_name` | Directly mapped  
`Gruppenavn` | `principal.group.group_display_name` | Directly mapped  
`Device_name` | `principal.hostname` | Directly mapped  
`Enhetsnavn` | `principal.hostname` | Directly mapped  
`principal_host` | `principal.hostname` | Directly mapped  
`shost` | `principal.hostname` | Renamed/mapped  
`c_ip` | `principal.ip` | Merged  
`cs_x_forwarded_for` | `principal.ip` | Merged  
`principal_ip` | `principal.ip` | Merged  
`shost` | `principal.ip` | Merged  
`source_ip` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`mac` | `principal.mac` | Merged  
`sourceTranslatedAddress` | `principal.nat_ip` | Merged  
`sourceTranslatedPort` | `principal.nat_port` | Renamed/mapped  
`c_port` | `principal.port` | Directly mapped  
`spt` | `principal.port` | Renamed/mapped  
`src_port` | `principal.port` | Directly mapped  
`sproc` | `principal.process.command_line` | Renamed/mapped  
`processName` | `principal.process.file.full_path` | Directly mapped  
`spid` | `principal.process.pid` | Renamed/mapped  
`principalUrl` | `principal.url` | Directly mapped  
`principal_role` | `principal.user.attribute.roles` | Merged  
`email` | `principal.user.email_addresses` | Merged  
`helo.sender` | `principal.user.email_addresses` | Merged  
`suser` | `principal.user.user_display_name` | Directly mapped  
`authenticated_user` | `principal.user.userid` | Directly mapped  
`cs_username` | `principal.user.userid` | Directly mapped  
`suid` | `principal.user.userid` | Renamed/mapped  
`sec_result` | `security_result` | Merged  
`security_result` | `security_result` | Merged  
`_action` | `security_result.action` | Merged  
`tempaction` | `security_result.action` | Merged  
`Action_Taken` | `security_result.action_details` | Directly mapped  
`act` | `security_result.action_details` | Directly mapped  
`cat` | `security_result.category_details` | Merged  
`Scan_Type` | `security_result.description` | Directly mapped  
`Type` | `security_result.description` | Directly mapped  
`msg_data_2` | `security_result.description` | Directly mapped  
`field1` | `security_result.detection_fields` | Merged  
`infection_channel_label` | `security_result.detection_fields` | Merged  
`operasjon_label` | `security_result.detection_fields` | Merged  
`operation_label` | `security_result.detection_fields` | Merged  
`permission_label` | `security_result.detection_fields` | Merged  
`spyware_Grayware_Type_label` | `security_result.detection_fields` | Merged  
`threat_probability_label` | `security_result.detection_fields` | Merged  
`tillatelse_label` | `security_result.detection_fields` | Merged  
`mwProfile` | `security_result.rule_name` | Directly mapped  
`Result` | `security_result.summary` | Directly mapped  
`appcategory` | `security_result.summary` | Directly mapped  
`reason` | `security_result.summary` | Renamed/mapped  
`Spyware` | `security_result.threat_name` | Directly mapped  
`Unknown_Threat` | `security_result.threat_name` | Directly mapped  
`Virus_Malware_Name` | `security_result.threat_name` | Directly mapped  
`oldFilePath` | `src.file.full_path` | Renamed/mapped  
`oldFileSize` | `src.file.size` | Renamed/mapped  
`old_permissions` | `src.resource.attribute.permissions` | Merged  
`target` | `target` | Renamed/mapped  
`dntdom` | `target.administrative_domain` | Renamed/mapped  
`destinationServiceName` | `target.application` | Renamed/mapped  
`host` | `target.asset.hostname` | Directly mapped  
`dst_ip1` | `target.asset.ip` | Merged  
`ip` | `target.asset.ip` | Merged  
`target_ip` | `target.asset.ip` | Merged  
`host` | `target.hostname` | Directly mapped  
`s_computerName` | `target.hostname` | Directly mapped  
`s_hostname` | `target.hostname` | Directly mapped  
`target_host` | `target.hostname` | Directly mapped  
`temp_dhost` | `target.hostname` | Directly mapped  
`IPv6_Address` | `target.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`dst_ip1` | `target.ip` | Merged  
`ip` | `target.ip` | Merged  
`target_ip` | `target.ip` | Merged  
`mac_address` | `target.mac` | Merged  
`destination_translated_address` | `target.nat_ip` | Merged  
`destinationTranslatedPort` | `target.nat_port` | Renamed/mapped  
`dpt` | `target.port` | Renamed/mapped  
`dst_port` | `target.port` | Directly mapped  
`s_port` | `target.port` | Directly mapped  
`dproc` | `target.process.command_line` | Renamed/mapped  
`File_name` | `target.process.file.full_path` | Directly mapped  
`Infected_Resource` | `target.process.file.full_path` | Directly mapped  
`Object` | `target.process.file.full_path` | Directly mapped  
`Objekt` | `target.process.file.full_path` | Directly mapped  
`dpid` | `target.process.pid` | Renamed/mapped  
`resource_Type_label` | `target.resource.attribute.labels` | Merged  
`request` | `target.url` | Directly mapped  
`target_url` | `target.url` | Directly mapped  
`url1` | `target.url` | Directly mapped  
`url2` | `target.url` | Directly mapped  
`target_role` | `target.user.attribute.roles` | Merged  
`CustomerName` | `target.user.user_display_name` | Directly mapped  
`temp_duser` | `target.user.user_display_name` | Directly mapped  
`Bruker` | `target.user.userid` | Directly mapped  
`User_value` | `target.user.userid` | Directly mapped  
`target_user` | `target.user.userid` | Directly mapped  
`temp_duid` | `target.user.userid` | Directly mapped  
N/A | `about` | Constant: `about`  
N/A | `about.ip` | Constant: `ips`  
N/A | `about.mac` | Constant: `mac_address`  
N/A | `about.nat_ip` | Constant: `deviceTranslatedAddress`  
N/A | `about.resource.attribute.permissions` | Constant: `permissions`  
N/A | `additional.fields` | Constant: `additional_eventId`  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `intermediary` | Constant: `intermediary`  
N/A | `intermediary.ip` | Constant: `intermediary_ip`  
N/A | `metadata.event_type` | Constant: `PROCESS_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `Cisco Ironport`  
N/A | `metadata.vendor_name` | Constant: `Cisco`  
N/A | `network.application_protocol` | Constant: `SMTP`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `network.email.subject` | Constant: `subject`  
N/A | `network.email.to` | Constant: `to`  
N/A | `network.received_bytes` | Constant: `uinteger`  
N/A | `principal.asset.ip` | Constant: `src_ip`  
N/A | `principal.ip` | Constant: `principal_ip`  
N/A | `principal.mac` | Constant: `mac`  
N/A | `principal.nat_ip` | Constant: `sourceTranslatedAddress`  
N/A | `principal.user.attribute.roles` | Constant: `principal_role`  
N/A | `principal.user.email_addresses` | Constant: `email`  
N/A | `security_result` | Constant: `security_result`  
N/A | `security_result.action` | Constant: `_action`  
N/A | `security_result.category_details` | Constant: `cat`  
N/A | `security_result.detection_fields` | Constant: `field1`  
N/A | `security_result.severity` | Constant: `LOW`  
N/A | `src.resource.attribute.permissions` | Constant: `old_permissions`  
N/A | `target.asset.ip` | Constant: `dst_ip1`  
N/A | `target.ip` | Constant: `dst_ip`  
N/A | `target.mac` | Constant: `mac_address`  
N/A | `target.nat_ip` | Constant: `destination_translated_address`  
N/A | `target.resource.attribute.labels` | Constant: `resource_Type_label`  
N/A | `target.user.attribute.roles` | Constant: `target_role`  
`column2` | `event.idm.read_only_udm.security_result.risk_score` | Mapped from changelog  
`column20` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`column23` | `event.idm.read_only_udm.security_result.threat_name` | Mapped from changelog  
`file_name` | `event.idm.read_only_udm.about.file.full_path` | Mapped from changelog  
`AMP.fileHash` | `event.idm.read_only_udm.about.file.sha256` | Mapped from changelog  
`ESAURLDetails` | `event.idm.read_only_udm.about.url` | Mapped from changelog  
`ESASenderGroup` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ESAAMPVerdict` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ESAASVerdict` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ESAAVVerdict` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Verdict` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column2` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`column3` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`column1` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`mailfrom.sender` | `event.idm.read_only_udm.network.email.from` | Mapped from changelog  
`ESAAttachmentDetails` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`result` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ESADCID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ESAICID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ESAMID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sc_bytes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`uritype` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`proto` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vendorid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`varianttype` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`uriidvalue` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs_url` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`cs_user_agent` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`dst_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`useragent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`response_code` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`cs_x_forwarded_for` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`target_host` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`about_hostname` | `event.idm.read_only_udm.about.hostname` | Mapped from changelog  
`cs_user_agent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`cs_method` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`cs_url` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`c_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`c_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`cs_username` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`s_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`s_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`session_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_webcat_code_full` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_result_code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs_x_forwarded_for` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs_mime_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs_referer` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_req_dvs_scanverdict` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_sophos_file_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_elapsed_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`s_hierarchy` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs_auth_group` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs_bytes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs_uri` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_acltag` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_ids_verdict` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_resp_dvs_canverdict` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_resp_dvs_threat_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_resp_dvs_verdictname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_suspect_user_agent` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_wbrs_threat_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_webcat_req_code_abbr` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_webroot_scanverdict` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_webroot_threat_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_webroot_trace_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_webroot_trr` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_webcat_resp_code_abbr` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_wbrs_score` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_sophos_virus_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_sophos_scanverdict` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_sophos_scanerror` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_mcafee_av_virustype` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_mcafee_av_virusname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_mcafee_av_scanerror` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_req_dvs_verdictname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_mcafee_av_scanverdict` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_mcafee_filename` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_mcafee_av_detecttype` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_icap_server` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_avc_behaviour` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_app_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_app` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_amp_verdict` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_amp_upload_indicator` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_amp_sha` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_amp_score` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_amp_malware_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_amp_filename` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sc_result_code_denial` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dkim` | `security_result.summary` | Mapped from changelog  
`antivirus` | `security_result.detection_fields` | Mapped from changelog  
`threat_level` | `security_result.detection_fields` | Mapped from changelog  
`threat_category` | `security_result.detection_fields` | Mapped from changelog  
`suspected_domain` | `security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ironport-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
