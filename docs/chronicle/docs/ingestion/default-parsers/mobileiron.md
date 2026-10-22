---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mobileiron/
title: Collect Ivanti Neurons for MDM (formerly MobileIron) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:01.313958+00:00
---

# Collect Ivanti Neurons for MDM (formerly MobileIron) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mobileiron/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Ivanti Neurons for MDM (formerly MobileIron) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Ivanti Neurons for MDM (formerly known as MobileIron) logs to Google Security Operations using Bindplane.

Ivanti Neurons for MDM is a unified endpoint management (UEM) platform that enables organizations to secure and manage mobile devices, applications, and content across iOS, Android, macOS, and Windows environments. It provides device enrollment, policy enforcement, compliance monitoring, app distribution, and threat detection capabilities for enterprise mobility management.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Ivanti Neurons for MDM admin console.



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

     * Locate the `config.yaml` file. Typically, it's in the `/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           tcplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             customer_id: '<customer_id>'
             endpoint: chronicle.googleapis.com
             log_type: MOBILEIRON
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
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in the **Get Google SecOps credentials for the Bindplane agent** section.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: MOBILEIRON
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
         




## Configure Ivanti Neurons for MDM syslog forwarding

  1. Sign in to the **Ivanti Neurons for MDM** admin console.
  2. Go to **Settings > Syslog**.
  3. Click **Add** to create a new syslog configuration.
  4. Provide the following configuration details: 
     * **Host** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Protocol** : Select **TCP**.
  5. In the **Event Types** section, select the event categories to forward: 
     * Device events
     * Compliance events
     * Security events
     * Admin events
  6. Click **Save** to apply the syslog configuration.

