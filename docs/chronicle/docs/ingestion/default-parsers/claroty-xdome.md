---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/claroty-xdome/
title: Collect Claroty xDome logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:37.115079+00:00
---

# Collect Claroty xDome logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/claroty-xdome/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Claroty xDome logs

**Parser Version:** 9.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Claroty xDome logs to Google Security Operations using the Bindplane agent.

The parser extracts fields from Claroty xDome syslog formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Claroty xDome management console or appliance



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

For additional installation options, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File: 
     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:



### Option A: UDP configuration (less secure)

  * **Note:** Using UDP, especially the "send from cloud" option sends security data unencrypted and might allow attackers to intercept data.
        
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
            log_type: 'CLAROTY_XDOME'
            raw_log_field: body
            ingestion_labels:
        
        service:
          pipelines:
            logs/source0__chronicle_w_labels-0:
              receivers:
                - udplog
              exporters:
                - chronicle/chronicle_w_labels
        




### Option B: TCP with TLS configuration (recommended for security)

  * The TCP with TLS configuration:
        
        receivers:
          tcplog:
            # Replace the port and IP address as required
            listen_address: "0.0.0.0:514"
            tls:
              # Path to the server's public TLS certificate file when using self-signed certificates
              cert_file: /etc/bindplane/certs/cert.pem
              key_file: /etc/bindplane/certs/key.pem
        
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
            log_type: 'CLAROTY_XDOME'
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

  * Replace `<customer_id>` with the actual Customer ID.

  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.

  * For TLS configuration, ensure the certificate files exist at the specified paths or generate self-signed certificates if needed.




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
            log_type: 'CLAROTY_XDOME'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




### Detailed Syslog configuration

  1. Sign in to the **Claroty xDome** Web UI.
  2. Click the **Settings** tab in the navigation bar.
  3. Select **System Settings** from the drop-down menu.
  4. Click **My Integrations** in the Integrations section.
  5. Click **\+ Add Integration**.
  6. Select **Internal Services** from the Category drop-down menu.
  7. Select **SIEM** and **Syslog** from the Integration drop-down menu.
  8. Click **Add**.
  9. Enter the following configuration details: 
     * **Destination IP** : Enter the Bindplane agent IP address.
     * **Transport Protocol** : Select **UDP** or **TCP** , or **TLS** depending on your Bindplane configuration.
     * If you select the TLS security protocol, do the following: 
       * Check the **Check Hostnames** option to verify if the server's hostname matches any of the names present in the **X.509 certificate**.
       * Check the **Use Custom Certificate Authority** option to use a custom Certificate Authority (CA) instead of the default CA. Upload the custom certificate file or insert the certificate (in PEM format) into the space provided.
     * **Destination Port** : The default value for TCP, TLS, and UDP is **514**. (Hover over the field to use the clickable arrows to select a different destination port).
     * **Advanced Options** : Enter the Advanced Options settings: 
       * **Message Format** : Select **CEF** (other options include JSON, or LEEF format).
       * **Syslog Protocol Standard** : Select **RFC 5424** or **RFC 3164**.
     * **Integration Name** : Enter a meaningful name for the integration (for example, `Google SecOps syslog`).
     * **Deployment options** : Select **Run from the collection server** or **Run from the cloud** option depending on your xDome configuration.
  10. Go to the **Integration Tasks** parameters.
  11. Turn on the **Export Claroty xDome Communication Events Using Syslog** option to enable exporting Claroty xDome communication events.
  12. From the **Event Types Selection** drop-down menu, click **Select All**.
  13. **Choose the device conditions to export** : Select **All Devices** option to export the communication event data of all affected devices.

