---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-stealthwatch/
title: Collect Cisco Secure Network Analytics logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:03.849198+00:00
---

# Collect Cisco Secure Network Analytics logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-stealthwatch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Secure Network Analytics logs

**Parser Version:** 19.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Secure Network Analytics (formerly Stealthwatch) logs to Google Security Operations using the Bindplane agent.

Cisco Secure Network Analytics is a network traffic analysis solution that uses telemetry from your existing network infrastructure to detect threats. It provides visibility into network activity, identifies anomalous behavior, and detects advanced threats such as command-and-control communications, lateral movement, and data exfiltration without the need for agents or additional hardware.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Windows Server 2016 or later, or Linux host with `systemd`.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Cisco Secure Network Analytics Manager (formerly Stealthwatch Management Console).
  * Network connectivity between the Cisco Secure Network Analytics Manager and the Bindplane agent host on UDP port `514` (or your chosen syslog port).



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
          chronicle/cisco_sna:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id-here'
            endpoint: chronicle.googleapis.com
            log_type: CISCO_STEALTHWATCH
            raw_log_field: body
            ingestion_labels:
        
        service:
          pipelines:
            logs/cisco_sna_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/cisco_sna
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on. Use `0.0.0.0` to listen on all interfaces. The port must match the port configured in Cisco Secure Network Analytics (default: `514`).
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from Google SecOps.
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/cisco_sna:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id-here'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CISCO_STEALTHWATCH
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File** > **Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Linux** , run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    2. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * To restart the Bindplane agent in **Windows** , choose one of the following options:

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
             




## Configure Cisco Secure Network Analytics syslog forwarding

  1. Sign in to the **Cisco Secure Network Analytics Manager** (formerly Stealthwatch Management Console).
  2. Go to **Configure** > **Detection Response Management**.
  3. Click the **Actions** tab.
  4. Locate the default **Send to Syslog** action in the list.
  5. Click the ellipsis (**...**) in the **Action** column next to **Send to Syslog** , and then click **Edit**.
  6. Provide the following configuration details: 
     * **Syslog Server Address** : Enter the IP address of the Bindplane agent host.
     * **UDP Port** : Enter `514` (or the port configured in the Bindplane agent `config.yaml`).
     * **Message Format** : Select **CEF**.
  7. Click the blue **Save** button in the upper right corner.
  8. Click the **Rules** tab.
  9. Click **Add New Rule** or edit an existing rule.
  10. Configure the rule conditions to define which alarms trigger the syslog action: 
     * **Host Alarm** : Select alarm categories to forward (for example, **High Concern Index** , **Exfiltration** , **Command and Control**).
     * **Host Group Relationship Alarm** : Select relationship policies to forward (for example, **High Traffic** , **SYN Flood**).
  11. In the **Response Actions** section, select the **Send to Syslog** action.
  12. Click **Save**.
  13. Verify that syslog messages are being received by checking the Bindplane agent logs.

**Note:** Ensure that UDP port `514` (or your chosen syslog port) is permitted on any firewalls or intermediate devices between the Cisco Secure Network Analytics Manager and the Bindplane agent host.



