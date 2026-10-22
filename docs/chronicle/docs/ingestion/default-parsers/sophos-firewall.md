---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-firewall/
title: Collect Sophos Firewall (SFOS) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:18.305221+00:00
---

# Collect Sophos Firewall (SFOS) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Sophos Firewall (SFOS) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Sophos Firewall logs to Google Security Operations using Bindplane. Sophos Firewall (SFOS) is a next-generation firewall that provides network security, web filtering, application control, IPS, VPN, and advanced threat protection. SFOS runs on Sophos XGS Series hardware appliances, virtual and cloud deployments, and generates detailed logs for firewall rules, web filtering, IPS events, authentication, VPN connections, and system activity.

**Note:** The Sophos XG Series hardware has reached end-of-life as of March 31, 2025. This guide applies to the current Sophos XGS Series hardware and SFOS software deployments.

For more information, see [Collect Sophos Firewall logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-firewall).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Sophos Firewall web admin console with administrator role.
  * Sophos Firewall running SFOS v18 or later.



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
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         




### Additional installation resources

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it is in the `/opt/observiq-otel-collector/config.yaml` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/sophos_firewall:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             customer_id: '<CUSTOMER_ID>'
             endpoint: chronicle.googleapis.com
             log_type: SOPHOS_FIREWALL
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/sophos_fw_to_chronicle:
               receivers:
                 - udplog
               exporters:
                 - chronicle/sophos_firewall
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace `<CUSTOMER_ID>` with the actual customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the path where the service account key file (Option 1) was saved.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/sophos_firewall:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: SOPHOS_FIREWALL
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in Linux, run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in Windows, you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure syslog forwarding on Sophos Firewall

