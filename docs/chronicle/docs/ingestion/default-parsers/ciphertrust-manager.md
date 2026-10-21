---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ciphertrust-manager/
title: Collect CipherTrust Manager logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:16:32.603299+00:00
---

# Collect CipherTrust Manager logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ciphertrust-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CipherTrust Manager logs

**Parser Version:** 18.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest CipherTrust Manager logs to Google Security Operations using the Bindplane agent.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and CipherTrust Manager
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the CipherTrust Manager web console



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

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
          chronicle/ciphertrust_manager:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: CIPHERTRUST_MANAGER
            raw_log_field: body
        
        service:
          pipelines:
            logs/ciphertrust_manager_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/ciphertrust_manager
        




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
          chronicle/ciphertrust_manager:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CIPHERTRUST_MANAGER
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
             




## Configure syslog for CipherTrust Manager

  1. Sign in to the **CipherTrust Manager** web console.
  2. Go to **Admin Settings > Notifications > Syslog**.
  3. Click **New Syslog Server**.
  4. Provide the following configuration details: 
     * **Host** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (default **514**).
     * **Log Format** : Select **RFC 5424**.
     * **Transport** : Select **UDP**.
  5. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`message` | `about` | Mapped: `CEF` → `about`  
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
`message` | `about.ip` | Mapped: `CEF` → `ips`  
`dvc_mac` | `about.mac` | Mapped: `slot` → `mac_address`  
`dvcmac` | `about.mac` | Merged  
`mac_address` | `about.mac` | Merged  
`message` | `about.mac` | Mapped: `CEF` → `mac_address`, `CEF` → `dvcmac`  
`deviceTranslatedAddress` | `about.nat_ip` | Merged  
`message` | `about.nat_ip` | Mapped: `CEF` → `deviceTranslatedAddress`  
`Emne` | `about.process.command_line` | Directly mapped  
`Path` | `about.process.command_line` | Directly mapped  
`Subject` | `about.process.command_line` | Directly mapped  
`deviceProcessName` | `about.process.command_line` | Renamed/mapped  
`dvcpid` | `about.process.pid` | Renamed/mapped  
`message` | `about.resource.attribute.permissions` | Mapped: `CEF` → `permissions`  
`permissions` | `about.resource.attribute.permissions` | Merged  
`Internal_label` | `additional.fields` | Merged  
`additional_alias_alias_field` | `additional.fields` | Merged  
`additional_alias_index_field` | `additional.fields` | Merged  
`additional_alias_type_field` | `additional.fields` | Merged  
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
`algorithm_label` | `additional.fields` | Merged  
`app_connector_type_label` | `additional.fields` | Merged  
`assignSelfAsOwner_label` | `additional.fields` | Merged  
`auth_domain_label` | `additional.fields` | Merged  
`client_name_label` | `additional.fields` | Merged  
`client_type_label` | `additional.fields` | Merged  
`codeDesc_label` | `additional.fields` | Merged  
`code_label` | `additional.fields` | Merged  
`createdAt_label` | `additional.fields` | Merged  
`cs2` | `additional.fields` | Mapped: `arc_test` → `additional_cs2`  
`cs5_label` | `additional.fields` | Merged  
`customAttributes_label` | `additional.fields` | Merged  
`deatils_domain_id_label` | `additional.fields` | Merged  
`details_user_metadata_current_domain_id_label` | `additional.fields` | Merged  
`details_user_metadata_current_persistedData_label` | `additional.fields` | Merged  
`details_user_metadata_current_persistedData_paging_label` | `additional.fields` | Merged  
`domain_id_label` | `additional.fields` | Merged  
`domain_label` | `additional.fields` | Merged  
`emptyMaterial_label` | `additional.fields` | Merged  
`feature_label` | `additional.fields` | Merged  
`format_label` | `additional.fields` | Merged  
`generateKeyId_label` | `additional.fields` | Merged  
`idType_label` | `additional.fields` | Merged  
`id_label` | `additional.fields` | Merged  
`identifier_label` | `additional.fields` | Merged  
`interfaceName_label` | `additional.fields` | Merged  
`interfaceType_label` | `additional.fields` | Merged  
`label_label` | `additional.fields` | Merged  
`message` | `additional.fields` | Mapped values (71 total, e.g. `CEF` → `additional_eventId`, `CEF` → `additional_devicePayloa...  
`messageFormat_label` | `additional.fields` | Merged  
`meta_label` | `additional.fields` | Merged  
`objectType_label` | `additional.fields` | Merged  
`ownerId_label` | `additional.fields` | Merged  
`padded_label` | `additional.fields` | Merged  
`permissions_label` | `additional.fields` | Merged  
`record_type_id_label` | `additional.fields` | Merged  
`refresh_token_counts_label` | `additional.fields` | Merged  
`refresh_token_counts_no_label` | `additional.fields` | Merged  
`refresh_token_counts_total_label` | `additional.fields` | Merged  
`refresh_token_id_label` | `additional.fields` | Merged  
`renew_refresh_token_label` | `additional.fields` | Merged  
`requestId_label` | `additional.fields` | Merged  
`requestIdentifierType_label` | `additional.fields` | Merged  
`requestIdentifier_label` | `additional.fields` | Merged  
`scope_label` | `additional.fields` | Merged  
`service_label` | `additional.fields` | Merged  
`switch_domain_id_label` | `additional.fields` | Merged  
`undeletable_label` | `additional.fields` | Merged  
`unexportable_label` | `additional.fields` | Merged  
`version_label` | `additional.fields` | Merged  
`xts_label` | `additional.fields` | Merged  
`zone_id_label` | `additional.fields` | Merged  
`details_grant_type` | `extensions.auth.auth_details` | Directly mapped  
`logon_type_temp` | `extensions.auth.mechanism` | Merged  
`message` | `extensions.auth.mechanism` | Mapped: `CEF` → `logon_type_temp`, `Get User` → `logon_type_temp`  
`message` | `intermediary` | Mapped: `CEF` → `intermediary`  
`proxy_ip` | `intermediary.ip` | Merged  
`msg` | `metadata.description` | Renamed/mapped  
`Generated` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`Received` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`event_time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`rt` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`syslog_timestamp` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss`  
`syslog_timestamp_with_year` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss yyyy`  
`cef_message` | `metadata.event_type` | Mapped: `(Use Key/Update Key/Export Key)` → `USER_RESOURCE_UPDATE_CONTENT`  
`event_name` | `metadata.event_type` | Mapped: `"LogSpyware","LogPredictiveMachineLearning"` → `SCAN_UNCATEGORIZED`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`message` | `metadata.event_type` | Mapped values (12 total, e.g. `CEF` → `PROCESS_UNCATEGORIZED`, `CEF` → `SCAN_UNCATEGORIZED`,...  
`device_event_class_id` | `metadata.product_event_type` | Directly mapped  
`event_name` | `metadata.product_event_type` | Directly mapped  
`externalId` | `metadata.product_log_id` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`uid` | `metadata.product_log_id` | Directly mapped  
`device_product` | `metadata.product_name` | Directly mapped  
`product` | `metadata.product_name` | Directly mapped  
`product_name` | `metadata.product_name` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`device_vendor` | `metadata.vendor_name` | Renamed/mapped  
`app_protocol_output` | `network.application_protocol` | Directly mapped  
`deviceDirection` | `network.direction` | Mapped: `0` → `INBOUND`, `1` → `OUTBOUND`  
`message` | `network.direction` | Mapped: `CEF` → `INBOUND`, `CEF` → `OUTBOUND`  
`requestMethod` | `network.http.method` | Renamed/mapped  
`requestClientApplication` | `network.http.user_agent` | Renamed/mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`in` | `network.received_bytes` | Renamed/mapped  
`out` | `network.sent_bytes` | Renamed/mapped  
`sntdom` | `principal.administrative_domain` | Renamed/mapped  
`sourceServiceName` | `principal.application` | Renamed/mapped  
`syslog_host` | `principal.asset.hostname` | Directly mapped  
`details_user_metadata_current_domain_name` | `principal.domain.name` | Directly mapped  
`Group_name` | `principal.group.group_display_name` | Directly mapped  
`Gruppenavn` | `principal.group.group_display_name` | Directly mapped  
`Device_name` | `principal.hostname` | Directly mapped  
`Enhetsnavn` | `principal.hostname` | Directly mapped  
`shost` | `principal.hostname` | Renamed/mapped  
`syslog_host` | `principal.hostname` | Directly mapped  
`client_ip` | `principal.ip` | Merged  
`message` | `principal.ip` | Mapped: `CEF` → `principal_ip`, `CEF` → `shost`, `CEF` → `client_ip`, `(SSL Handshake failed...  
`principal_ip` | `principal.ip` | Merged  
`shost` | `principal.ip` | Merged  
`mac` | `principal.mac` | Merged  
`message` | `principal.mac` | Mapped: `CEF` → `mac`  
`message` | `principal.nat_ip` | Mapped: `CEF` → `sourceTranslatedAddress`  
`sourceTranslatedAddress` | `principal.nat_ip` | Merged  
`sourceTranslatedPort` | `principal.nat_port` | Renamed/mapped  
`spt` | `principal.port` | Renamed/mapped  
`sproc` | `principal.process.command_line` | Renamed/mapped  
`spid` | `principal.process.pid` | Renamed/mapped  
`acc_label` | `principal.resource.attribute.labels` | Merged  
`acct_label` | `principal.resource.attribute.labels` | Merged  
`iss_label` | `principal.resource.attribute.labels` | Merged  
`jti_label` | `principal.resource.attribute.labels` | Merged  
`message` | `principal.resource.attribute.labels` | Mapped values (5 total, e.g. `CEF` → `acct_label`, `CEF` → `acc_label`, `CEF` → `iss_label`)  
`sub_label` | `principal.resource.attribute.labels` | Merged  
`message` | `principal.user.attribute.roles` | Mapped: `CEF` → `principal_role`  
`principal_role` | `principal.user.attribute.roles` | Merged  
`details_username` | `principal.user.user_display_name` | Directly mapped  
`suser` | `principal.user.user_display_name` | Directly mapped  
`username` | `principal.user.user_display_name` | Directly mapped  
`details_user_id` | `principal.user.userid` | Directly mapped  
`details_userid` | `principal.user.userid` | Directly mapped  
`suid` | `principal.user.userid` | Renamed/mapped  
`user_id` | `principal.user.userid` | Directly mapped  
`username` | `principal.user.userid` | Directly mapped  
`_security_result` | `security_result` | Merged  
`message` | `security_result` | Mapped: `CEF` → `security_result`  
`_action` | `security_result.action` | Merged  
`act` | `security_result.action` | Mapped: `accept` → `_action`, `deny` → `_action`  
`message` | `security_result.action` | Mapped: `CEF` → `_action`  
`Action_Taken` | `security_result.action_details` | Directly mapped  
`act` | `security_result.action_details` | Directly mapped  
`details_errorMessage` | `security_result.action_details` | Directly mapped  
`cat` | `security_result.category_details` | Merged  
`message` | `security_result.category_details` | Mapped: `CEF` → `cat`  
`Scan_Type` | `security_result.description` | Directly mapped  
`Type` | `security_result.description` | Directly mapped  
`message` | `security_result.description` | Directly mapped  
`msg_data_2` | `security_result.description` | Directly mapped  
`infection_channel_label` | `security_result.detection_fields` | Merged  
`message` | `security_result.detection_fields` | Mapped values (7 total, e.g. `CEF` → `operation_label`, `CEF` → `operasjon_label`, `CEF` → `...  
`operasjon_label` | `security_result.detection_fields` | Merged  
`operation_label` | `security_result.detection_fields` | Merged  
`permission_label` | `security_result.detection_fields` | Merged  
`spyware_Grayware_Type_label` | `security_result.detection_fields` | Merged  
`threat_probability_label` | `security_result.detection_fields` | Merged  
`tillatelse_label` | `security_result.detection_fields` | Merged  
`mwProfile` | `security_result.rule_name` | Directly mapped  
`message` | `security_result.severity` | Mapped: `CEF` → `LOW`, `CEF` → `MEDIUM`, `CEF` → `HIGH`, `CEF` → `CRITICAL`  
`severity` | `security_result.severity` | Mapped: `"0", "1", "2", "3", "LOW"` → `LOW`, `"4", "5", "6", "MEDIUM", "SUBSTANTIAL", "INFO"...  
`Result` | `security_result.summary` | Directly mapped  
`appcategory` | `security_result.summary` | Directly mapped  
`reason` | `security_result.summary` | Renamed/mapped  
`success` | `security_result.summary` | Directly mapped  
`Spyware` | `security_result.threat_name` | Directly mapped  
`Unknown_Threat` | `security_result.threat_name` | Directly mapped  
`Virus_Malware_Name` | `security_result.threat_name` | Directly mapped  
`oldFilePath` | `src.file.full_path` | Renamed/mapped  
`oldFileSize` | `src.file.size` | Renamed/mapped  
`client_ip` | `src.ip` | Merged  
`message` | `src.ip` | Mapped: `CEF` → `client_ip`  
`message` | `src.resource.attribute.permissions` | Mapped: `CEF` → `old_permissions`  
`old_permissions` | `src.resource.attribute.permissions` | Merged  
`cust_client_id` | `src.user.product_object_id` | Directly mapped  
`details_client_id` | `src.user.product_object_id` | Directly mapped  
`dntdom` | `target.administrative_domain` | Renamed/mapped  
`destinationServiceName` | `target.application` | Renamed/mapped  
`service` | `target.application` | Directly mapped  
`service_name` | `target.application` | Directly mapped  
`application` | `target.domain.name` | Directly mapped  
`details.size` | `target.file.size` | Renamed/mapped  
`details.host` | `target.hostname` | Directly mapped  
`target_hostname` | `target.hostname` | Directly mapped  
`temp_dhost` | `target.hostname` | Directly mapped  
`IPv6_Address` | `target.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`ipv6` | `target.ip` | Mapped: `-` → `IPv6_Address`  
`message` | `target.ip` | Mapped: `CEF` → `dst_ip`, `CEF` → `IPv6_Address`  
`mac_address` | `target.mac` | Merged  
`message` | `target.mac` | Mapped: `CEF` → `mac_address`  
`destination_translated_address` | `target.nat_ip` | Merged  
`message` | `target.nat_ip` | Mapped: `CEF` → `destination_translated_address`  
`destinationTranslatedPort` | `target.nat_port` | Renamed/mapped  
`details.port` | `target.port` | Renamed/mapped  
`dpt` | `target.port` | Renamed/mapped  
`dproc` | `target.process.command_line` | Renamed/mapped  
`File_name` | `target.process.file.full_path` | Directly mapped  
`Infected_Resource` | `target.process.file.full_path` | Directly mapped  
`Object` | `target.process.file.full_path` | Directly mapped  
`Objekt` | `target.process.file.full_path` | Directly mapped  
`dpid` | `target.process.pid` | Renamed/mapped  
`account_label` | `target.resource.attribute.labels` | Merged  
`connection_label` | `target.resource.attribute.labels` | Merged  
`message` | `target.resource.attribute.labels` | Mapped values (6 total, e.g. `CEF` → `resource_Type_label`, `CEF` → `name_label`, `CEF` → `u...  
`name_label` | `target.resource.attribute.labels` | Merged  
`resource_Type_label` | `target.resource.attribute.labels` | Merged  
`uri_label` | `target.resource.attribute.labels` | Merged  
`usageMask_label` | `target.resource.attribute.labels` | Merged  
`source` | `target.resource.name` | Directly mapped  
`request` | `target.url` | Directly mapped  
`message` | `target.user.attribute.roles` | Mapped: `CEF` → `target_role`  
`target_role` | `target.user.attribute.roles` | Merged  
`CustomerName` | `target.user.user_display_name` | Directly mapped  
`temp_duser` | `target.user.user_display_name` | Directly mapped  
`Bruker` | `target.user.userid` | Directly mapped  
`User_value` | `target.user.userid` | Directly mapped  
`temp_duid` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `network.ip_protocol` | Constant: `UDP`  
N/A | `security_result.severity` | Constant: `LOW`  
`details.host` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`details.messageFormat` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`details.transport` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`syslog_timestamp` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`syslog_host` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`product` | `event.idm.read_only_udm.metadata.product_name` | Mapped from changelog  
`details.errorMessage` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`sev` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ciphertrust-manager-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