**Note:** To receive OT Activity events through Syslog, it's necessary to create and enable OT Activity Alerts for the relevant event types. This is because xDome only sends events related to alerts for OT Activity.
  14. Turn on the **Export Claroty xDome Device Changes Alerts Change Log to Syslog** option to export Claroty xDome change events.

  15. In the **Change Event Types Selection** drop-down, select the **change event types** you want to export.

  16. **Choose the device conditions you want to export** : Select **All Devices** to export the change event data of all the affected devices.

  17. Turn on the **Export Claroty xDome Alert Information for Affected Devices Using Syslog** option to export alert information for any alert type, including custom alerts.

  18. From **Alert Types** , click **Select All**.

  19. Turn on the **Export Claroty xDome Vulnerability Information for Affected Devices Using Syslog** option to export Claroty xDome vulnerability types.

  20. In the **Vulnerability Types Selection** drop-down menu, select the **vulnerability types** you want to export.

  21. Specify the **CVSS Threshold** number. This parameter allows you to set a CVSS threshold to send a vulnerability using Syslog. (Only vulnerabilities greater or equal to this threshold will be exported. The threshold will revert to the CVSS V3 Base Score by default and CVSS V2 Base Score if the CVSS V3 score is unknown).

  22. **Choose the device conditions to export** : Select **All Devices** to export the data of all affected devices.

  23. Turn on the **Export Claroty xDome Server Incidents Information to Syslog** option to export Claroty xDome server incidents.

  24. Select the collection server types you want to export from the **Collection Server Selection** drop-down menu.

  25. Select the server incidents you want to export on the **Server Incidents Selection** drop-down menu.

  26. Click **Apply** to save the configuration settings.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`add_alert_id` | `additional.fields` | Merged  
