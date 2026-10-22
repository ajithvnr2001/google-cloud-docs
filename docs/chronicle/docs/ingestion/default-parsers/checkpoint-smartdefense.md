---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-smartdefense/
title: Collect Check Point SmartDefense logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:19.362737+00:00
---

# Collect Check Point SmartDefense logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-smartdefense/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Check Point SmartDefense logs

**Parser Version:** 18.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Check Point SmartDefense logs to Google Security Operations using the Bindplane agent.

The parser extracts fields from Check Point SmartDefense syslog formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Check Point SmartDefense management console or appliance



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

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: <customer_id>
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'CHECKPOINT_SMARTDEFENSE'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - udplog
               exporters:
                 - chronicle/chronicle_w_labels
         

     * Replace the port and IP address as required in your infrastructure.
     * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
     * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
     * Replace `<CUSTOMER_ID>` with the actual Customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: <customer_id>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'CHECKPOINT_SMARTDEFENSE'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Syslog forwarding on Check Point SmartDefense

### Step 1: Create Log Exporter/SIEM Object in SmartConsole

  1. Sign in to the **Check Point SmartConsole**.
  2. Go to **Objects** > **More object types** > **Server** > **Log Exporter/SIEM**.
  3. Click **New** to create a new Log Exporter object.
  4. Provide the following configuration details: 
     * **Object Name** : Enter a descriptive name (for example, `Google SecOps Bindplane`).
     * **Export Configuration** : Select **Enabled**.
     * **Target Server** : Enter the Bindplane agent IP address.
     * **Target Port** : Enter `514` (or your configured Bindplane agent port number).
     * **Protocol** : Select **UDP**.
  5. Go to the **Data Manipulation** page.
  6. Provide the following configuration details: 
     * **Format** : Select **Common Event Format (CEF)**.
     * **Timezone** : Select UTC timezone for universal consistency across systems.
  7. Click **OK** to save the configuration.



### Step 2: Configure Management Server or Log Server

  1. In SmartConsole, go to **Gateways & Servers**.
  2. Open your **Management Server** or **Dedicated Log Server/SmartEvent Server** object.
  3. Go to **Logs** > **Export**.
  4. Click **+** and select the Log Exporter/SIEM object you configured earlier.
  5. Click **OK**.



### Step 3: Install Database Policy

  1. From the top menu, click **Install** > **Install database**.
  2. Select **all objects**.
  3. Click **Install**.