### Add syslog server

  1. Sign in to the **Sophos Firewall** web admin console.
  2. Go to **System services > Log settings**.
  3. Scroll down to the **Syslog servers** section.
  4. Click **Add** to add a new syslog server.

  5. Provide the following configuration details:

     * **Name** : Enter a descriptive name (for example, `Bindplane-SecOps`).
     * **IP address/Domain** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514` (or your configured port).
     * **Facility** : Select **DAEMON**.
     * **Severity level** : Select **Information** (recommended for comprehensive logging).
     * **Format** : Select **Device Standard Format**.
  6. Click **Save**.




### Select log types to forward

  1. In the **Syslog servers** section, click on the syslog server entry `Bindplane-SecOps`.
  2. In the **Log type** section, enable the log categories to forward:

     * **Firewall** : Firewall rule hits, dropped traffic, and allowed connections.
     * **IPS** : Intrusion Prevention System alerts and events.
     * **Anti-Virus** : Malware detection events.
     * **Anti-Spam** : Spam detection and filtering events.
     * **Content Filtering** : Web filtering and URL categorization events.
     * **Events** : System events, authentication, and administrative activity.
     * **Web Server Protection** : WAF events.
     * **Advanced Threat Protection** : Sandstorm and ATP detection events.
     * **Wireless** : Wireless access point events (if applicable).
     * **Heartbeat** : Sophos Security Heartbeat status changes (if Synchronized Security is enabled).
     * **System Health** : Hardware and software health events.
     * **Authentication** : User and administrator authentication events.
     * **Admin** : Administrative console activity.
  3. Click **Apply**.




### Verify syslog forwarding

  1. Go to **Log viewer** in the Sophos Firewall web admin console.
  2. Verify that log entries are being generated.
  3. Check the Bindplane agent logs to confirm that syslog messages are being received:
         
         sudo journalctl -u observiq-otel-collector -f
         




For more information, see [Sophos Firewall syslog documentation](https://docs.sophos.com/nsg/sophos-firewall/latest/Help/en-us/webhelp/onlinehelp/AdministratorHelp/SystemServices/LogSettings/index.html).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`device_id` | `intermediary.asset.asset_id` | Directly mapped  
`device_serial_id` | `intermediary.asset.asset_id` | Directly mapped  
`device_model` | `intermediary.hostname` | Directly mapped  
`device_name` | `intermediary.hostname` | Directly mapped  
`log_msg` | `metadata.description` | Directly mapped  
`date_time` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss Z`  
`timestamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`log_component` | `metadata.product_event_type` | Directly mapped  
`log_id` | `metadata.product_log_id` | Directly mapped  
`client_physical_address` | `network.dhcp.chaddr` | Directly mapped  
`ipaddress` | `network.dhcp.ciaddr` | Directly mapped  
`client_host_name` | `network.dhcp.client_hostname` | Directly mapped  
`user_agent` | `network.http.parsed_user_agent` | Renamed/mapped  
`referer` | `network.http.referral_url` | Directly mapped  
`http_status` | `network.http.response_code` | Renamed/mapped  
`status_code` | `network.http.response_code` | Renamed/mapped  
`user_agent` | `network.http.user_agent` | Directly mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`bytes_received` | `network.received_bytes` | Renamed/mapped  
`recv_bytes` | `network.received_bytes` | Renamed/mapped  
`packets_received` | `network.received_packets` | Renamed/mapped  
`recv_pkts` | `network.received_packets` | Renamed/mapped  
`bytes_sent` | `network.sent_bytes` | Renamed/mapped  
`sent_bytes` | `network.sent_bytes` | Renamed/mapped  
`packets_sent` | `network.sent_packets` | Renamed/mapped  
`sent_pkts` | `network.sent_packets` | Renamed/mapped  
`duration` | `network.session_duration.seconds` | Renamed/mapped  
`domain` | `principal.administrative_domain` | Renamed/mapped  
`app_name` | `principal.application` | Directly mapped  
`application` | `principal.application` | Directly mapped  
`ipaddress` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`src_country` | `principal.location.country_or_region` | Directly mapped  
`src_country_code` | `principal.location.country_or_region` | Directly mapped  
`src_mac` | `principal.mac` | Merged  
`src_trans_ip` | `principal.nat_ip` | Merged  
`tran_src_ip` | `principal.nat_ip` | Merged  
`src_trans_port` | `principal.nat_port` | Renamed/mapped  
`tran_src_port` | `principal.nat_port` | Renamed/mapped  
`src_port` | `principal.port` | Renamed/mapped  
`user_name` | `principal.user.email_addresses` | Mapped: `.*?@.*` → `user_name`  
`user_name` | `principal.user.userid` | Directly mapped  
`action` | `security_result.action` | Merged  
`status` | `security_result.action_details` | Directly mapped  
`_about0` | `security_result.detection_fields` | Merged  
`_about2` | `security_result.detection_fields` | Merged  
`activityname_label` | `security_result.detection_fields` | Merged  
`appCategory_label` | `security_result.detection_fields` | Merged  
`appTech_label` | `security_result.detection_fields` | Merged  
`app_filter_policy_id_label` | `security_result.detection_fields` | Merged  
`app_is_cloud_label` | `security_result.detection_fields` | Merged  
`app_resolved_by_label` | `security_result.detection_fields` | Merged  
`category_type_label` | `security_result.detection_fields` | Merged  
`con_event_label` | `security_result.detection_fields` | Merged  
`con_id_label` | `security_result.detection_fields` | Merged  
`connevent_label` | `security_result.detection_fields` | Merged  
`connid_label` | `security_result.detection_fields` | Merged  
`dst_zone_type_label` | `security_result.detection_fields` | Merged  
`dstzonetype_label` | `security_result.detection_fields` | Merged  
`ether_type_label` | `security_result.detection_fields` | Merged  
`exceptions_label` | `security_result.detection_fields` | Merged  
`gw_id_request_label` | `security_result.detection_fields` | Merged  
`gw_name_request_label` | `security_result.detection_fields` | Merged  
`hb_health_label` | `security_result.detection_fields` | Merged  
`hb_status_label` | `security_result.detection_fields` | Merged  
`http_category_label` | `security_result.detection_fields` | Merged  
`http_category_type_label` | `security_result.detection_fields` | Merged  
`in_display_interface_label` | `security_result.detection_fields` | Merged  
`in_interface_label` | `security_result.detection_fields` | Merged  
`log_component_label` | `security_result.detection_fields` | Merged  
`log_occurrence_label` | `security_result.detection_fields` | Merged  
`log_subtype_label` | `security_result.detection_fields` | Merged  
`log_type_label` | `security_result.detection_fields` | Merged  
`log_version_label` | `security_result.detection_fields` | Merged  
`nat_rule_id_label` | `security_result.detection_fields` | Merged  
`nat_rule_name_label` | `security_result.detection_fields` | Merged  
`out_display_interface_label` | `security_result.detection_fields` | Merged  
`out_interface_label` | `security_result.detection_fields` | Merged  
`qualifier_label` | `security_result.detection_fields` | Merged  
`reason_label` | `security_result.detection_fields` | Merged  
`risk_label` | `security_result.detection_fields` | Merged  
`src_zone_type_label` | `security_result.detection_fields` | Merged  
`srczonetype_label` | `security_result.detection_fields` | Merged  
`used_quota_label` | `security_result.detection_fields` | Merged  
`web_policy_id_label` | `security_result.detection_fields` | Merged  
`fw_rule_id` | `security_result.rule_id` | Directly mapped  
`fw_rule_name` | `security_result.rule_name` | Directly mapped  
`fw_rule_section` | `security_result.rule_set` | Directly mapped  
`fw_rule_type` | `security_result.rule_type` | Directly mapped  
`priority` | `security_result.severity` | Mapped: `"INFORMATION", "NOTIFICATION", "NOTICE"` → `INFORMATIONAL`, `"ERROR","WARNING"` → `...  
`reason` | `security_result.summary` | Directly mapped  
`domain` | `target.hostname` | Directly mapped  
`dst_ip` | `target.ip` | Merged  
`dst_country` | `target.location.country_or_region` | Directly mapped  
`dst_country_code` | `target.location.country_or_region` | Directly mapped  
`dst_mac` | `target.mac` | Merged  
`dst_trans_ip` | `target.nat_ip` | Merged  
`tran_dst_ip` | `target.nat_ip` | Merged  
`dst_trans_port` | `target.nat_port` | Renamed/mapped  
`tran_dst_port` | `target.nat_port` | Renamed/mapped  
`dst_port` | `target.port` | Renamed/mapped  
`url` | `target.url` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `VPN`  
N/A | `metadata.event_type` | Constant: `NETWORK_HTTP`  
N/A | `metadata.product_name` | Constant: `SOPHOS Firewall`  
N/A | `metadata.vendor_name` | Constant: `SOPHOS`  
N/A | `network.application_protocol` | Constant: `DHCP`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
`date_time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`referer` | `network.http.referer_url` | Mapped from changelog  
`device_serial_id` | `principal.asset.asset_id` | Mapped from changelog  
`application_category, application_risk and application_technology` | `security_result.detection_fields` | Mapped from changelog  
`user_name` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`device_id` | `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-firewall-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
