---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kaspersky-av/
title: Collect Kaspersky Endpoint Security logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:41.226692+00:00
---

# Collect Kaspersky Endpoint Security logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kaspersky-av/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Kaspersky Endpoint Security logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can ingest Kaspersky Endpoint Security logs to Google Security Operations using Bindplane. Kaspersky Endpoint Security provides multi-layered protection against malware, ransomware, exploits, and advanced threats on endpoints running Windows, macOS, and Linux. Kaspersky Security Center (KSC) is the centralized management console that aggregates events from all managed endpoints and supports syslog forwarding for SIEM integration.

**Note:** Kaspersky products are subject to trade restrictions and may not be available in all countries or regions. Verify compliance with applicable regulations before deployment.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Kaspersky Security Center (KSC) Administration Console or Web Console.
  * Kaspersky Security Center 14 or later with the SIEM Integration component installed.



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

## Configure Bindplane Agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           tcplog:
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
             customer_id: <PLACEHOLDER_CUSTOMER_ID>
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'KASPERSKY_AV'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/chronicle_w_labels
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace `<PLACEHOLDER_CUSTOMER_ID>` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in the **Get Google SecOps credentials for the Bindplane agent** section.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: <PLACEHOLDER_CUSTOMER_ID>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'KASPERSKY_AV'
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
         




## Configure Kaspersky Security Center syslog forwarding

  1. Sign in to the **Kaspersky Security Center Web Console** or open the **Administration Console** (MMC).
  2. Go to **Administration Server > Properties** (or right-click the Administration Server node and select **Properties**).
  3. In the properties window, go to **Event export > SIEM**.
  4. Select the **Automatically export events to SIEM system database** checkbox.
  5. Provide the following configuration details: 
     * **SIEM system** : Select **Other**.
     * **SIEM system server address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **SIEM system server port** : Enter `514` (or the port configured in Bindplane).
     * **Protocol** : Select **TCP**.
     * **Format** : Select **Syslog** (CEF format).
  6. Click **Events to export** to select which event categories to forward:

     1. Select **Critical events** checkbox.
     2. Select **Functional failure** checkbox.
     3. Select **Warning** checkbox.
     4. Select **Info** checkbox.
**Note:** At minimum, enable **Critical events** and **Functional failure** categories. Select all categories for comprehensive monitoring.
  7. Click **OK** to save the SIEM export configuration.

  8. Go to **Administration Server > Events**.

  9. Verify that events appear and that syslog delivery is active by checking the Bindplane agent logs.