### Step 4: Verify Log Export Configuration

  1. Connect to the command line on the Management Server/Log Server.
  2. Log in to Expert mode.
  3. Run the following command to verify the configuration:
         
         cp_log_export show
         

  4. To restart the Log Exporter if needed:
         
         cp_log_export restart
         




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
`cs2` | `additional.fields` | Mapped: `arc_test` → `additional_cs2`  
`cs5_label` | `additional.fields` | Merged  
`description_url_label` | `additional.fields` | Merged  
`http_host_label` | `additional.fields` | Merged  
`log_id_field` | `additional.fields` | Merged  
`message` | `additional.fields` | Mapped values (27 total, e.g. `CEF:` → `sequencenum_label`, `CEF:` → `additional_eventId`, `...  
`originsicname_field` | `additional.fields` | Merged  
`reject_id_kid_field` | `additional.fields` | Merged  
`sequencenum_label` | `additional.fields` | Merged  
`ser_agent_kid_field` | `additional.fields` | Merged  
`version_field` | `additional.fields` | Merged  
`message` | `extensions.vulns.vulnerabilities` | Mapped: `CEF:` → `v`  
`v` | `extensions.vulns.vulnerabilities` | Merged  
`int` | `intermediary` | Merged  
`message` | `intermediary` | Mapped: `CEF:` → `int`  
`msg` | `metadata.description` | Directly mapped  
`Generated` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`Received` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`lastupdatetime` | `metadata.event_timestamp` | Parsed as `UNIX`  
`rt` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`event_name` | `metadata.event_type` | Mapped: `"LogSpyware","LogPredictiveMachineLearning"` → `SCAN_UNCATEGORIZED`  
`message` | `metadata.event_type` | Mapped: `CEF:` → `PROCESS_UNCATEGORIZED`, `CEF:` → `SCAN_UNCATEGORIZED`, `CEF:` → `NETWORK_C...  
`principal_machine_id_present` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`  
`device_event_class_id` | `metadata.product_event_type` | Directly mapped  
`event_name` | `metadata.product_event_type` | Directly mapped  
`externalId` | `metadata.product_log_id` | Directly mapped  
`loguid` | `metadata.product_log_id` | Directly mapped  
`device_product` | `metadata.product_name` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`device_vendor` | `metadata.vendor_name` | Renamed/mapped  
`app_protocol_output` | `network.application_protocol` | Directly mapped  
`deviceDirection` | `network.direction` | Mapped: `0` → `INBOUND`, `1` → `OUTBOUND`  
`message` | `network.direction` | Mapped: `CEF:` → `INBOUND`, `CEF:` → `OUTBOUND`  
`requestMethod` | `network.http.method` | Renamed/mapped  
`requestClientApplication` | `network.http.user_agent` | Renamed/mapped  
`user_agent` | `network.http.user_agent` | Directly mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`in` | `network.received_bytes` | Renamed/mapped  
`out` | `network.sent_bytes` | Renamed/mapped  
`session_id` | `network.session_id` | Directly mapped  
`sntdom` | `principal.administrative_domain` | Renamed/mapped  
`sourceServiceName` | `principal.application` | Renamed/mapped  
`Group_name` | `principal.group.group_display_name` | Directly mapped  
`Gruppenavn` | `principal.group.group_display_name` | Directly mapped  
`Device_name` | `principal.hostname` | Directly mapped  
`Enhetsnavn` | `principal.hostname` | Directly mapped  
`shost` | `principal.hostname` | Renamed/mapped  
`ip_proxy` | `principal.ip` | Merged  
`message` | `principal.ip` | Mapped: `CEF:` → `principal_ip`, `CEF:` → `shost`, `CEF:` → `ip_proxy`  
`principal_ip` | `principal.ip` | Merged  
`shost` | `principal.ip` | Merged  
`mac` | `principal.mac` | Merged  
`message` | `principal.mac` | Mapped: `CEF:` → `mac`  
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
`Scan_Type` | `security_result.description` | Directly mapped  
`Type` | `security_result.description` | Directly mapped  
`msg_data_2` | `security_result.description` | Directly mapped  
`fn1` | `security_result.detection_fields` | Merged  
`fn2` | `security_result.detection_fields` | Merged  
`fs2` | `security_result.detection_fields` | Merged  
`ifname_label` | `security_result.detection_fields` | Merged  
`infection_channel_label` | `security_result.detection_fields` | Merged  
`layer_name_label` | `security_result.detection_fields` | Merged  
`layer_uuid_label` | `security_result.detection_fields` | Merged  
`message` | `security_result.detection_fields` | Mapped values (19 total, e.g. `CEF:` → `mitre_execution_label`, `CEF:` → `ifname_label`, `CE...  
`mitre_discovery_label` | `security_result.detection_fields` | Merged  
`mitre_execution_label` | `security_result.detection_fields` | Merged  
`operasjon_label` | `security_result.detection_fields` | Merged  
`operation_label` | `security_result.detection_fields` | Merged  
`permission_label` | `security_result.detection_fields` | Merged  
`policy_label` | `security_result.detection_fields` | Merged  
`policy_time_label` | `security_result.detection_fields` | Merged  
`smartdefense_profile_label` | `security_result.detection_fields` | Merged  
`spyware_Grayware_Type_label` | `security_result.detection_fields` | Merged  
`tags_label` | `security_result.detection_fields` | Merged  
`threat_probability_label` | `security_result.detection_fields` | Merged  
`tillatelse_label` | `security_result.detection_fields` | Merged  
`rule_uid` | `security_result.rule_id` | Directly mapped  
`mwProfile` | `security_result.rule_name` | Directly mapped  
`rule_name` | `security_result.rule_name` | Directly mapped  
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
`action` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`ifdir` | `event.idm.read_only_udm.network.direction` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`vendor_name` | `event.idm.read_only_udm.metadata.vendor_name` | Mapped from changelog  
`src_host` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`smartdefense_profile` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`layer_uuid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`layer_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`precise_error` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`suppressed_logs` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`flags` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`originsicname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sequencenum` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`description_url` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`log_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`performance_impact` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`reject_id_kid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`received_bytes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sent_bytes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ser_agent_kid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`packet_info` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ProductFamily` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`malware_rule_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tags` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`policy_name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`__policy_id_tag.product` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`db_tag` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`mgmt` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`date` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ifname` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`policy` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`policy_time` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`protection_id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`protection_type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`rule` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`sub_policy_name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`sub_policy_uid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`action` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`loguid` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`attack` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`attack_info` | `event.idm.read_only_udm.security_result.threat_name` | Mapped from changelog  
`Attack Info` | `event.idm.read_only_udm.security_result.threat_name` | Mapped from changelog  
`dst` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`lastupdatetime` | `event.idm.read_only_udm.security_result.last_updated_time` | Mapped from changelog  
`protection_name` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`reason` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`src` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`proxy_src_ip` | `event.idm.read_only_udm.principal.nat_ip` | Mapped from changelog  
`received_bytes` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`resource` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`rule_name` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`rule_uid` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`reject_id` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`s_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`sport_svc` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`sent_bytes` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`service` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`svc` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`service_id` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`session_id` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`web_client_type` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`web_client_type` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-smartdefense-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