For more information, see the [Cisco Secure Network Analytics documentation](https://www.cisco.com/c/en/us/support/security/stealthwatch/series.html) and the [Response Management syslog configuration guide](https://www.cisco.com/c/en/us/support/docs/security/secure-network-analytics/222868-configure-response-management-to-send-sy.html).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`_about` | `about` | Merged  
`about` | `about` | Merged  
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
`dvcmac` | `about.mac` | Merged  
`mac_address` | `about.mac` | Merged  
`deviceTranslatedAddress` | `about.nat_ip` | Merged  
`Emne` | `about.process.command_line` | Directly mapped  
`Path` | `about.process.command_line` | Directly mapped  
`Subject` | `about.process.command_line` | Directly mapped  
`deviceProcessName` | `about.process.command_line` | Renamed/mapped  
`dvcpid` | `about.process.pid` | Renamed/mapped  
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
`cs5_label` | `additional.fields` | Merged  
`field_` | `additional.fields` | Merged  
`_intermediary` | `intermediary` | Merged  
`data.short_text` | `metadata.description` | Directly mapped  
`desc` | `metadata.description` | Directly mapped  
`description` | `metadata.description` | Directly mapped  
`leef.fullmessage` | `metadata.description` | Directly mapped  
`msg` | `metadata.description` | Renamed/mapped  
`short_text` | `metadata.description` | Directly mapped  
`device_event_class_id` | `metadata.product_event_type` | Directly mapped  
`eventData_id` | `metadata.product_event_type` | Directly mapped  
`event_name` | `metadata.product_event_type` | Directly mapped  
`reportName` | `metadata.product_event_type` | Directly mapped  
`externalId` | `metadata.product_log_id` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`device_product` | `metadata.product_name` | Directly mapped  
`Version` | `metadata.product_version` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`version` | `metadata.product_version` | Directly mapped  
`device_vendor` | `metadata.vendor_name` | Renamed/mapped  
`app_protocol_output` | `network.application_protocol` | Directly mapped  
`protocol` | `network.application_protocol` | Directly mapped  
`method` | `network.http.method` | Directly mapped  
`requestMethod` | `network.http.method` | Renamed/mapped  
`requestClientApplication` | `network.http.user_agent` | Renamed/mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`ServerBytes` | `network.received_bytes` | Renamed/mapped  
`in` | `network.received_bytes` | Renamed/mapped  
`peerBytes` | `network.received_bytes` | Renamed/mapped  
`data.packets_in` | `network.received_packets` | Directly mapped  
`packets_in` | `network.received_packets` | Directly mapped  
`ClientBytes` | `network.sent_bytes` | Renamed/mapped  
`hostBytes` | `network.sent_bytes` | Renamed/mapped  
`out` | `network.sent_bytes` | Renamed/mapped  
`data.packets_out` | `network.sent_packets` | Directly mapped  
`packets_out` | `network.sent_packets` | Directly mapped  
`session_id` | `network.session_id` | Directly mapped  
`SourceModuleType` | `observer.application` | Directly mapped  
`leef_flowCollectorIP` | `observer.asset.ip` | Merged  
`leef.flowCollectorName` | `observer.hostname` | Directly mapped  
`leef_flowCollectorIP` | `observer.ip` | Merged  
`leef.domain` | `principal.administrative_domain` | Directly mapped  
`sntdom` | `principal.administrative_domain` | Renamed/mapped  
`sourceServiceName` | `principal.application` | Renamed/mapped  
`details.title` | `principal.asset.hostname` | Directly mapped  
`hostname` | `principal.asset.hostname` | Directly mapped  
`prin_host` | `principal.asset.hostname` | Directly mapped  
`source_name` | `principal.asset.hostname` | Directly mapped  
`ClientIP` | `principal.asset.ip` | Merged  
`MessageSourceAddress` | `principal.asset.ip` | Merged  
`connected_ip` | `principal.asset.ip` | Merged  
`data.connected_ip` | `principal.asset.ip` | Merged  
`details.ip` | `principal.asset.ip` | Merged  
`host.ipAddress` | `principal.asset.ip` | Merged  
`host_ip` | `principal.asset.ip` | Merged  
`ip` | `principal.asset.ip` | Merged  
`leef.src` | `principal.asset.ip` | Merged  
`prin_ip` | `principal.asset.ip` | Merged  
`sourceIPv4Address` | `principal.asset.ip` | Merged  
`source_name` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`Group_name` | `principal.group.group_display_name` | Directly mapped  
`Gruppenavn` | `principal.group.group_display_name` | Directly mapped  
`Device_name` | `principal.hostname` | Directly mapped  
`Enhetsnavn` | `principal.hostname` | Directly mapped  
`details.title` | `principal.hostname` | Directly mapped  
`hostname` | `principal.hostname` | Directly mapped  
`prin_host` | `principal.hostname` | Directly mapped  
`shost` | `principal.hostname` | Renamed/mapped  
`source_name` | `principal.hostname` | Directly mapped  
`ClientIP` | `principal.ip` | Merged  
`MessageSourceAddress` | `principal.ip` | Merged  
`connected_ip` | `principal.ip` | Merged  
`data.connected_ip` | `principal.ip` | Merged  
`details.ip` | `principal.ip` | Merged  
`host.ipAddress` | `principal.ip` | Merged  
`host_ip` | `principal.ip` | Merged  
`ip` | `principal.ip` | Merged  
`leef.src` | `principal.ip` | Merged  
`prin_ip` | `principal.ip` | Merged  
`principal_ip` | `principal.ip` | Merged  
`shost` | `principal.ip` | Merged  
`sourceIPv4Address` | `principal.ip` | Merged  
`source_name` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`Source_HG` | `principal.location.country_or_region` | Directly mapped  
`host.country` | `principal.location.country_or_region` | Directly mapped  
`leef.sourceHG` | `principal.location.country_or_region` | Directly mapped  
`ClientMAC` | `principal.mac` | Merged  
`mac` | `principal.mac` | Merged  
`source_mac_address` | `principal.mac` | Merged  
`source_info.namespace` | `principal.namespace` | Directly mapped  
`sourceTranslatedAddress` | `principal.nat_ip` | Merged  
`sourceTranslatedPort` | `principal.nat_port` | Renamed/mapped  
`ClientPort` | `principal.port` | Renamed/mapped  
`SourcePort` | `principal.port` | Renamed/mapped  
`data.port` | `principal.port` | Renamed/mapped  
`port` | `principal.port` | Renamed/mapped  
`spt` | `principal.port` | Renamed/mapped  
`sproc` | `principal.process.command_line` | Renamed/mapped  
`process_name` | `principal.process.file.full_path` | Directly mapped  
`process_pid` | `principal.process.pid` | Directly mapped  
`spid` | `principal.process.pid` | Renamed/mapped  
`Source_HostSnapshot` | `principal.url` | Directly mapped  
`leef.sourceHostSnapshot` | `principal.url` | Directly mapped  
`principal_role` | `principal.user.attribute.roles` | Merged  
`actor_email` | `principal.user.email_addresses` | Merged  
`actor_name` | `principal.user.email_addresses` | Merged  
`UserName` | `principal.user.user_display_name` | Directly mapped  
`actor.username` | `principal.user.user_display_name` | Directly mapped  
`data.actor.username` | `principal.user.user_display_name` | Directly mapped  
`source_username` | `principal.user.user_display_name` | Directly mapped  
`suser` | `principal.user.user_display_name` | Directly mapped  
`actor.id` | `principal.user.userid` | Directly mapped  
`data.actor.id` | `principal.user.userid` | Directly mapped  
`suid` | `principal.user.userid` | Renamed/mapped  
`user_name` | `principal.user.userid` | Directly mapped  
`security_res` | `security_result` | Merged  
`security_result` | `security_result` | Merged  
`_action` | `security_result.action` | Merged  
`Action_Taken` | `security_result.action_details` | Directly mapped  
`act` | `security_result.action_details` | Directly mapped  
`cat` | `security_result.category_details` | Merged  
`Scan_Type` | `security_result.description` | Directly mapped  
`Type` | `security_result.description` | Directly mapped  
`msg_data_2` | `security_result.description` | Directly mapped  
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
`dntdom` | `target.administrative_domain` | Renamed/mapped  
`destinationServiceName` | `target.application` | Renamed/mapped  
`target_hostname` | `target.asset.hostname` | Directly mapped  
`DestIPv4Address` | `target.asset.ip` | Merged  
`ServerIP` | `target.asset.ip` | Merged  
`ipt` | `target.asset.ip` | Merged  
`leef.dst` | `target.asset.ip` | Merged  
`peer.ipAddress` | `target.asset.ip` | Merged  
`file_path` | `target.file.full_path` | Directly mapped  
`file_type` | `target.file.mime_type` | Directly mapped  
`target_hostname` | `target.hostname` | Directly mapped  
`temp_dhost` | `target.hostname` | Directly mapped  
`DestIPv4Address` | `target.ip` | Merged  
`IPv6_Address` | `target.ip` | Merged  
`ServerIP` | `target.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`ipt` | `target.ip` | Merged  
`leef.dst` | `target.ip` | Merged  
`peer.ipAddress` | `target.ip` | Merged  
`peer.country` | `target.location.country_or_region` | Directly mapped  
`ServerMAC` | `target.mac` | Merged  
`mac_address` | `target.mac` | Merged  
`target_mac_address` | `target.mac` | Merged  
`destination_translated_address` | `target.nat_ip` | Merged  
`destinationTranslatedPort` | `target.nat_port` | Renamed/mapped  
`DestPort` | `target.port` | Renamed/mapped  
`ServerPort` | `target.port` | Renamed/mapped  
`dpt` | `target.port` | Renamed/mapped  
`dproc` | `target.process.command_line` | Renamed/mapped  
`File_name` | `target.process.file.full_path` | Directly mapped  
`Infected_Resource` | `target.process.file.full_path` | Directly mapped  
`Object` | `target.process.file.full_path` | Directly mapped  
`Objekt` | `target.process.file.full_path` | Directly mapped  
`dpid` | `target.process.pid` | Renamed/mapped  
`process_id` | `target.process.pid` | Directly mapped  
`resource_Type_label` | `target.resource.attribute.labels` | Merged  
`SourceModuleName` | `target.resource.name` | Directly mapped  
`Target_HostSnapshot` | `target.url` | Directly mapped  
`leef.targetHostSnapshot` | `target.url` | Directly mapped  
`request` | `target.url` | Directly mapped  
`target_role` | `target.user.attribute.roles` | Merged  
`CustomerName` | `target.user.user_display_name` | Directly mapped  
`temp_duser` | `target.user.user_display_name` | Directly mapped  
`Bruker` | `target.user.userid` | Directly mapped  
`User_value` | `target.user.userid` | Directly mapped  
`temp_duid` | `target.user.userid` | Directly mapped  
`sid` | `target.user.windows_sid` | Directly mapped  
N/A | `about` | Constant: `about`  
N/A | `about.ip` | Constant: `ips`  
N/A | `about.mac` | Constant: `mac_address`  
N/A | `about.nat_ip` | Constant: `deviceTranslatedAddress`  
N/A | `about.resource.attribute.permissions` | Constant: `permissions`  
N/A | `additional.fields` | Constant: `additional_eventId`  
N/A | `intermediary` | Constant: `_intermediary`  
N/A | `metadata.event_type` | Constant: `PROCESS_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `Cisco Stealthwatch`  
N/A | `metadata.vendor_name` | Constant: `Cisco`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `network.ip_protocol` | Constant: `TCP`  
N/A | `observer.asset.ip` | Constant: `leef_flowCollectorIP`  
N/A | `observer.ip` | Constant: `leef_flowCollectorIP`  
N/A | `principal.asset.ip` | Constant: `host_ip`  
N/A | `principal.ip` | Constant: `host_ip`  
N/A | `principal.mac` | Constant: `mac`  
N/A | `principal.nat_ip` | Constant: `sourceTranslatedAddress`  
N/A | `principal.user.attribute.roles` | Constant: `principal_role`  
N/A | `principal.user.email_addresses` | Constant: `actor_name`  
N/A | `security_result` | Constant: `security_result`  
N/A | `security_result.action` | Constant: `_action`  
N/A | `security_result.category_details` | Constant: `cat`  
N/A | `security_result.detection_fields` | Constant: `operation_label`  
N/A | `security_result.severity` | Constant: `LOW`  
N/A | `src.resource.attribute.permissions` | Constant: `old_permissions`  
N/A | `target.asset.ip` | Constant: `leef.dst`  
N/A | `target.ip` | Constant: `leef.dst`  
N/A | `target.mac` | Constant: `mac_address`  
N/A | `target.nat_ip` | Constant: `destination_translated_address`  
N/A | `target.resource.attribute.labels` | Constant: `resource_Type_label`  
N/A | `target.user.attribute.roles` | Constant: `target_role`  
`ProtocolIdentifier` | `network.ip_protocol` | Mapped from changelog  
`inputSNMPIface", "outputSNMPIface", "InPackets` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-stealthwatch-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