For additional details, refer to the [Kaspersky Security Center documentation on SIEM integration](https://support.kaspersky.com/KSC/14.2/en-US/151657.htm).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`message` | `about` | Mapped: `CEF:0` → `about`  
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
`message` | `about.ip` | Mapped: `CEF:0` → `ips`  
`dvc_mac` | `about.mac` | Mapped: `slot` → `mac_address`  
`dvcmac` | `about.mac` | Merged  
`mac_address` | `about.mac` | Merged  
`message` | `about.mac` | Mapped: `CEF:0` → `mac_address`, `CEF:0` → `dvcmac`  
`deviceTranslatedAddress` | `about.nat_ip` | Merged  
`message` | `about.nat_ip` | Mapped: `CEF:0` → `deviceTranslatedAddress`  
`Emne` | `about.process.command_line` | Directly mapped  
`Path` | `about.process.command_line` | Directly mapped  
`Subject` | `about.process.command_line` | Directly mapped  
`deviceProcessName` | `about.process.command_line` | Renamed/mapped  
`dvcpid` | `about.process.pid` | Renamed/mapped  
`message` | `about.resource.attribute.permissions` | Mapped: `CEF:0` → `permissions`  
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
`cn1_label` | `additional.fields` | Merged  
`cs2` | `additional.fields` | Mapped: `arc_test` → `additional_cs2`  
`cs5_label` | `additional.fields` | Merged  
`cs9_label` | `additional.fields` | Merged  
`event_component_label` | `additional.fields` | Merged  
`event_type_label` | `additional.fields` | Merged  
`kl_event_status_label` | `additional.fields` | Merged  
`message` | `additional.fields` | Mapped values (25 total, e.g. `CEF:0` → `additional_eventId`, `CEF:0` → `additional_devicePa...  
`tdn_label` | `additional.fields` | Merged  
`message` | `extensions.vulns.vulnerabilities` | Mapped: `CEF:0` → `vulnerabilities`  
`vulnerabilities` | `extensions.vulns.vulnerabilities` | Merged  
`message` | `intermediary` | Mapped: `CEF:0` → `intermediary`  
`intermediary_host` | `intermediary.hostname` | Directly mapped  
`intermediary_hostname` | `intermediary.hostname` | Directly mapped  
`meta_description` | `metadata.description` | Directly mapped  
`msg` | `metadata.description` | Renamed/mapped  
`Generated` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`Received` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`formatted_timestamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss Z`  
`rt` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`ts` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event_name` | `metadata.event_type` | Mapped: `"LogSpyware","LogPredictiveMachineLearning"` → `SCAN_UNCATEGORIZED`  
`event_type` | `metadata.event_type` | Directly mapped  
`event_type_set` | `metadata.event_type` | Mapped: `false` → `NETWORK_CONNECTION`, `false` → `STATUS_UPDATE`  
`message` | `metadata.event_type` | Mapped values (7 total, e.g. `CEF:0` → `PROCESS_UNCATEGORIZED`, `CEF:0` → `SCAN_UNCATEGORIZE...  
`target_hostname_present` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`device_event_class_id` | `metadata.product_event_type` | Directly mapped  
`et` | `metadata.product_event_type` | Directly mapped  
`event_name` | `metadata.product_event_type` | Directly mapped  
`product_event_type` | `metadata.product_event_type` | Directly mapped  
`externalId` | `metadata.product_log_id` | Directly mapped  
`device_product` | `metadata.product_name` | Directly mapped  
`message` | `metadata.product_name` | Mapped: `CEF:0` → `SecurityCenter`, `CEF:0` → `KASPERSKY_AV`  
`device_version` | `metadata.product_version` | Directly mapped  
`device_vendor` | `metadata.vendor_name` | Renamed/mapped  
`message` | `metadata.vendor_name` | Mapped: `CEF:0` → `KasperskyLab`, `CEF:0` → `KASPERSKY`  
`app_protocol_output` | `network.application_protocol` | Directly mapped  
`message` | `network.application_protocol` | Mapped: `CEF:0` → `HTTP`  
`protocol` | `network.application_protocol` | Mapped: `(?i)http` → `HTTP`  
`deviceDirection` | `network.direction` | Mapped: `0` → `INBOUND`, `1` → `OUTBOUND`  
`message` | `network.direction` | Mapped: `CEF:0` → `INBOUND`, `CEF:0` → `OUTBOUND`  
`method` | `network.http.method` | Directly mapped  
`requestMethod` | `network.http.method` | Renamed/mapped  
`url` | `network.http.referral_url` | Directly mapped  
`Application` | `network.http.user_agent` | Directly mapped  
`description` | `network.http.user_agent` | Directly mapped  
`requestClientApplication` | `network.http.user_agent` | Renamed/mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`in` | `network.received_bytes` | Renamed/mapped  
`out` | `network.sent_bytes` | Renamed/mapped  
`domain` | `principal.administrative_domain` | Directly mapped  
`sntdom` | `principal.administrative_domain` | Renamed/mapped  
`sourceServiceName` | `principal.application` | Renamed/mapped  
`ip` | `principal.asset.ip` | Merged  
`message` | `principal.asset.ip` | Mapped: `CEF:0` → `ip`  
`Group_name` | `principal.group.group_display_name` | Directly mapped  
`Gruppenavn` | `principal.group.group_display_name` | Directly mapped  
`Device_name` | `principal.hostname` | Directly mapped  
`Enhetsnavn` | `principal.hostname` | Directly mapped  
`description` | `principal.hostname` | Directly mapped  
`hdn` | `principal.hostname` | Directly mapped  
`host_name` | `principal.hostname` | Directly mapped  
`shost` | `principal.hostname` | Renamed/mapped  
`hip` | `principal.ip` | Merged  
`ip` | `principal.ip` | Merged  
`message` | `principal.ip` | Mapped: `CEF:0` → `principal_ip`, `CEF:0` → `shost`, `CEF:0` → `ip`, `CEF:0` → `hip`  
`principal_ip` | `principal.ip` | Merged  
`shost` | `principal.ip` | Merged  
`mac` | `principal.mac` | Merged  
`message` | `principal.mac` | Mapped: `CEF:0` → `mac`  
`message` | `principal.nat_ip` | Mapped: `CEF:0` → `sourceTranslatedAddress`  
`sourceTranslatedAddress` | `principal.nat_ip` | Merged  
`sourceTranslatedPort` | `principal.nat_port` | Renamed/mapped  
`spt` | `principal.port` | Renamed/mapped  
`sproc` | `principal.process.command_line` | Renamed/mapped  
`Process ID` | `principal.process.pid` | Directly mapped  
`spid` | `principal.process.pid` | Renamed/mapped  
`message` | `principal.user.attribute.roles` | Mapped: `CEF:0` → `principal_role`  
`principal_role` | `principal.user.attribute.roles` | Merged  
`p7` | `principal.user.user_display_name` | Directly mapped  
`suser` | `principal.user.user_display_name` | Directly mapped  
`user_name` | `principal.user.user_display_name` | Directly mapped  
`username` | `principal.user.user_display_name` | Directly mapped  
`suid` | `principal.user.userid` | Renamed/mapped  
`message` | `security_result` | Mapped: `CEF:0` → `security_result`  
`gn_label` | `security_result.about.labels` | Merged  
`label_task_name` | `security_result.about.labels` | Merged  
`message` | `security_result.about.labels` | Mapped: `CEF:0` → `gn_label`, `CEF:0` → `rtid_labels`, `CEF:0` → `label_task_name`  
`rtid_labels` | `security_result.about.labels` | Merged  
`_action` | `security_result.action` | Merged  
`act` | `security_result.action` | Mapped: `accept` → `_action`, `deny` → `_action`  
`message` | `security_result.action` | Mapped: `CEF:0` → `_action`, `CEF:0` → `sr_action`  
`sr_action` | `security_result.action` | Merged  
`Action_Taken` | `security_result.action_details` | Directly mapped  
`act` | `security_result.action_details` | Directly mapped  
`Content category` | `security_result.category_details` | Merged  
`cat` | `security_result.category_details` | Merged  
`et` | `security_result.category_details` | Merged  
`message` | `security_result.category_details` | Mapped: `CEF:0` → `cat`, `CEF:0` → `Content category`, `CEF:0` → `et`  
`Result description` | `security_result.description` | Renamed/mapped  
`Rule` | `security_result.description` | Directly mapped  
`Scan_Type` | `security_result.description` | Directly mapped  
`Type` | `security_result.description` | Directly mapped  
`description` | `security_result.description` | Directly mapped  
`label` | `security_result.description` | Directly mapped  
`msg_data_2` | `security_result.description` | Directly mapped  
`bid_id_label` | `security_result.detection_fields` | Merged  
`certificate_verification_status_label` | `security_result.detection_fields` | Merged  
`et2_label` | `security_result.detection_fields` | Merged  
`exchange_label` | `security_result.detection_fields` | Merged  
`ifm_ori_label` | `security_result.detection_fields` | Merged  
`infection_channel_label` | `security_result.detection_fields` | Merged  
`message` | `security_result.detection_fields` | Mapped values (20 total, e.g. `CEF:0` → `operation_label`, `CEF:0` → `operasjon_label`, `CEF...  
`object_name_label` | `security_result.detection_fields` | Merged  
`object_path_label` | `security_result.detection_fields` | Merged  
`object_type_label` | `security_result.detection_fields` | Merged  
`operasjon_label` | `security_result.detection_fields` | Merged  
`operation_label` | `security_result.detection_fields` | Merged  
`permission_label` | `security_result.detection_fields` | Merged  
`pub_label` | `security_result.detection_fields` | Merged  
`publisher_id_label` | `security_result.detection_fields` | Merged  
`sec_id_label` | `security_result.detection_fields` | Merged  
`site_id_label` | `security_result.detection_fields` | Merged  
`spyware_Grayware_Type_label` | `security_result.detection_fields` | Merged  
`threat_probability_label` | `security_result.detection_fields` | Merged  
`tillatelse_label` | `security_result.detection_fields` | Merged  
`xrtb_id_label` | `security_result.detection_fields` | Merged  
`mwProfile` | `security_result.rule_name` | Directly mapped  
`p5` | `security_result.rule_name` | Directly mapped  
`message` | `security_result.severity` | Mapped: `CEF:0` → `LOW`, `CEF:0` → `MEDIUM`, `CEF:0` → `HIGH`, `CEF:0` → `CRITICAL`  
`severity` | `security_result.severity` | Mapped: `"0", "1", "2", "3", "LOW"` → `LOW`, `"4", "5", "6", "MEDIUM", "SUBSTANTIAL", "INFO"...  
`Erreur` | `security_result.summary` | Directly mapped  
`Reason` | `security_result.summary` | Directly mapped  
`Result` | `security_result.summary` | Directly mapped  
`appcategory` | `security_result.summary` | Directly mapped  
`cs10` | `security_result.summary` | Directly mapped  
`reason` | `security_result.summary` | Renamed/mapped  
`summary` | `security_result.summary` | Directly mapped  
`Spyware` | `security_result.threat_name` | Directly mapped  
`Type` | `security_result.threat_name` | Directly mapped  
`Unknown_Threat` | `security_result.threat_name` | Directly mapped  
`Virus_Malware_Name` | `security_result.threat_name` | Directly mapped  
`oldFilePath` | `src.file.full_path` | Renamed/mapped  
`oldFileSize` | `src.file.size` | Renamed/mapped  
`message` | `src.resource.attribute.permissions` | Mapped: `CEF:0` → `old_permissions`  
`old_permissions` | `src.resource.attribute.permissions` | Merged  
`dntdom` | `target.administrative_domain` | Renamed/mapped  
`destinationServiceName` | `target.application` | Renamed/mapped  
`name` | `target.file.full_path` | Directly mapped  
`file_name` | `target.file.names` | Merged  
`message` | `target.file.names` | Mapped: `CEF:0` → `file_name`  
`temp_dhost` | `target.hostname` | Directly mapped  
`IPv6_Address` | `target.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`ipv6` | `target.ip` | Mapped: `-` → `IPv6_Address`  
`message` | `target.ip` | Mapped: `CEF:0` → `dst_ip`, `CEF:0` → `IPv6_Address`  
`mac_address` | `target.mac` | Merged  
`message` | `target.mac` | Mapped: `CEF:0` → `mac_address`  
`destination_translated_address` | `target.nat_ip` | Merged  
`message` | `target.nat_ip` | Mapped: `CEF:0` → `destination_translated_address`  
`destinationTranslatedPort` | `target.nat_port` | Renamed/mapped  
`dpt` | `target.port` | Renamed/mapped  
`dproc` | `target.process.command_line` | Renamed/mapped  
`Application path` | `target.process.file.full_path` | Directly mapped  
`File_name` | `target.process.file.full_path` | Directly mapped  
`Infected_Resource` | `target.process.file.full_path` | Directly mapped  
`Name` | `target.process.file.full_path` | Directly mapped  
`Nom` | `target.process.file.full_path` | Directly mapped  
`Object` | `target.process.file.full_path` | Directly mapped  
`Objekt` | `target.process.file.full_path` | Directly mapped  
`application_path` | `target.process.file.full_path` | Directly mapped  
`p2` | `target.process.file.full_path` | Directly mapped  
`MD5` | `target.process.file.md5` | Directly mapped  
`MD5 file hash` | `target.process.file.md5` | Directly mapped  
`md5` | `target.process.file.md5` | Directly mapped  
`File SHA256 hash` | `target.process.file.sha256` | Directly mapped  
`SHA256` | `target.process.file.sha256` | Directly mapped  
`p1` | `target.process.file.sha256` | Directly mapped  
`dpid` | `target.process.pid` | Renamed/mapped  
`process_id` | `target.process.pid` | Directly mapped  
`cs4_label` | `target.resource.attribute.labels` | Merged  
`message` | `target.resource.attribute.labels` | Mapped: `CEF:0` → `resource_Type_label`, `CEF:0` → `cs4_label`  
`resource_Type_label` | `target.resource.attribute.labels` | Merged  
`Component` | `target.resource.name` | Directly mapped  
`message` | `target.resource.type` | Mapped: `CEF:0` → `DATABASE`, `Content category source` → `DATABASE`  
`source` | `target.resource.type` | Mapped: `databases` → `DATABASE`  
`Requested web page` | `target.url` | Directly mapped  
`request` | `target.url` | Directly mapped  
`message` | `target.user.attribute.roles` | Mapped: `CEF:0` → `target_role`  
`target_role` | `target.user.attribute.roles` | Merged  
`CustomerName` | `target.user.user_display_name` | Directly mapped  
`temp_duser` | `target.user.user_display_name` | Directly mapped  
`Bruker` | `target.user.userid` | Directly mapped  
`User_value` | `target.user.userid` | Directly mapped  
`temp_duid` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `PROCESS_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `SecurityCenter`  
N/A | `metadata.vendor_name` | Constant: `KasperskyLab`  
N/A | `network.application_protocol` | Constant: `HTTP`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `security_result.severity` | Constant: `LOW`  
N/A | `target.resource.type` | Constant: `DATABASE`  
`cs9` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cn1` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kl_event_status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs10` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`cs4` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`vendor_name` | `event.idm.read_only_udm.metadata.vendor_name` | Mapped from changelog  
`product_name` | `event.idm.read_only_udm.metadata.product_name` | Mapped from changelog  
`Event_Component` | `additional.fields` | Mapped from changelog  
`EventType` | `additional.fields` | Mapped from changelog  
`threat_level` | `vulnerabilities.severity_details` | Mapped from changelog  
`Hachage SHA256", "p1` | `target.process.file.sha256` | Mapped from changelog  
`Hachage MD5", "md5` | `target.process.file.md5` | Mapped from changelog  
`intermediary` | `event.idm.read_only_udm.intermediary` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kaspersky-av-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