`additional_data` | `additional.fields` | Merged  
`affected_device_data_available` | `additional.fields` | Mapped: `true` → `additional_data`  
`alert_info_firmware_device_type_label` | `additional.fields` | Merged  
`alert_info_firmware_model_label` | `additional.fields` | Merged  
`alert_info_latest_software_version_label` | `additional.fields` | Merged  
`alert_type_label` | `additional.fields` | Merged  
`destination_printJobName_label` | `additional.fields` | Merged  
`destination_printedFilesBackupPath_label` | `additional.fields` | Merged  
`destination_printerName_label` | `additional.fields` | Merged  
`device_connection_type_list_label` | `additional.fields` | Merged  
`device_managed_device_label` | `additional.fields` | Merged  
`device_network_list_label` | `additional.fields` | Merged  
`device_type_family_label` | `additional.fields` | Merged  
`device_vulnerability_manufacturer_remediation_info_label` | `additional.fields` | Merged  
`device_vulnerability_relevance_source_label` | `additional.fields` | Merged  
`evnt_action_label` | `additional.fields` | Merged  
`firmware_device_type_label` | `additional.fields` | Merged  
`firmware_model_label` | `additional.fields` | Merged  
`firmware_original_versions` | `additional.fields` | Merged  
`latest_hardware_version_label` | `additional.fields` | Merged  
`latest_software_version_label` | `additional.fields` | Merged  
`map_field` | `additional.fields` | Merged  
`original_hardware_version_label` | `additional.fields` | Merged  
`original_software_version_label` | `additional.fields` | Merged  
`process_owner_label` | `additional.fields` | Merged  
`vulnerability_release_date_label` | `additional.fields` | Merged  
`comm_tuple_server_port` | `intermediary.port` | Directly mapped  
`server_port` | `intermediary.port` | Directly mapped  
`event_description` | `metadata.description` | Directly mapped  
`evnt_description` | `metadata.description` | Directly mapped  
`devTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ssZZ`  
`evnt.ingested` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`evnt.inserted` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`  
`evnt.timestamp` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`ts` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`vulnerability_info.release_date` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSSSSZZ`  
`msg_category` | `metadata.event_type` | Mapped: `vulnerability_affected_device` → `SCAN_VULN_HOST`  
`msg_category` | `metadata.product_event_type` | Directly mapped  
`sub_category` | `metadata.product_event_type` | Directly mapped  
`event_id` | `metadata.product_log_id` | Directly mapped  
`evnt_id` | `metadata.product_log_id` | Directly mapped  
`version` | `metadata.product_version` | Directly mapped  
`app_protocol_output` | `network.application_protocol` | Directly mapped  
`evnt_extra_info.ip_protocol` | `network.ip_protocol` | Directly mapped  
`observer_hostname` | `observer.hostname` | Directly mapped  
`event_observer_label` | `observer.labels` | Merged  
`group` | `principal.administrative_domain` | Directly mapped  
`affected_device.asset_id` | `principal.asset.asset_id` | Directly mapped  
`user_deviceUid` | `principal.asset.asset_id` | Directly mapped  
`affected_device_app_version_label` | `principal.asset.attribute.labels` | Merged  
`affected_device_device_subcategory_label` | `principal.asset.attribute.labels` | Merged  
`affected_device_device_type_family_label` | `principal.asset.attribute.labels` | Merged  
`affected_device_device_type_label` | `principal.asset.attribute.labels` | Merged  
`affected_device_retired_label` | `principal.asset.attribute.labels` | Merged  
`affected_device_risk_score_label` | `principal.asset.attribute.labels` | Merged  
`alert_info_firmware_manufacturer_label` | `principal.asset.attribute.labels` | Merged  
`connection_type_list_label` | `principal.asset.attribute.labels` | Merged  
`device_retired_label` | `principal.asset.attribute.labels` | Merged  
`device_subcategory_label` | `principal.asset.attribute.labels` | Merged  
`device_type_label` | `principal.asset.attribute.labels` | Merged  
`firmware_manufacturer_label` | `principal.asset.attribute.labels` | Merged  
`network_list_label` | `principal.asset.attribute.labels` | Merged  
`affected_device_device_category` | `principal.asset.category` | Directly mapped  
`device_category` | `principal.asset.category` | Directly mapped  
`hardware` | `principal.asset.hardware` | Merged  
`device_name` | `principal.asset.hostname` | Directly mapped  
`management_ip` | `principal.asset.ip` | Merged  
`mac_check` | `principal.asset.mac` | Merged  
`device_asset_id` | `principal.asset.network_domain` | Directly mapped  
`affected_device_os` | `principal.asset.platform_software.platform` | Mapped: `windows` → `WINDOWS`, `linux` → `LINUX`, `mac` → `MAC`  
`device_os` | `principal.asset.platform_software.platform` | Mapped: `windows` → `WINDOWS`, `linux` → `LINUX`, `mac` → `MAC`  
`source_operatingSystem` | `principal.asset.platform_software.platform` | Mapped: `windows` → `WINDOWS`, `linux` → `LINUX`, `mac` → `MAC`  
`affected_device_uid` | `principal.asset.product_object_id` | Directly mapped  
`device_uid` | `principal.asset.product_object_id` | Directly mapped  
`software` | `principal.asset.software` | Merged  
`device_name` | `principal.hostname` | Directly mapped  
`principal_hostname` | `principal.hostname` | Directly mapped  
`management_ip` | `principal.ip` | Merged  
`evnt_extra_info_geo_location` | `principal.location.city` | Directly mapped  
`comm_tuple_src_mac` | `principal.mac` | Merged  
`mac_check` | `principal.mac` | Merged  
`mac_list` | `principal.mac` | Merged  
`srcMAC` | `principal.mac` | Merged  
`affected_device.site_name` | `principal.namespace` | Directly mapped  
`device_site_name` | `principal.namespace` | Directly mapped  
`comm_tuple_src_port` | `principal.port` | Directly mapped  
`srcPort` | `principal.port` | Directly mapped  
`device_note_label` | `principal.resource.attribute.labels` | Merged  
`password_length_label` | `principal.resource.attribute.labels` | Merged  
`username_label` | `principal.user.attribute.labels` | Merged  
`user_id` | `principal.user.product_object_id` | Directly mapped  
`user_email` | `principal.user.userid` | Directly mapped  
`file_changeType_label` | `security_result.about.resource.attribute.labels` | Merged  
`tactics_data` | `security_result.attack_details.tactics` | Merged  
`technique_data` | `security_result.attack_details.techniques` | Merged  
`alert_category` | `security_result.category_details` | Merged  
`alertcategory` | `security_result.category_details` | Merged  
`alert_info_signature_confidence` | `security_result.confidence_score` | Directly mapped  
`evnt_extra_info_ids_signature_info_signature_confidence` | `security_result.confidence_score` | Directly mapped  
`alert_description` | `security_result.description` | Directly mapped  
`alertdescription` | `security_result.description` | Directly mapped  
`alert_device_status_label` | `security_result.detection_fields` | Merged  
`alert_info_signature_severity_description` | `security_result.detection_fields` | Merged  
`alert_type_name_label` | `security_result.detection_fields` | Merged  
`alertdevice_status_label` | `security_result.detection_fields` | Merged  
`device_vulnerability_manufacturer_remediation_info_source_label` | `security_result.detection_fields` | Merged  
`device_vulnerability_overall_cvss_v3_score_label` | `security_result.detection_fields` | Merged  
`device_vulnerability_relevance_label` | `security_result.detection_fields` | Merged  
`event_vector_label` | `security_result.detection_fields` | Merged  
`key` | `security_result.detection_fields` | Mapped: `"signature_first_released", "signature_last_updated", "signature_last_updated_by_sy...  
`map_field` | `security_result.detection_fields` | Merged  
`risk_indicator_id_label` | `security_result.detection_fields` | Merged  
`risk_indicator_name_label` | `security_result.detection_fields` | Merged  
`risk_indicator_weight_label` | `security_result.detection_fields` | Merged  
`vulnerability_affected_products_label` | `security_result.detection_fields` | Merged  
`vulnerability_device_info_overall_cvss_v3_score_label` | `security_result.detection_fields` | Merged  
`vulnerability_device_info_relevance_label` | `security_result.detection_fields` | Merged  
`vulnerability_device_info_relevance_source_label` | `security_result.detection_fields` | Merged  
`vulnerability_info_affected_products_label` | `security_result.detection_fields` | Merged  
`vulnerability_info_is_known_exploited_label` | `security_result.detection_fields` | Merged  
`vulnerability_info_known_exploits_label` | `security_result.detection_fields` | Merged  
`vulnerability_info_name_label` | `security_result.detection_fields` | Merged  
`vulnerability_info_type_label` | `security_result.detection_fields` | Merged  
`vulnerability_is_known_exploited_label` | `security_result.detection_fields` | Merged  
`vulnerability_known_exploits_label` | `security_result.detection_fields` | Merged  
`vulnerability_type_label` | `security_result.detection_fields` | Merged  
`risk.score` | `security_result.risk_score` | Directly mapped  
`signature_id` | `security_result.rule_id` | Directly mapped  
`rule_name` | `security_result.rule_name` | Directly mapped  
`alert_info_signature_active_rev` | `security_result.rule_version` | Directly mapped  
`event_extra_info_ids_signature_info_signature_active_rev` | `security_result.rule_version` | Directly mapped  
`vulnerability_note` | `security_result.summary` | Directly mapped  
`client_id` | `target.asset.asset_id` | Directly mapped  
`evnt_extra_info_client_id` | `target.asset.asset_id` | Directly mapped  
`comm_tuple_dst_mac` | `target.mac` | Merged  
`dstMAC` | `target.mac` | Merged  
`comm_tuple_dst_port` | `target.port` | Directly mapped  
`dstPort` | `target.port` | Directly mapped  
N/A | `extensions.vulns.vulnerabilities` | Constant: `vulnerabilities`  
N/A | `metadata.event_type` | Constant: `NETWORK_CONNECTION`  
N/A | `metadata.product_name` | Constant: `xDome`  
N/A | `metadata.vendor_name` | Constant: `Claroty`  
N/A | `principal.asset.ip` | Constant: `principal_ips`  
N/A | `principal.asset.platform_software.platform` | Constant: `WINDOWS`  
N/A | `principal.ip` | Constant: `principal_ips`  
N/A | `security_result.severity` | Constant: `CRITICAL`  
N/A | `target.asset.ip` | Constant: `target_ips`  
N/A | `target.ip` | Constant: `target_ips`  
`evnt_extra_info.policy_info.policy_pair` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`signature_tag` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`management_status` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`certificate_type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`signature_severity_description` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`policy_pair` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`communication_type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`flow` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`body_content` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`distance` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`reference` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`sid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`rev` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`link` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`asset_id` | `event.idm.read_only_udm.target.asset.asset_id` | Mapped from changelog  
`uid` | `event.idm.read_only_udm.target.asset.product_object_id` | Mapped from changelog  
`mac` | `event.idm.read_only_udm.target.asset.mac` | Mapped from changelog  
`ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`side_b_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`device_category_data` | `event.idm.read_only_udm.target.asset.category` | Mapped from changelog  
`other_device_device_subcategory` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`other_device_device_type` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`other_device_device_type_family` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`other_device_risk_score` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`site_name` | `event.idm.read_only_udm.target.location.name` | Mapped from changelog  
`other_device_device_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`other_device_connection_type_list` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`thumbprint` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`expiry_date` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`start_date` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`OU` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`O` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`C` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ST` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`L` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`mode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`side_b_port` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`evnt_extra_info_direction` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`side_a_port` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`manufacturer` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`network_list` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`other_device_os` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`CN` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`affected_device_management_status` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`assignees` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`affected_device_os` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`sender_id` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`source_username` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`comm_tuple_protocol` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`protocol` | `event.idm.read_only_udm.network.tls.version` | Mapped from changelog  
`side_a_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`side_a_mac` | `event.idm.read_only_udm.principal.mac` | Mapped from changelog  
`affectedmac` | `event.idm.read_only_udm.principal.mac` | Mapped from changelog  
`evnt_type` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`msg_content` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`side_b_mac` | `event.idm.read_only_udm.target.mac` | Mapped from changelog  
`policy_name` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`evnt_extra_info_direction` | `event.idm.read_only_udm.network.direction` | Mapped from changelog  
`content` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`reference_url` | `event.idm.read_only_udm.security_result.url_back_to_product` | Mapped from changelog  
`classtype` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`metadata_description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`device_name` | `event.idm.read_only_udm.principal.mac` | Mapped from changelog  
`alert_type_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`firmware_device_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`device_name` | `event.idm.read_only_udm.principal.asset.mac` | Mapped from changelog  
`device_retired` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`device_note` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`device_app_version` | `event.idm.read_only_udm.principal.asset.software.version` | Mapped from changelog  
`device_vulnerability_relevance` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`device_vulnerability_overall_cvss_v3_score` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`device_vulnerability_manufacturer_remediation_info_source` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`vulnerability_type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`vulnerability_affected_products` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`vulnerability_is_known_exploited` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`vulnerability_known_exploits` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`vulnerability_note` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`device_managed_device` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`device_vulnerability_relevance_source` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`device_vulnerability_manufacturer_remediation_info` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vulnerability_name` | `event.idm.read_only_udm.extensions.vulns.vulnerabilities.name` | Mapped from changelog  
`device_risk_score` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`device_name` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`device_name` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`alert_info_signature_confidence` | `event.idm.read_only_udm.security_result.confidence_score` | Mapped from changelog  
`evnt_extra_info_ids_signature_info_signature_confidence` | `event.idm.read_only_udm.security_result.confidence_score` | Mapped from changelog  
`evnt_extra_info.ids_signature_info.signature_active_rev` | `event.idm.read_only_udm.security_result.rule_version` | Mapped from changelog  
`alert_info_signature_active_rev` | `event.idm.read_only_udm.security_result.rule_version` | Mapped from changelog  
`evnt_extra_info.ids_signature_info.signature_severity_description` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`alert_info.signature_severity_description` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`evnt_extra_info.geo_location` | `event.idm.read_only_udm.principal.location.city` | Mapped from changelog  
`evnt_extra_info.ip_protocol` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`affected_device.management_status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`affected_device.note` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`evnt_extra_info.domain` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`evnt_extra_info.src_domain` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`evnt_extra_info.src_geo_location` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`evnt_extra_info.ids_signature_info.signature_powered_by` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`evnt_extra_info.other_device` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.note` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`affected_device.labels` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert_info.signature_severity_description` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`evnt_extra_info.ids_signature_info.signature_first_released` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`evnt_extra_info.ids_signature_info.signature_last_updated` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`evnt_extra_info.ids_signature_info.signature_last_updated_by_system` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`rule_name` | `event.idm.read_only_udm.alert_info.signature_name` | Mapped from changelog  
`risk_severity` | `event.idm.read_only_udm.alert_info.signature_severity` | Mapped from changelog  
`affected_device.retired` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`management_ip` | `event.idm.read_only_udm.principal.asset.ip` and `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/claroty-xdome-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
