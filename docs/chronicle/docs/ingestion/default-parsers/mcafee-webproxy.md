---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-webproxy/
title: Collect Skyhigh Secure Web Gateway (formerly McAfee Web Gateway) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:00.724691+00:00
---

# Collect Skyhigh Secure Web Gateway (formerly McAfee Web Gateway) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-webproxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Skyhigh Secure Web Gateway (formerly McAfee Web Gateway) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Skyhigh Secure Web Gateway (formerly known as McAfee Web Gateway) logs to Google Security Operations using Bindplane.

Skyhigh Secure Web Gateway is an on-premises web proxy appliance that protects organizations from web-based threats by inspecting HTTP, HTTPS, and FTP traffic. It provides URL filtering, anti-malware scanning, SSL inspection, data loss prevention, and application control capabilities. The appliance enforces web access policies and provides detailed logging of all web activity for compliance and security monitoring.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later, or a Linux host with `systemd`.
  * If running behind a proxy, ensure firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open.
  * Privileged access to the Skyhigh Secure Web Gateway management console.



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
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, consult the [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it is in the `/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           tcplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/mcafee_webproxy:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             customer_id: '<customer_id>'
             endpoint: chronicle.googleapis.com
             log_type: 'MCAFEE_WEBPROXY'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/mcafee_webproxy_to_chronicle:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/mcafee_webproxy
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace `<customer_id>` with the actual customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the path where the service account key file (Option 1) was saved in the Get Google SecOps credentials for the Bindplane agent section.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/mcafee_webproxy:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'MCAFEE_WEBPROXY'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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
         




## Configure syslog forwarding on Skyhigh Secure Web Gateway

  1. Sign in to the **Skyhigh Secure Web Gateway** management console.
  2. Go to **Policy** > **Settings** > **Logging** > **Syslog**.
  3. Click **Add** to create a new syslog destination.
  4. Provide the following configuration details: 
     * **Syslog Server** : Enter the Bindplane agent IP address (for example, `192.168.1.100`).
     * **Port** : Enter `514`.
     * **Protocol** : Select **TCP**.
     * **Log Level** : Select the desired log level (for example, **Informational** or higher).
     * **Format** : Select **Best Practices Access Log** or the desired log format.
  5. Select the log types to forward: 
     * **Access Log** \- records all web traffic passing through the gateway.
     * **Block Log** \- records blocked requests.
     * **Scan Log** \- records anti-malware scan results.
  6. Click **Save Changes**.
  7. Go to **Troubleshooting** > **Confirm Changes** and click **Save Changes** to apply the configuration.

**Note:** Make sure the Skyhigh Secure Web Gateway appliance can reach the Bindplane agent IP address and port over TCP.**Note:** For more information, see [Skyhigh Secure Web Gateway documentation](https://success.skyhighsecurity.com/Skyhigh_Secure_Web_Gateway_\(On_Premises\)).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`entry_format` | `about` | Mapped: `json_format` → `about`, `kv_format1` → `about`  
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
`entry_format` | `about.ip` | Mapped: `json_format` → `ips`, `kv_format1` → `ips`  
`ips` | `about.ip` | Merged  
`dvc_mac` | `about.mac` | Mapped: `slot` → `mac_address`  
`dvcmac` | `about.mac` | Merged  
`entry_format` | `about.mac` | Mapped: `json_format` → `mac_address`, `json_format` → `dvcmac`, `kv_format1` → `mac_address...  
`mac_address` | `about.mac` | Merged  
`deviceTranslatedAddress` | `about.nat_ip` | Merged  
`entry_format` | `about.nat_ip` | Mapped: `json_format` → `deviceTranslatedAddress`, `kv_format1` → `deviceTranslatedAddress`  
`Emne` | `about.process.command_line` | Directly mapped  
`Path` | `about.process.command_line` | Directly mapped  
`Subject` | `about.process.command_line` | Directly mapped  
`deviceProcessName` | `about.process.command_line` | Renamed/mapped  
`dvcpid` | `about.process.pid` | Renamed/mapped  
`entry_format` | `about.resource.attribute.permissions` | Mapped: `json_format` → `permissions`, `kv_format1` → `permissions`  
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
`application_name_label` | `additional.fields` | Merged  
`block_id_label` | `additional.fields` | Merged  
`cs2` | `additional.fields` | Mapped: `arc_test` → `additional_cs2`  
`cs5_label` | `additional.fields` | Merged  
`entry_format` | `additional.fields` | Mapped values (43 total, e.g. `json_format` → `additional_eventId`, `json_format` → `additio...  
`facility_label` | `additional.fields` | Merged  
`priority_label` | `additional.fields` | Merged  
`reputation_label` | `additional.fields` | Merged  
`entry_format` | `intermediary` | Mapped: `json_format` → `intermediary`, `kv_format1` → `intermediary`  
`intermediary_hostname` | `intermediary.hostname` | Directly mapped  
`intermediary_ip` | `intermediary.ip` | Merged  
`json_entry.client_ip` | `intermediary.ip` | Merged  
`_metadata` | `metadata` | Renamed/mapped  
`msg` | `metadata.description` | Renamed/mapped  
`Generated` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`Received` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`_timestamp` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`rt` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`ts` | `metadata.event_timestamp` | Parsed as `dd/MM/yyyy:HH:mm:ss Z`  
`entry_format` | `metadata.event_type` | Mapped: `json_format` → `PROCESS_UNCATEGORIZED`, `json_format` → `SCAN_UNCATEGORIZED`, `kv_f...  
`event_name` | `metadata.event_type` | Mapped: `"LogSpyware","LogPredictiveMachineLearning"` → `SCAN_UNCATEGORIZED`  
`event_type` | `metadata.event_type` | Directly mapped  
`device_event_class_id` | `metadata.product_event_type` | Directly mapped  
`event_name` | `metadata.product_event_type` | Directly mapped  
`externalId` | `metadata.product_log_id` | Directly mapped  
`device_product` | `metadata.product_name` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`device_vendor` | `metadata.vendor_name` | Renamed/mapped  
`_network` | `network` | Renamed/mapped  
`app_protocol_output` | `network.application_protocol` | Directly mapped  
`proto` | `network.application_protocol` | Directly mapped  
`proto_version` | `network.application_protocol_version` | Directly mapped  
`deviceDirection` | `network.direction` | Mapped: `0` → `INBOUND`, `1` → `OUTBOUND`  
`entry_format` | `network.direction` | Mapped: `json_format` → `INBOUND`, `json_format` → `OUTBOUND`, `kv_format1` → `INBOUND`, `kv...  
`http_method` | `network.http.method` | Directly mapped  
`requestMethod` | `network.http.method` | Renamed/mapped  
`userAgent` | `network.http.parsed_user_agent` | Renamed/mapped  
`requestContext` | `network.http.referral_url` | Directly mapped  
`http_response` | `network.http.response_code` | Directly mapped  
`requestClientApplication` | `network.http.user_agent` | Renamed/mapped  
`userAgent` | `network.http.user_agent` | Directly mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`proto` | `network.ip_protocol` | Directly mapped  
`bytesToClient` | `network.received_bytes` | Directly mapped  
`entry_format` | `network.received_bytes` | Mapped: `json_format` → `uinteger`, `kv_format1` → `uinteger`  
`in` | `network.received_bytes` | Renamed/mapped  
`bytesFromClient` | `network.sent_bytes` | Directly mapped  
`entry_format` | `network.sent_bytes` | Mapped: `json_format` → `uinteger`, `kv_format1` → `uinteger`  
`out` | `network.sent_bytes` | Renamed/mapped  
`_principal` | `principal` | Renamed/mapped  
`sntdom` | `principal.administrative_domain` | Renamed/mapped  
`sourceServiceName` | `principal.application` | Renamed/mapped  
`clientIP` | `principal.asset.ip` | Merged  
`entry_format` | `principal.asset.ip` | Mapped: `json_format` → `clientIP`, `json_format` → `principal_ip`, `kv_format1` → `clientIP...  
`principal_ip` | `principal.asset.ip` | Merged  
`Group_name` | `principal.group.group_display_name` | Directly mapped  
`Gruppenavn` | `principal.group.group_display_name` | Directly mapped  
`Device_name` | `principal.hostname` | Directly mapped  
`Enhetsnavn` | `principal.hostname` | Directly mapped  
`principal_hostname` | `principal.hostname` | Directly mapped  
`shost` | `principal.hostname` | Renamed/mapped  
`clientIP` | `principal.ip` | Merged  
`entry_format` | `principal.ip` | Mapped values (6 total, e.g. `json_format` → `principal_ip`, `json_format` → `shost`, `json_...  
`principal_ip` | `principal.ip` | Merged  
`shost` | `principal.ip` | Merged  
`entry_format` | `principal.mac` | Mapped: `json_format` → `mac`, `kv_format1` → `mac`  
`mac` | `principal.mac` | Merged  
`entry_format` | `principal.nat_ip` | Mapped: `json_format` → `sourceTranslatedAddress`, `kv_format1` → `sourceTranslatedAddress`  
`sourceTranslatedAddress` | `principal.nat_ip` | Merged  
`sourceTranslatedPort` | `principal.nat_port` | Renamed/mapped  
`spt` | `principal.port` | Renamed/mapped  
`sproc` | `principal.process.command_line` | Renamed/mapped  
`fileType` | `principal.process.file.mime_type` | Directly mapped  
`spid` | `principal.process.pid` | Renamed/mapped  
`entry_format` | `principal.user.attribute.roles` | Mapped: `json_format` → `principal_role`, `kv_format1` → `principal_role`  
`principal_role` | `principal.user.attribute.roles` | Merged  
`suser` | `principal.user.user_display_name` | Directly mapped  
`suid` | `principal.user.userid` | Renamed/mapped  
`userName` | `principal.user.userid` | Directly mapped  
`entry_format` | `security_result` | Mapped: `json_format` → `security_result`, `kv_format1` → `security_result`  
`_action` | `security_result.action` | Merged  
`act` | `security_result.action` | Mapped: `accept` → `_action`, `deny` → `_action`  
`action` | `security_result.action` | Merged  
`cn1_Label` | `security_result.action` | Mapped: `Block Reason` → `action`  
`entry_format` | `security_result.action` | Mapped values (6 total, e.g. `json_format` → `_action`, `json_format` → `action`, `json_form...  
`security_action` | `security_result.action` | Merged  
`Action_Taken` | `security_result.action_details` | Directly mapped  
`act` | `security_result.action_details` | Directly mapped  
`_security_category` | `security_result.category` | Merged  
`entry_format` | `security_result.category` | Mapped: `json_format` → `_security_category`, `kv_format1` → `_security_category`  
`_category_details` | `security_result.category_details` | Merged  
`cat` | `security_result.category_details` | Merged  
`entry_format` | `security_result.category_details` | Mapped: `json_format` → `cat`, `json_format` → `_category_details`, `kv_format1` → `cat`, `k...  
`sec_result_category_details` | `security_result.category_details` | Merged  
`Scan_Type` | `security_result.description` | Directly mapped  
`Type` | `security_result.description` | Directly mapped  
`msg_data_2` | `security_result.description` | Directly mapped  
`entry_format` | `security_result.detection_fields` | Mapped values (14 total, e.g. `json_format` → `operation_label`, `json_format` → `operasjon_...  
`infection_channel_label` | `security_result.detection_fields` | Merged  
`operasjon_label` | `security_result.detection_fields` | Merged  
`operation_label` | `security_result.detection_fields` | Merged  
`permission_label` | `security_result.detection_fields` | Merged  
`spyware_Grayware_Type_label` | `security_result.detection_fields` | Merged  
`threat_probability_label` | `security_result.detection_fields` | Merged  
`tillatelse_label` | `security_result.detection_fields` | Merged  
`mwProfile` | `security_result.rule_name` | Directly mapped  
`policy` | `security_result.rule_name` | Directly mapped  
`rule_name` | `security_result.rule_name` | Directly mapped  
`entry_format` | `security_result.severity` | Mapped values (8 total, e.g. `json_format` → `LOW`, `json_format` → `MEDIUM`, `json_format` ...  
`risk` | `security_result.severity` | Mapped: `High Risk` → `HIGH`, `Medium Risk` → `MEDIUM`  
`severity` | `security_result.severity` | Mapped: `"0", "1", "2", "3", "LOW"` → `LOW`, `"4", "5", "6", "MEDIUM", "SUBSTANTIAL", "INFO"...  
`risk` | `security_result.severity_details` | Directly mapped  
`Result` | `security_result.summary` | Directly mapped  
`appcategory` | `security_result.summary` | Directly mapped  
`av_status` | `security_result.summary` | Directly mapped  
`block_reason` | `security_result.summary` | Directly mapped  
`content` | `security_result.summary` | Directly mapped  
`icap_status` | `security_result.summary` | Directly mapped  
`reason` | `security_result.summary` | Renamed/mapped  
`summary` | `security_result.summary` | Directly mapped  
`Spyware` | `security_result.threat_name` | Directly mapped  
`Unknown_Threat` | `security_result.threat_name` | Directly mapped  
`Virus_Malware_Name` | `security_result.threat_name` | Directly mapped  
`oldFilePath` | `src.file.full_path` | Renamed/mapped  
`oldFileSize` | `src.file.size` | Renamed/mapped  
`entry_format` | `src.resource.attribute.permissions` | Mapped: `json_format` → `old_permissions`, `kv_format1` → `old_permissions`  
`old_permissions` | `src.resource.attribute.permissions` | Merged  
`_target` | `target` | Renamed/mapped  
`dntdom` | `target.administrative_domain` | Renamed/mapped  
`appname` | `target.application` | Directly mapped  
`destinationServiceName` | `target.application` | Renamed/mapped  
`tar_host` | `target.asset.hostname` | Directly mapped  
`tar_host` | `target.hostname` | Directly mapped  
`target_hostname` | `target.hostname` | Directly mapped  
`temp_dhost` | `target.hostname` | Directly mapped  
`IPv6_Address` | `target.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`entry_format` | `target.ip` | Mapped: `json_format` → `dst_ip`, `json_format` → `IPv6_Address`, `kv_format1` → `dst_ip`, `...  
`ipv6` | `target.ip` | Mapped: `-` → `IPv6_Address`  
`entry_format` | `target.mac` | Mapped: `json_format` → `mac_address`, `kv_format1` → `mac_address`  
`mac_address` | `target.mac` | Merged  
`destination_translated_address` | `target.nat_ip` | Merged  
`entry_format` | `target.nat_ip` | Mapped: `json_format` → `destination_translated_address`, `kv_format1` → `destination_transl...  
`destinationTranslatedPort` | `target.nat_port` | Renamed/mapped  
`dpt` | `target.port` | Renamed/mapped  
`tar_port` | `target.port` | Directly mapped  
`dproc` | `target.process.command_line` | Renamed/mapped  
`File_name` | `target.process.file.full_path` | Directly mapped  
`Infected_Resource` | `target.process.file.full_path` | Directly mapped  
`Object` | `target.process.file.full_path` | Directly mapped  
`Objekt` | `target.process.file.full_path` | Directly mapped  
`dpid` | `target.process.pid` | Renamed/mapped  
`entry_format` | `target.resource.attribute.labels` | Mapped: `json_format` → `resource_Type_label`, `kv_format1` → `resource_Type_label`  
`resource_Type_label` | `target.resource.attribute.labels` | Merged  
`request` | `target.url` | Directly mapped  
`tar_host` | `target.url` | Directly mapped  
`tar_port` | `target.url` | Directly mapped  
`entry_format` | `target.user.attribute.roles` | Mapped: `json_format` → `target_role`, `kv_format1` → `target_role`  
`target_role` | `target.user.attribute.roles` | Merged  
`CustomerName` | `target.user.user_display_name` | Directly mapped  
`temp_duser` | `target.user.user_display_name` | Directly mapped  
`Bruker` | `target.user.userid` | Directly mapped  
`User_value` | `target.user.userid` | Directly mapped  
`temp_duid` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `PROCESS_UNCATEGORIZED`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `security_result.severity` | Constant: `LOW`  
`url` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`categories` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`rt` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`reputationString` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`blockID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`applicationName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`facility` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`priority` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`userName` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`appname` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`http_method` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`proto_version` | `event.idm.read_only_udm.network.application_protocol_version` | Mapped from changelog  
`userAgent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`userAgent` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`bytesFromClient` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`bytesToClient` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`clientIP` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`clientIP` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`fileType` | `event.idm.read_only_udm.principal.process.file.mime_type` | Mapped from changelog  
`Type` | `event.idm.read_only_udm.target.file.mime_type` | Mapped from changelog  
`sr_bytes` | `network.send_bytes` | Mapped from changelog  
`requested_host" and "requested_path` | `target.url` | Mapped from changelog  
`username` | `principal.user.userid` | Mapped from changelog  
`destination_ip` | `target.ip` | Mapped from changelog  
`destination_port` | `target.port` | Mapped from changelog  
`target_ip` | `target.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-webproxy-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