**Note:** Verify that the Ivanti Neurons for MDM appliance can reach the Bindplane agent host on TCP port 514. Check the Bindplane agent logs to confirm that syslog messages are being received.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`COMMAND_label` | `additional.fields` | Merged  
`NI_label` | `additional.fields` | Merged  
`PR_label` | `additional.fields` | Merged  
`RES_label` | `additional.fields` | Merged  
`SHR_label` | `additional.fields` | Merged  
`S_label` | `additional.fields` | Merged  
`SystemType_label` | `additional.fields` | Merged  
`VIRT_label` | `additional.fields` | Merged  
`apache_error_code_label` | `additional.fields` | Merged  
`attempts_label` | `additional.fields` | Merged  
`b_label` | `additional.fields` | Merged  
`bi_label` | `additional.fields` | Merged  
`bo_label` | `additional.fields` | Merged  
`buff_label` | `additional.fields` | Merged  
`cache_label` | `additional.fields` | Merged  
`cpuTIME_label` | `additional.fields` | Merged  
`cpu_percent_label` | `additional.fields` | Merged  
`cs_label` | `additional.fields` | Merged  
`duration_ms_label` | `additional.fields` | Merged  
`error_code_label` | `additional.fields` | Merged  
`free_label` | `additional.fields` | Merged  
`in_label` | `additional.fields` | Merged  
`ip_in_bracket_label` | `additional.fields` | Merged  
`log_year_label` | `additional.fields` | Merged  
`mem_percent_label` | `additional.fields` | Merged  
`module_label` | `additional.fields` | Merged  
`ns_1_label` | `additional.fields` | Merged  
`pctCPU_label` | `additional.fields` | Merged  
`pctMEM_label` | `additional.fields` | Merged  
`product_label` | `additional.fields` | Merged  
`r_label` | `additional.fields` | Merged  
`rss_label` | `additional.fields` | Merged  
`safepoint_ns_1_label` | `additional.fields` | Merged  
`safepoint_ns_2_label` | `additional.fields` | Merged  
`si_label` | `additional.fields` | Merged  
`so_label` | `additional.fields` | Merged  
`st_label` | `additional.fields` | Merged  
`start_label` | `additional.fields` | Merged  
`stat_label` | `additional.fields` | Merged  
`swpd_label` | `additional.fields` | Merged  
`sy_label` | `additional.fields` | Merged  
`t1_label` | `additional.fields` | Merged  
`tag_label` | `additional.fields` | Merged  
`token_id_label` | `additional.fields` | Merged  
`us_label` | `additional.fields` | Merged  
`vsz_label` | `additional.fields` | Merged  
`wa_label` | `additional.fields` | Merged  
`has_target_user` | `extensions.auth.type` | Mapped: `true` → `MACHINE`  
`host` | `intermediary.asset.hostname` | Directly mapped  
`host` | `intermediary.hostname` | Directly mapped  
`ip_1` | `intermediary.ip` | Merged  
`desc` | `metadata.description` | Directly mapped  
`kv_msg` | `metadata.description` | Directly mapped  
`msg` | `metadata.description` | Directly mapped  
`date_time` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd--HH-mm-ss`  
`policyViolatedAt` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`time` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSS+0000`  
`time_1` | `metadata.event_timestamp` | Parsed as `UNIX`  
`timestamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSSSS+00:00`  
`ts` | `metadata.event_timestamp` | Parsed as `MMM DD HH:mm:ss`  
`action` | `metadata.event_type` | Mapped: `Started Session` → `USER_UNCATEGORIZED`  
`has_resource` | `metadata.event_type` | Mapped: `true` → `USER_RESOURCE_ACCESS`  
`has_target_user` | `metadata.event_type` | Mapped: `true` → `USER_LOGOUT`  
`principal_mid_present` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`msgid` | `metadata.product_log_id` | Directly mapped  
`version` | `metadata.product_version` | Directly mapped  
`protocol` | `network.application_protocol` | Directly mapped  
`protocol_version` | `network.application_protocol_version` | Directly mapped  
`http_method` | `network.http.method` | Directly mapped  
`method` | `network.http.method` | Directly mapped  
`referrer` | `network.http.referral_url` | Directly mapped  
`url` | `network.http.referral_url` | Directly mapped  
`http_status` | `network.http.response_code` | Renamed/mapped  
`user_agent` | `network.http.user_agent` | Directly mapped  
`response_size` | `network.received_bytes` | Renamed/mapped  
`sessionId` | `network.session_id` | Directly mapped  
`cipher` | `network.tls.cipher` | Directly mapped  
`tls_version` | `network.tls.version` | Directly mapped  
`app_name` | `principal.application` | Directly mapped  
`hardware` | `principal.asset.hardware` | Merged  
`client_ip` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`platformType` | `principal.asset.platform_software.platform` | Mapped: `(?i)Windows` → `WINDOWS`, `(?i)(MAC/OS X/IOS)` → `MAC`, `(?i)Linux` → `LINUX`  
`platformType` | `principal.asset.platform_software.platform_version` | Directly mapped  
`platformVersion` | `principal.asset.platform_software.platform_version` | Directly mapped  
`id` | `principal.asset.product_object_id` | Directly mapped  
`client_ip` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`client_port` | `principal.port` | Directly mapped  
`PID` | `principal.process.pid` | Directly mapped  
`procid` | `principal.process.pid` | Directly mapped  
`idle_label` | `principal.resource.attribute.labels` | Merged  
`iowait_label` | `principal.resource.attribute.labels` | Merged  
`nice_label` | `principal.resource.attribute.labels` | Merged  
`steal_label` | `principal.resource.attribute.labels` | Merged  
`system_label` | `principal.resource.attribute.labels` | Merged  
`user_label` | `principal.resource.attribute.labels` | Merged  
`emailAddress` | `principal.user.email_addresses` | Merged  
`firstName` | `principal.user.first_name` | Directly mapped  
`lastName` | `principal.user.last_name` | Directly mapped  
`displayName` | `principal.user.user_display_name` | Directly mapped  
`USER` | `principal.user.userid` | Directly mapped  
`username` | `principal.user.userid` | Directly mapped  
`policy_Violated_At` | `security_result.about.labels` | Merged  
`sr_action` | `security_result.action` | Merged  
`category` | `security_result.category` | Merged  
`complianceViolationTypeToReason.BLACKLIST_APPS` | `security_result.description` | Directly mapped  
`complianceViolationTypeToReason.PC` | `security_result.description` | Directly mapped  
`complianceViolationTypeToReason.SA` | `security_result.description` | Directly mapped  
`description` | `security_result.description` | Directly mapped  
`http_request_label` | `security_result.detection_fields` | Merged  
`run_user_label` | `security_result.detection_fields` | Merged  
`safepoint_type_label` | `security_result.detection_fields` | Merged  
`systemd_user_label` | `security_result.detection_fields` | Merged  
`type_label` | `security_result.detection_fields` | Merged  
`policyViolatedID` | `security_result.rule_id` | Directly mapped  
`loglevel` | `security_result.severity` | Mapped: `(?i)INFO` → `INFORMATIONAL`, `(?i)Error` → `ERROR`, `(?i)Warning` → `MEDIUM`  
`loglevel` | `security_result.severity_details` | Directly mapped  
`summary` | `security_result.summary` | Directly mapped  
`target_ip` | `target.asset.ip` | Merged  
`target_host` | `target.hostname` | Directly mapped  
`target_ip` | `target.ip` | Merged  
`target_port` | `target.port` | Directly mapped  
`command` | `target.process.command_line` | Directly mapped  
`pid` | `target.process.pid` | Directly mapped  
`program_name` | `target.resource.name` | Directly mapped  
`url_1` | `target.url` | Directly mapped  
`session_user` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `MACHINE`  
N/A | `metadata.event_type` | Constant: `USER_LOGOUT`  
N/A | `metadata.product_name` | Constant: `Endpoint Manager Mobile`  
N/A | `metadata.vendor_name` | Constant: `Ivanti`  
N/A | `principal.asset.platform_software.platform` | Constant: `WINDOWS`  
N/A | `principal.asset.type` | Constant: `MOBILE`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
`common_client_id` | `event.idm.read_only_udm.principal.process.product_specific_process_id` | Mapped from changelog  
`common_client_name` | `event.idm.read_only_udm.principal.asset.software.name` | Mapped from changelog  
`common_client_version` | `event.idm.read_only_udm.principal.asset.software.version` | Mapped from changelog  
`ios_ip_address` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`common_ip_address` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`ios_vpn_ip_address` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`common_creation_date` | `event.idm.read_only_udm.principal.asset.attribute.creation_time` | Mapped from changelog  
`common_current_phone_number` | `event.idm.read_only_udm.principal.user.phone_numbers` | Mapped from changelog  
`common_home_phone_number` | `event.idm.read_only_udm.principal.user.phone_numbers` | Mapped from changelog  
`common_id` | `event.idm.read_only_udm.principal.resource.product_object_id` | Mapped from changelog  
`common_manufacturer` | `event.idm.read_only_udm.principal.asset.hardware.manufacturer` | Mapped from changelog  
`common_SerialNumber` | `event.idm.read_only_udm.principal.asset.hardware.serial_number` | Mapped from changelog  
`common_model` | `event.idm.read_only_udm.principal.asset.hardware.model` | Mapped from changelog  
`common_os_version` | `event.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`user_user_id` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`common_uuid` | `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
`common_wifi_mac_address` | `event.idm.read_only_udm.principal.mac` | Mapped from changelog  
`ios_BluetoothMAC` | `event.idm.read_only_udm.principal.mac` | Mapped from changelog  
`ios_BuildVersion` | `event.idm.read_only_udm.principal.platform_patch_level` | Mapped from changelog  
`ios_iPhoneUDID` | `event.idm.read_only_udm.principal.asset.product_object_id` | Mapped from changelog  
`user_display_name` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`user_email_address` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`user_ldap_user_attributes_mail` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`user_first_name` | `event.idm.read_only_udm.principal.user.first_name` | Mapped from changelog  
`user_last_name` | `event.idm.read_only_udm.principal.user.last_name` | Mapped from changelog  
`user_last_admin_portal_login_time` | `event.idm.read_only_udm.principal.user.last_login_time` | Mapped from changelog  
`user_uuid` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`user_ldap_user_object_sid` | `event.idm.read_only_udm.principal.user.windows_sid` | Mapped from changelog  
`user_ldap_user_attributes_memberOf` | `event.idm.read_only_udm.principal.user.group_identifiers` | Mapped from changelog  
`user_ldap_groups` | `event.idm.read_only_udm.principal.user.group_identifiers` | Mapped from changelog  
`common_client_build_date` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`common_compliant` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`common_data_protection_enabled` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`common_device_is_compromised` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ios_DeviceName` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`ios_iPhoneVERSION` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`ios_iPhonePRODUCT` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`ios_ProductName` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`user_sam_account_name` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`user_ldap_attr_dn` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`user_ldap_dn` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`user_ldap_principal` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`user_ldap_upn` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`user_ldap_user_attributes_sAMAccountName` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`user_ldap_user_attributes_displayName` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`user_ldap_user_attributes_givenName` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`user_ldap_user_attributes_sn` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`user_ldap_user_attributes_userPrincipalName` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`common_apns_capable` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_background_status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_battery_level` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_blocked` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_cellular_technology` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_device_admin_enabled` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_device_encrypted` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_lang_country_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_language` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_language_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_mutual_auth_enabled` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_locale` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_intune_compliance_azure_device_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_intune_compliance_azure_client_status_code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_intune_compliance_azure_tenant_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_mdm_managed` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_miclient_last_connected_at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_mdm_tos_accepted` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_model_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_modified_at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_processor_architecture` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_quarantined_action` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_quarantined` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_registration_date` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_retired` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_roaming` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_sd_card_encrypted` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_security_state` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_storage_capacity` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_storage_free` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_catalog_ids` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_device_space_ids` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_device_space_path` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_device_space_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_mtd_status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_mtd_anti_phishing_status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_mtd_anti_phishing_vpn_status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_ccm_migration_status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_auth_only` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_EnhancedLoggingEnabled` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_apnsToken` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_osUpdateStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_data_protection` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_DataRoamingEnabled` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_PersonalHotspotEnabled` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_forceEncryptedBackup` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_HardwareEncryptionCaps` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_iOSBackgroundStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_IsDeviceLocatorServiceEnabled` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_IsDoNotDisturbInEffect` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_iTunesStoreAccountIsActive` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_IsDEPEnrolledDevice` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_IsDEPDevice` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_IsMDMServiceEnrolledDevice` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_IsCloudBackupEnabled` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_IsNetworkTethered` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_IsActivationLockEnabled` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_ActivationLockBypassCode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_it_policy_result` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_PasscodeIsCompliant` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_PasscodeIsCompliantWithProfiles` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_PasscodePresent` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_security_reason_code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_VoiceRoamingEnabled` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_wakeup_status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_IsMDMLostModeEnabled` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_IsMultiUser` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_sim_countOfSims` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_Supervised` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_TimeZone` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_apple_user_enrolled_device` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_TrustedDevice` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_ddm_enabled` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ios_ddm_capabilities_available` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`common_owner` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_ldap_user_account_control_account_disabled` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_ldap_user_account_control_password_expired` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_ldap_user_account_control_locked_out` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_ldap_user_attributes_distinguishedName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_ldap_user_attributes_objectSid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_ldap_user_attributes_cn` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_ldap_user_attributes_userAccountControl` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`actorId` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`actorName` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`actorUid` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`actorRoles` | `event.idm.read_only_udm.principal.user.attribute.roles` | Mapped from changelog  
`resultStatus` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`resultStatus` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`actionType` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`entityName` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`entityId` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`entityType` | `event.idm.read_only_udm.target.resource.resource_subtype` | Mapped from changelog  
`entityGroup` | `event.idm.read_only_udm.target.user.group_identifiers` | Mapped from changelog  
`entityAuditId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`details` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`entityDeleted` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`expiresAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`publishedAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`publisherId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tenantUuid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`log_source` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`time` | `event.idm.read_only_udm.security_result.first_discovered_time` | Mapped from changelog  
`host` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`host` | `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`product` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ip_in_bracket` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mobileiron-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
