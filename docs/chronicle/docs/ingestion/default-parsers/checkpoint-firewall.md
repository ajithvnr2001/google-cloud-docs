---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-firewall/
title: Collect Check Point firewall logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:07.097179+00:00
---

# Collect Check Point firewall logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Check Point firewall logs

**Parser Version:** 34.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Check Point firewall logs to Google Security Operations using the Bindplane agent.

Check Point firewalls generate logs for network connections, security events, VPN activity, threat prevention, and administrative operations. The parser extracts key-value and CEF fields and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Check Point firewall
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Check Point firewall UI



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
          chronicle/checkpoint_firewall:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: CHECKPOINT_FIREWALL
            raw_log_field: body
        
        service:
          pipelines:
            logs/checkpoint_firewall_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/checkpoint_firewall
        




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
          chronicle/checkpoint_firewall:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CHECKPOINT_FIREWALL
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
           
           ```bash
           sudo systemctl status observiq-otel-collector
           ```
           

    2. Check logs for errors:
           
           ```bash
           sudo journalctl -u observiq-otel-collector -f
           ```
           

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
             




## Configure syslog export in a Check Point firewall

  1. Sign in to the Check Point firewall UI using a privileged account.
  2. Go to **Logs & Monitoring > Log Servers**.
  3. Navigate to **Syslog Servers**.
  4. Click **Configure** , and set the following values: 
     * **Protocol** : Select **UDP** to send security logs and/or system logs.
     * **Name** : Provide a unique name (for example, `Bindplane_Server`).
     * **IP Address** : Provide your syslog server IP address (Bindplane IP).
     * **Port** : Provide your syslog server port (Bindplane port).
  5. Select **Enable log server**.
  6. Select logs to forward: **Both system and security logs**.
  7. Click **Apply**.



## UDM mapping table

| `proto` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog | | `helo` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `inner_syslog_priority` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `principal_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog | | `syslog_priority` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `creation_time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog | | `last_hit_time` | `event.idm.read_only_udm.security_result.last_discovered_time` | Mapped from changelog | | `update_count` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `devTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `queue_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `process` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `from_host` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog | | `from_host` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog | | `from_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog | | `from_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog | | `email_from` | `event.idm.read_only_udm.network.email.from` | Mapped from changelog | | `email_to` | `event.idm.read_only_udm.network.email.to` | Mapped from changelog | | `protocol` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog | | `program` | `event.idm.read_only_udm.target.application` | Mapped from changelog | | `syslog_host` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog | | `icmp_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `icmp_code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `precise_error` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog | | `action_reason` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `alert` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `message_type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `UP_match_table` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `UP_match_table_2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `ROW_START` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `ROW_START_2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `match_id_2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `ROW_END` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `ROW_END_2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `layer_uuid_2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `layer_name_2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `rule_uid_2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `rule_name_2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `dst_dynobj_name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog | | `dst_object_type` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog | | `version` | `event.idm.read_only_udm.intermediary.platform_version` | Mapped from changelog | | `referrer` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog | | `mac_address` | `event.idm.read_only_udm.principal.mac` | Mapped from changelog | | `mgmt_value` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `date_value` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `origin` | `event.idm.read_only_udm.intermediary1.ip` | Mapped from changelog | | `logid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `db_tag` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `web_client_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `acks_total", "attachments_num", "arrival_time","attack_status", "attack_traffic_bps", "attack_traffic_pps", "audit_status", "auth_method", "bandwidth", "best_practice_id", "blade_name", "cb_rate", "cb_recommendation", "cb_relevantobjectname", "cb_relevantobjectstatus", "file_count", "cb_scan_id", "from", "to", "cb_status", "cb_bp_blade", "controller", "delivery_time", "device_identification", "direction", "discard_traffic_bps", "discard_traffic_pps", "dlp_data_type_name", "dlp_relevant_data_types", "dlp_rule_name", "dlp_transport", "dns_query_type", "failure_reason", "file_size", "file_type" and "file_direction` | `additional.fields` | Mapped from changelog | | `destination_dns_hostname` | `target.hostname` | Mapped from changelog | | `email_content` | `security_result.description` | Mapped from changelog | | `email_subject` | `network.email.subject` | Mapped from changelog | | `event_name` | `metadata.description` | Mapped from changelog | | `web_client_type` | `network.http.user_agent` | Mapped from changelog | | `file_size` | `target.file_size` | Mapped from changelog | | `from` | `network.email.from` | Mapped from changelog | | `to` | `network.email.to` | Mapped from changelog | | `verdict` | `security_result.verdict_response` | Mapped from changelog | | `file_name` | `target.file.names` | Mapped from changelog | | `file_md5` | `target.file.md5` | Mapped from changelog | | `file_sha1` | `target.file.sha1` | Mapped from changelog | | `file_sha256` | `target.file.sha256` | Mapped from changelog | | `description` | `security_result.description` | Mapped from changelog | | `Name` | `security_result.detection_fields` | Mapped from changelog | | `Level` | `security_result.confidence_details` | Mapped from changelog | | `Impact` | `additional.fields` | Mapped from changelog | | `security_result.action` | `BLOCK` | Mapped from changelog | | `machine` | `target.hostname` | Mapped from changelog | | `user` | `principal.user.user_display_name` | Mapped from changelog | | `src` | `principal.hostname` | Mapped from changelog | | `security_result.action` | `ALLOW` | Mapped from changelog | | `operation_number` | `security_result.detection_fields` | Mapped from changelog | | `client_ip` | `principal.ip` | Mapped from changelog | | `log_sys_message` | `metadata.description` | Mapped from changelog | | `layer_name` | `security_result.detection_fields` | Mapped from changelog | | `feature_name" and "securexl_message` | `additional.fields` | Mapped from changelog | | `emailSubject` | `network.email.subject` | Mapped from changelog | | `cat` | `security_result.detection_fields` | Mapped from changelog | | `url` | `principal.url` | Mapped from changelog | | `srcPostNAT` | `principal.nat_ip` | Mapped from changelog | | `dstPostNAT` | `target.nat_ip` | Mapped from changelog | | `srcPostNATPort` | `principal.nat_port` | Mapped from changelog | | `dstPostNATPort` | `target.nat_port` | Mapped from changelog | | `dns_query` | `network.dns.questions` | Mapped from changelog | | `layer_uuid_rule_uuid` | `security_result.rule_id` | Mapped from changelog | | `domain` | `principal.administrative_domain` | Mapped from changelog | | `fservice", "appi_name", "app_risk", and "policy_name` | `security_result.detection_fields` | Mapped from changelog | | `packets", "__id", "dedup_time", "browse_time", "bytes", "product_family", "hll_key", and "calc_service` | `additional.fields` | Mapped from changelog | | `id` | `metadata.product_log_id` | Mapped from changelog | | `orig_log_server` | `principal.resource.product_object_id` | Mapped from changelog | | `environment_id` | `target.resource.product_object_id` | Mapped from changelog | | `client_outbound_packets" and "client_inbound_packets` | `principal.resource.attribute.labels` | Mapped from changelog | | `server_outbound_bytes" and "server_inbound_bytes` | `target.resource.attribute.labels` | Mapped from changelog | | `orig` | `principal.hostname` | Mapped from changelog | | `orig_log_server_ip` | `principal.ip` | Mapped from changelog | | `proto` | `network.ip_protocol` | Mapped from changelog | | `inter_host` | `intermediary.hostname` | Mapped from changelog | | `origin` | `target.ip` | Mapped from changelog | | `smartdefense_profile", "malware_rule_id", and "malware_rule_name` | `security_result.detection_fields` | Mapped from changelog | | `sequencenum", "description_url", "industry_reference", "mitre_execution", "packet_capture_name", "packet_capture_unique_id", "packet_capture_time", and "performance_impact` | `additional.fields` | Mapped from changelog | | `version` | `metadata.product_version` | Mapped from changelog | | `http_host` | `target.resource.attribute.labels` | Mapped from changelog | | `log_id` | `metadata.product_log_id` | Mapped from changelog | | `user_agent` | `network.http.user_agent` | Mapped from changelog | | `hostname", "dvc", and "principal_hostname` | `target.hostname` | Mapped from changelog | | `protection_id", "malware_action", "malware_family,protection_name", "protection_type` | `security_result.detection_fields` | Mapped from changelog | | `confidence_level` | `security_result.confidence` | Mapped from changelog | | `method` | `network.http.method` | Mapped from changelog | | `duration` | `network.session_duration.seconds` | Mapped from changelog | | `additional_info` | `security_result.description` | Mapped from changelog | | `operation` | `security_result.summary` | Mapped from changelog | | `subject` | `metadata.description` | Mapped from changelog | | `principal_hostname` | `intermediary.hostname` | Mapped from changelog | | `flags` | `security_result.detection_fields` | Mapped from changelog | | `tcp_flags` | `security_result.detection_fields` | Mapped from changelog | | `tcp_packet_out_of_state` | `security_result.detection_fields` | Mapped from changelog | | `sport_svc` | `principal.port` | Mapped from changelog | | `ProductFamily` | `additional.fields` | Mapped from changelog | | `mitre_initial_access` | `security_result.detection_fields` | Mapped from changelog | | `policy_time` | `security_result.detection_fields` | Mapped from changelog | | `profile` | `security_result.detection_fields` | Mapped from changelog | | `reject_id_kid` | `security_result.detection_fields` | Mapped from changelog | | `ser_agent_kid` | `security_result.detection_fields` | Mapped from changelog | | `app_category` | `security_result.category_details` | Mapped from changelog | | `matched_category` | `security_result.detection_fields` | Mapped from changelog | | `app_properties` | `security_result.detection_fields` | Mapped from changelog | | `conn_direction` | `additional.fields` | Mapped from changelog | | `rule_name` | `security_result.rule_name` | Mapped from changelog | | `rule","sub_policy_name","sub_policy_uid","smartdefense_profile","tags","flexString2` | `security_result.detection_fields` | Mapped from changelog | | `dvc` | `intermediary.hostname` | Mapped from changelog | | `hostname` | `intermediary.hostname` | Mapped from changelog | | `origin_sic_name` | `intermediary.asset_id` | Mapped from changelog | | `conn_direction` | `network.ip_protocol` | Mapped from changelog | | `ifname` | `security_result.detection_fields` | Mapped from changelog | | `security_inzone` | `security_result.detection_fields` | Mapped from changelog | | `match_id` | `security_result.detection_fields` | Mapped from changelog | | `parent_rule` | `security_result.detection_fields` | Mapped from changelog | | `security_outzone` | `security_result.detection_fields` | Mapped from changelog | | `sub_policy_name` | `security_result.detection_fields` | Mapped from changelog | | `sub_policy_uid` | `security_result.detection_fields` | Mapped from changelog | | `drop_reason` | `security_result.summary` | Mapped from changelog | | `reason` | `security_result.summary` | Mapped from changelog | | `xlatesport` | `principal.nat_port` | Mapped from changelog | | `xlatedport` | `target.nat_port` | Mapped from changelog | | `ipv6_dst` | `target.ip` | Mapped from changelog | | `ipv6_src` | `principal.ip` | Mapped from changelog | | `portal_message` | `security_result.description` | Mapped from changelog | | `URL` | `security_result.about.url` | Mapped from changelog | | `Activity` | `security_result.summary` | Mapped from changelog | | `Reference` | `security_result.about.resource.attribute.labels` | Mapped from changelog | | `malware_action", "malware_family,protection_name", "protection_type` | `security_result.about.resource.attribute.labels` | Mapped from changelog | | `src_machine_name` | `security_result.detection_fields` | Mapped from changelog | | `message_info` | `metadata.description` | Mapped from changelog |

Log field | UDM mapping  
---|---  
`@timestamp` | `metadata.event_timestamp`  
`__id` | `additional.fields`  
`__nsons` | `additional.fields`  
`__p_dport` | `additional.fields`  
`__pos` | `additional.fields`  
`_action` | `security_result.action_id`  
`access_method` | `metadata.product_event_type`  
`acks_total` | `additional.fields`  
`act` | `security_result.action_details`  
`Action` | `additional.fields`  
`action_details` | `additional.fields`  
`action_reason` | `security_result.detection_fields`  
`Activity` | `security_result.summary`  
`additional_info` | `security_result.description`,  
`security_result.detection_fields`  
`administrator` | `target.user.userid`  
`aggregated_log_count` | `security_result.detection_fields`  
`alert` | `security_result.detection_fields`  
`answer_rdata` | `additional.fields`  
`app` | `principal.application`  
`app_activity` | `security_result.description`  
`app_category` | `security_result.category_details`  
`app_desc` | `additional.fields`  
`app_id` | `additional.fields`  
`app_properties` | `additional.fields`,  
`security_result.detection_fields`  
`app_risk` | `security_result.detection_fields`  
`app_session_id` | `network.session_id`  
`app_sig_id` | `additional.fields`  
`appcategory` | `additional.fields`  
`appi_name` | `security_result.detection_fields`  
`application` | `principal.application`  
`application_version` | `additional.fields`  
`arrival_time` | `additional.fields`  
`attachment_link` | `additional.fields`  
`attachments_num` | `additional.fields`  
`attack` | `security_result.threat_name`  
`attack_info` | `security_result.description`  
`attack_status` | `additional.fields`  
`attack_traffic_bps` | `additional.fields`  
`attackStatus` | `security_result.detection_fields`  
`audit_status` | `additional.fields`  
`auth_method` | `additional.fields`  
`auth_status` | `security_result.summary`  
`authentication_trial` | `additional.fields`  
`authority_rdata` | `principal.resource.attribute.labels`  
`authorization` | `security_result.detection_fields`  
`bandwidth` | `security_result.detection_fields`  
`best_practice_id` | `security_result.detection_fields`  
`blade_name` | `security_result.detection_fields`  
`browse_time` | `additional.fields`  
`browser` | `network.http.user_agent`  
`bytes` | `additional.fields`  
`c_bytes` | `additional.fields`  
`calc_desc` | `security_result.description`  
`calc_service` | `additional.fields`  
`cat` | `security_result.detection_fields`  
`category` | `security_result.category_details`  
`cb_bp_blade` | `additional.fields`  
`cb_rate` | `additional.fields`  
`cb_recommendation` | `additional.fields`  
`cb_relevantobjectname` | `additional.fields`  
`cb_relevantobjectstatus` | `additional.fields`  
`cb_scan_id` | `security_result.detection_fields`  
`cb_status` | `additional.fields`  
`certificate_validity` | `additional.fields`  
`client_inbound_bytes` | `principal.network.received_bytes`  
`client_inbound_interface` | `additional.fields`  
`client_inbound_packets` | `principal.network.received_packets`  
`client_ip` | `principal.ip`,  
`principal.asset.ip`  
`client_name` | `security_result.detection_fields`  
`client_outbound_bytes` | `principal.network.sent_bytes`  
`client_outbound_interface` | `additional.fields`  
`client_outbound_packets` | `principal.network.sent_packets`  
`client_to_gateway_ciphers` | `additional.fields`  
`client_type_os` | `principal.platform`  
`client_version.0` | `intermediary.platform_version`  
`cloud_hourly_quota` | `additional.fields`  
`cloud_hourly_quota_exceeded` | `additional.fields`  
`cloud_hourly_quota_usage_for_quota_id` | `additional.fields`  
`cloud_hourly_quota_usage_for_this_gw` | `additional.fields`  
`cloud_hourly_remaining_quota` | `additional.fields`  
`cloud_last_quota_update_gmt_time` | `additional.fields`  
`cloud_monthly_quota` | `additional.fields`  
`cloud_monthly_quota_exceeded` | `additional.fields`  
`cloud_monthly_quota_period_end` | `additional.fields`  
`cloud_monthly_quota_period_start` | `additional.fields`  
`cloud_monthly_quota_usage_for_quota_id` | `additional.fields`  
`cloud_monthly_quota_usage_for_this_gw` | `additional.fields`  
`cloud_quota_description` | `additional.fields`  
`cloud_quota_identifier` | `additional.fields`  
`cloud_quota_status` | `additional.fields`  
`cloud_remaining_quota` | `additional.fields`  
`cluster_info` | `additional.fields`  
`cn2` | `additional.fields`  
`cn3` | `additional.fields`  
`comment` | `security_result.description`  
`community` | `additional.fields`  
`condition` | `additional.fields`  
`confidence_level` | `security_result.confidence`  
`conn_direction` | `network.direction`,  
`additional.fields`  
`connection_count` | `security_result.detection_fields`  
`connection_luuid` | `additional.fields`  
`connection_uid` | `additional.fields`  
`consent_flag_status` | `additional.fields`  
`consent_flag_value` | `additional.fields`  
`content_disposition` | `target.file.names`  
`content_length` | `target.file.size`  
`content_risk` | `additional.fields`  
`content_type` | `target.file.mime_type`  
`context_num` | `additional.fields`  
`contextnum` | `additional.fields`  
`contract_name` | `security_result.detection_fields`  
`control_log_type` | `additional.fields`  
`controller` | `additional.fields`  
`cookiei` | `additional.fields`  
`cookier` | `additional.fields`  
`cp_component_name` | `additional.fields`  
`cp_component_version` | `additional.fields`  
`creation_time` | `principal.asset.attribute.creation_time`  
`cs2_second` | `intermediary.ip`,  
`intermediary.asset.ip`  
`cu_detected_by` | `additional.fields`  
`cu_detection_time` | `additional.fields`  
`cu_log_count` | `additional.fields`  
`cu_rule_category` | `security_result.rule_name`  
`cu_rule_id` | `security_result.rule_id`  
`current_value` | `additional.fields`  
`d_name` | `security_result.detection_fields`  
`data_type_name` | `security_result.detection_fields`  
`date_value` | `additional.fields`  
`datetime` | `metadata.event_timestamp`  
`db_tag` | `security_result.detection_fields`  
`db_ver` | `additional.fields`  
`DCE_RPC_Interface_UID` | `additional.fields`  
`dce-rpc_interface_uuid` | `additional.fields`  
`dce-rpc_interface_uuid-1` | `additional.fields`  
`dce-rpc_interface_uuid-2` | `additional.fields`  
`dce-rpc_interface_uuid-3` | `additional.fields`  
`dedup_time` | `additional.fields`  
`default_device_message` | `additional.fields`  
`delivery_time` | `additional.fields`  
`desc` | `security_result.summary`  
`description` | `security_result.detection_fields`  
`description_url` | `additional.fields`  
`Destination` | `additional.fields`  
`destination_dns_hostname` | `target.hostname`,  
`target.asset.hostname`  
`destinationAddress` | `target.ip`,  
`target.asset.ip`  
`destinationDnsDomain` | `target.url`  
`destinationPort` | `target.port`  
`destinationTranslatedAddress` | `target.ip`,  
`target.asset.ip`,  
`target.nat_ip`  
`destinationTranslatedPort` | `target.port`,  
`target.nat_port`  
`detected_by` | `security_result.detection_fields`  
`device` | `intermediary.ip`,  
`intermediary.asset.ip`  
`device_identification` | `additional.fields`  
`device_message` | `security_result.description`  
`device_name` | `target.hostname`,  
`target.asset.hostname`  
`device_type` | `target.resource.resource_subtype`  
`deviceCustomNumber2` | `additional.fields`  
`deviceCustomString2` | `security_result.rule_name`  
`deviceDirection` | `network.direction`  
`devTime` | `metadata.event_timestamp`  
`direction` | `additional.fields`  
`discard_traffic_bps` | `additional.fields`  
`discard_traffic_pps` | `additional.fields`  
`dlp_data_type_name` | `additional.fields`  
`dlp_relevant_data_types` | `additional.fields`  
`dlp_rule_name` | `additional.fields`  
`dlp_transport` | `additional.fields`  
`dn` | `additional.fields`  
`dns_domain_name` | `target.hostname`,  
`target.asset.hostname`  
`dns_message_type` | `security_result.detection_fields`  
`dns_query_type` | `additional.fields`  
`dns_query.queries` | `network.dns.questions.name`  
`dns_type` | `additional.fields`  
`domain` | `principal.administrative_domain`  
`domain_name` | `principal.administrative_domain`  
`dpt` | `target.port`  
`drop_reason` | `security_result.summary`  
`dst` | `target.ip`,  
`target.asset.ip`  
`dst_country` | `target.location.country_or_region`  
`dst_domain_name` | `target.hostname`,  
`target.asset.hostname`  
`dst_ip` | `target.ip`,  
`target.asset.ip`  
`dst_machine_name` | `target.user.email_addresses`  
`dst_phone_number` | `target.user.phone_numbers`  
`dst_port` | `target.port`  
`dst_uo_icon` | `additional.fields`  
`dst_uo_name` | `target.location.country_or_region`  
`dst_user_dn` | `target.resource.attribute.labels`  
`dst_user_name` | `target.user.user_display_name`  
`dstBytes` | `additional.fields`  
`dstkeyid` | `additional.fields`  
`dstPostNAT` | `target.nat_ip`  
`dstPostNATPort` | `target.nat_port`  
`duration` | `network.session_duration.seconds`  
`during_sec` | `additional.fields`  
`dvc` | `target.ip`,  
`intermediary.ip`  
`elapsed` | `additional.fields`  
`email_content` | `security_result.description`  
`email_control` | `additional.fields`  
`email_queue_id` | `security_result.detection_fields`  
`email_queue_name` | `security_result.detection_fields`  
`email_session_id` | `additional.fields`  
`email_status` | `security_result.detection_fields`  
`email_subject` | `network.email.subject`  
`emailSubject` | `network.email.subject`  
`emulated_on` | `additional.fields`  
`encryption_fail_reason` | `additional.fields`  
`encryption_failure` | `security_result.description`  
`environment_id` | `target.resource.product_object_id`  
`Errors` | `security_result.description`  
`euid` | `additional.fields`  
`event_kind` | `additional.fields`  
`event_name` | `metadata.description`  
`event_start_time` | `additional.fields`  
`extraction_download_time` | `additional.fields`  
`extraction_time` | `additional.fields`  
`extraction_total_time` | `additional.fields`  
`failure_impact` | `additional.fields`  
`failure_reason` | `additional.fields`  
`feature_name` | `additional.fields`  
`fg-1_client_in_rule_name` | `additional.fields`  
`fg-1_client_out_rule_name` | `additional.fields`  
`fieldschanges` | `security_result.detection_fields`  
`file_count` | `additional.fields`  
`file_direction` | `additional.fields`  
`file_md5` | `target.file.md5`  
`file_name` | `target.file.names`  
`file_sha1` | `target.file.sha1`  
`file_sha256` | `target.file.sha256`  
`file_size` | `target.file.size`  
`file_status` | `target.resource.attribute.labels`  
`file_type` | `additional.fields`  
`Firewall management node` | `security_result.detection_fields`  
`firstname` | `principal.user.first_name`  
`flags` | `additional.fields`  
`flexString2` | `security_result.detection_fields`  
`FollowUp` | `security_result.detection_fields`  
`fragments_dropped` | `additional.fields`  
`from` | `network.email.from`,  
`additional.fields`  
`from_user` | `principal.user.userid`  
`fservice` | `security_result.detection_fields`  
`fw_message` | `additional.fields`  
`fw_subproduct` | `metadata.product_name`  
`gateway_to_server_ciphers` | `additional.fields`  
`geoip_dst.country_name` | `target.location.country_or_region`  
`h_version` | `security_result.detection_fields`  
`has_accounting` | `additional.fields`  
`header_ip_` | `intermediary.ip`,  
`intermediary.asset.ip`  
`hll_key` | `additional.fields`  
`host` | `target.hostname`,  
`target.asset.hostname`  
`hostname` | `target.hostname`,  
`target.asset.hostname`  
`http_host` | `target.ip`,  
`target.asset.ip` (if it is an IP address),  
`target.hostname` (if it is a hostname)  
`http_server` | `target.application`  
`http_status` | `network.http.response_code`  
`https_inspection_action` | `additional.fields`  
`https_inspection_rule_id` | `security_result.detection_fields`  
`https_inspection_rule_name` | `security_result.detection_fields`  
`https_validation` | `security_result.detection_fields`  
`i_ip` | `intermediary.ip`,  
`intermediary.asset.ip`  
`icmp` | `additional.fields`  
`ICMP` | `additional.fields`  
`icmp_code` | `additional.fields`  
`ICMP_Code` | `additional.fields`  
`icmp_type` | `additional.fields`  
`ICMP_Type` | `additional.fields`  
`id` | `metadata.product_log_id`  
`identity_src` | `target.application`  
`identity_type` | `additional.fields`,  
`extensions.auth.type`  
`if_direction` | `network.direction`  
`if_name` | `additional.fields`  
`ifdir` | `network.direction`  
`ifname` | `security_result.detection_fields`  
`ike` | `security_result.description`  
`ike_ids` | `additional.fields`  
`Impact` | `additional.fields`  
`indicator_name` | `security_result.detection_fields`  
`indicator_uuid` | `security_result.detection_fields`  
`industry_reference` | `additional.fields`  
`Info` | `security_result.description`  
`information` | `metadata.description`  
`inspection_category` | `additional.fields`  
`inspection_information` | `additional.fields`  
`inspection_item` | `additional.fields`  
`inspection_profile` | `additional.fields`  
`install_policy_acceleration` | `additional.fields`  
`instance_id` | `principal.hostname`,  
`principal.asset.hostname`  
`instruction` | `additional.fields`  
`inter_host` | `intermediary.ip`  
`inter_host1` | `intermediary.hostname`  
`inter_hostname_` | `intermediary.hostname`  
`intermediary_application` | `intermediary.application`  
`intermediary_hostname_` | `intermediary.ip`,  
`_intermediary.hostname`  
`intermediary_ip` | `intermediary.ip`  
`inzone` | `security_result.detection_fields`  
`ip_address` | `target.resource.attribute.labels`  
`ip_address` (derived from packets) | `principal.ip`  
`ip_address2` (derived from packets) | `principal.ip`,  
`principal.asset.ip`  
`ip_host` | `intermediary.ip`,  
`intermediary.asset.ip` (if it is an IP address),  
`intermediary.hostname` (if it is a hostname)  
`ip_id` | `additional.fields`  
`ip_len` | `additional.fields`  
`ip_offset` | `additional.fields`  
`ipv6_dst` | `target.ip`,  
`target.asset.ip`  
`ipv6_src` | `principal.ip`,  
`principal.asset.ip`  
`is_correlated` | `additional.fields`  
`is_last` | `additional.fields`  
`last_hit_time` | `security_result.last_discovered_time`  
`last_rematch_time` | `additional.fields`  
`lastchg` | `additional.fields`  
`lastname` | `principal.user.last_name`  
`lastupdatetime` | `security_result.last_updated_time`  
`layer_name` | `security_result.rule_set_display_name`,  
`security_result.detection_fields`  
`layer_name_match_table` | `additional.fields` (list)  
`layer_name_TP_match_table` | `additional.fields` (list)  
`layer_names` | `additional.fields.list`  
`layer_uuid` | `security_result.rule_set`,  
`security_result.detection_fields`  
`layer_uuid_match_table` | `additional.fields` (list)  
`layer_uuid_rule_uuid.0` | `security_result.rule_id`  
`layer_uuids` | `additional.fields.list`  
`level` | `security_result.detection_fields`  
`Level` | `security_result.confidence_details`  
`local_value` | `additional.fields`  
`localhost` | `target.hostname`,  
`target.asset.hostname`  
`log_attachment_uid` | `additional.fields`  
`log_delay` | `additional.fields`  
`log_id` | `metadata.product_log_id`  
`log_link` | `additional.fields`  
`log_sys_message` | `metadata.description`  
`log_uid` | `additional.fields`  
`log_version` | `metadata.product_version`  
`logic_changes` | `security_result.detection_fields`  
`logicchanges.FollowUp` | `security_result.detection_fields`  
`logicchanges.Protection` | `security_result.detection_fields`  
`logicchanges.Srcs_srcs` | `target.resource.product_object_id`  
`logid` | `security_result.detection_fields`  
`loguid` | `metadata.product_log_id`  
`mac_address` | `principal.mac`  
`machine` | `target.ip`  
`maestro_gw` | `additional.fields`  
`malware` | `security_result.detection_fields`  
`malware_action` | `security_result.detection_fields`  
`malware_family` | `security_result.detection_fields`,  
`security_result.about.resource.attribute.labels`  
`malware_rule_id` | `security_result.detection_fields`  
`malware_rule_id_TP_match_table` | `additional.fields` (list)  
`malware_rule_name` | `security_result.detection_fields`  
`match_id` | `additional.fields` (list)  
`match_id_match_table` | `additional.fields` (list)  
`match_ids` | `security_result.detection_fields`  
`matched_category` | `security_result.detection_fields`  
`max_num_count_detected` | `additional.fields`  
`max_vms_num` | `additional.fields`  
`media_type` | `additional.fields`  
`member_id` | `additional.fields`  
`message_info` | `metadata.description`  
`metadata.product_log_id_insertion_epoch_timestamp` | `metadata.collected_timestamp`  
`method` | `network.http.method`  
`methods` | `additional.fields`  
`mgmt_value` | `additional.fields`  
`mitre_collection` | `additional.fields`  
`mitre_command_and_control` | `additional.fields`  
`mitre_credential_access` | `additional.fields`  
`mitre_defense_evasion` | `additional.fields`  
`mitre_discovery` | `additional.fields`  
`mitre_execution` | `additional.fields`  
`mitre_exfiltration` | `additional.fields`  
`mitre_impact` | `additional.fields`  
`mitre_initial_access` | `security_result.detection_fields`  
`mitre_lateral_movement` | `additional.fields`  
`mitre_persistence` | `additional.fields`  
`mitre_privilege_escalation` | `additional.fields`  
`more_sources` | `principal.ip`  
`msg` | `security_result.description`  
`msgid` | `additional.fields`  
`Name` | `security_result.detection_fields`,  
`security_result.about.resource.attribute.labels`  
`nat_addtnl_rulenum` | `additional.fields`  
`NAT_addtnl_rulenum` | `security_result.detection_fields`  
`nat_rule_uid` | `additional.fields`  
`nat_rulenum` | `security_result.detection_fields`  
`NAT_rulenum` | `security_result.detection_fields`  
`needs_browse_time` | `additional.fields`  
`next_update_desc` | `additional.fields`  
`num_of_updates` | `additional.fields`  
`object` | `target.ip`  
`objectname` | `additional.fields`  
`objecttype` | `security_result.detection_fields`  
`observable_comment` | `security_result.detection_fields`  
`observable_id` | `security_result.detection_fields`  
`observable_name` | `security_result.detection_fields`  
`oid_prefix` | `additional.fields`  
`operation` | `additional.fields`  
`operation_number` | `security_result.detection_fields`  
`operation_results` | `additional.fields`  
`orig` | `principal.hostname`,  
`principal.asset.hostname`  
`orig_log_server` | `principal.resource.product_object_id`  
`orig_log_server_ip` | `principal.ip`,  
`principal.asset.ip`  
`origin` | `intermediary.ip`,  
`target.ip`,  
`target.asset.ip` (when both principal and target machine details are null.)  
`origin_repetitions` | `additional.fields`  
`origin_sic_name` | `intermediary.asset_id`  
`originsicname` | `security_result.detection_fields`  
`os` | `principal.platform`  
`os_name` | `principal.asset.platform_software.platform`  
`os_version` | `principal.asset.platform_software.platform_patch_level`  
`outzone` | `security_result.detection_fields`  
`p_hostname` | `principal.hostname`  
`p_ip` | `principal.ip`,  
`principal.asset.ip`  
`p_userid` | `principal.user.userid`  
`p_username` | `principal.user.user_display_name`  
`package_action` | `additional.fields`  
`packet_amount` | `additional.fields`  
`packet_capture_name` | `additional.fields`  
`packet_capture_time` | `additional.fields`  
`packet_capture_unique_id` | `additional.fields`  
`packets` | `additional.fields`  
`parameter` | `additional.fields`  
`parent_rule` | `additional.fields` (list)  
`parent_rule_match_table` | `additional.fields` (list)  
`parent_rules` | `additional.fields.list`  
`password_field` | `additional.fields`  
`path` | `target.file.full_path`  
`peer_gateway` | `target.ip`,  
`target.asset.ip`  
`performance_impact` | `additional.fields`  
`performanceImpAction` | `security_result.detection_fields`  
`pid` | `principal.process.pid`  
`platform_patch_level` | `principal.asset.platform_software.platform_patch_level`  
`policy` | `additional.fields`  
`policy_name` | `security_result.detection_fields`  
`policy_time` | `security_result.detection_fields`  
`policyNames` | `security_result.rule_set_display_name`  
`port` | `additional.fields`  
`port` (derived from packets) | `principal.port`  
`port2` (derived from packets) | `target.port`  
`portal_message` | `security_result.description`  
`ppid` | `principal.process.parent_pid`  
`precise_error` | `security_result.detection_fields`  
`principal_hostname` | `principal.ip` and `principal.asset.ip` (when `principal_hostname` is a valid IP),  
`principal.hostname`,  
`principal.asset.hostname` and `intermediary.hostname` (all other cases)  
`principal_ip` | `principal.ip`,  
`principal.asset.ip`  
`product` | `metadata.product_name`  
`product_event_type` | `metadata.product_event_type`  
`product_family` | `additional.fields`  
`product_log_id` | `metadata.product_log_id`  
`ProductFamily` | `additional.fields`  
`profile` | `security_result.detection_fields`  
`Protection` | `security_result.detection_fields`  
`protection_id` | `security_result.detection_fields`  
`protection_name` | `security_result.detection_fields`,  
`security_result.about.resource.attribute.labels`  
`protection_type` | `security_result.detection_fields`,  
`security_result.about.resource.attribute.labels`  
`proto` | `additional.fields`  
`protocol` | `network.application_protocol`  
`proxy` | `security_resultc_ipprincipal.nat_ip`  
`query` | `additional.fields`  
`question_rdata` | `security_result.detection_fields`  
`reason` | `security_result.summary`  
`received_bytes` | `network.received_bytes`  
`Reference` | `security_result.detection_fields`,  
`security_result.about.resource.attribute.labels`  
`registered_ip_phones` | `additional.fields`  
`reject_category` | `security_result.summary`  
`reject_id_kid` | `security_result.detection_fields`  
`resource` | `additional.fields.list_value`  
`resource_name` | `target.resource.name`  
`resource1` | `target.url`  
`result` | `security_result.summary`  
`roles` | `additional.fields`  
`ROW_END` | `additional.fields`  
`ROW_START` | `additional.fields`  
`rt` | `metadata.event_timestamp`  
`rule` | `security_result.rule_name`,  
`security_result.detection_fields`  
`rule_action` | `security_result.action`,  
`security_result.detection_fields`  
`rule_action_match_table` | `additional.fields` (list)  
`rule_actions` | `security_result.detection_fields`  
`rule_id` | `security_result.rule_id`  
`rule_name` | `security_result.rule_name`  
`rule_name_match_table` | `additional.fields` (list)  
`rule_names` | `additional.fields`  
`rule_uid" | `security_result.rule_id`  
`rule_uid_match_table` | `additional.fields` (list)  
`rule_uids` | `security_result.detection_fields`,  
`additional.fields`  
`s_port` | `additional.fields`  
`scheme` | `additional.fields`  
`scope` | `principal.ip` (if it is an IP address),  
`additional.fields` (if it is not an IP address)  
`scrub_activity` | `additional.fields`  
`securexl_message` | `additional.fields`  
`security_inzone` | `security_result.detection_fields`  
`security_outzone` | `security_result.detection_fields`  
`segment_time` | `additional.fields`  
`sendtotrackerasadvancedauditlog` | `security_result.detection_fields`  
`sensor_alert_blade` | `additional.fields`  
`sensor_alert_category` | `additional.fields`  
`sensor_alert_duration` | `additional.fields`  
`sensor_alert_id` | `additional.fields`  
`sensor_alert_message` | `additional.fields`  
`sensor_alert_module` | `additional.fields`  
`sensor_alert_solution` | `additional.fields`  
`sensor_alert_solution_sk` | `additional.fields`  
`sensor_alert_title` | `additional.fields`  
`sensor_alert_type` | `additional.fields`  
`sensor_test_name` | `additional.fields`  
`sent_bytes` | `network.sent_bytes`  
`sequencenum` | `additional.fields`  
`ser_agent_kid` | `security_result.detection_fields`  
`server_inbound_bytes` | `network.sent_bytes`  
`server_inbound_interface` | `additional.fields`  
`server_inbound_packets` | `network.sent_bytes`  
`server_kid` | `additional.fields`  
`server_outbound_bytes` | `network.received_bytes`  
`server_outbound_interface` | `target.resource.attribute.labels`  
`server_outbound_packets` | `network.received_bytes`  
`service` | `target.port`  
`service_id` | `additional.fields`  
`session_description` | `security_result.detection_fields`  
`session_id` | `network.session_id`  
`session_name` | `security_result.detection_fields`  
`session_uid` | `network.session_id`  
`sev` | `security_result.severity`  
`severity` | `security_result.detection_fields`  
`Severity` | `security_result.severity`  
`sig_id` | `additional.fields`  
`signature` | `security_result.threat_name`  
`site` | `network.http.user_agent`  
`smartdefense_profile` | `security_result.detection_fields`  
`smartdefense_profile_TP_match_table` | `additional.fields` (list)  
`sni` | `additional.fields`  
`snid` | `network.session_id`  
`Source` | `target.resource.attribute.labels`  
`source_os` | `additional.fields`  
`sourceAddress` | `principal.ip`,  
`principal.asset.ip`  
`sourcePort` | `principal.port`  
`sourceTranslatedAddress` | `principal.ip`,  
`principal.asset.ip`,  
`principal.nat_ip`  
`sourceTranslatedPort` | `principal.port`,  
`principal.nat_port`  
`sourceUserName` | `match => { "sourceUserName" => [ "%{DATA:firstname}( %{DATA:lastname})? \\\(%{DATA:userid}\\\)"]}`  
`special_attack` | `additional.fields`  
`spt` | `principal.port`  
`sr_url` | `security_result.about.url`  
`src` | `principal.ip`,  
`principal.hostname`,  
`principal.asset.ip`,  
`principal.asset.hostname`  
`src_domain_name` | `principal.hostname`,  
`principal.asset.hostname`  
`src_ip` | `principal.ip`,  
`principal.asset.ip`  
`src_localhost` | `principal.hostname`,  
`principal.asset.hostname`  
`src_machine_group` | `principal.resource.attribute.labels`  
`src_machine_name` | `principal.user.email_addresses`  
`src_port` | `principal.port`  
`src_uo_icon` | `additional.fields`  
`src_uo_name` | `principal.location.country_or_region`  
`src_user` | `principal.user.userid`  
`src_user_dn` | `principal.resource.attribute.labels`  
`src_user_group` | `principal.resource.attribute.labels`  
`src_user_name` | `principal.user.userid`  
`srcBytes` | `additional.fields`  
`srcip` | `additional.fields`  
`srcPort` | `principal.port`  
`srcPostNAT` | `principal.nat_ip`  
`srcPostNATPort` | `principal.nat_port`  
`Srcs` | `security_resultcstarget.resource.attribute.labels`  
`srv_ip` | `target.ip`  
`ssh_connection_stage` | `additional.fields`  
`sshd_function` | `additional.fields`  
`start_time` | `metadata.collected_timestamp`  
`status` | `security_result.action_details`,  
`security_result.detection_fields`,  
`security_result.action`  
`stormagentaction` | `additional.fields`  
`stormagentname` | `additional.fields`  
`sub_policy_name` | `security_result.detection_fields`  
`sub_policy_uid` | `security_result.detection_fields`  
`subject` | `metadata.description`  
`subscription_description` | `additional.fields`  
`subscription_stat` | `security_result.detection_fields`  
`subscription_stat_desc` | `security_result.summary`  
`subscription_status` | `security_result.detection_fields`  
`suppressed_logs` | `security_result.detection_fields`  
`svc` | `target.port`  
`sys_message` | `additional.fields`  
`syslog_date` | `additional.fields`  
`syslog_facility_code` | `additional.fields`  
`syslog_pri` | `additional.fields`  
`system_alert_message` | `additional.fields`  
`system_application` | `additional.fields`  
`tags` | `security_result.detection_fields`  
`tar_user` | `target.user.userid`  
`tar_userid` | `target.user.userid`  
`tar_username` | `target.user.user_display_name`  
`target_port` | `target.port`  
`tcp_flags` | `additional.fields`  
`tcp_packet_out_of_state` | `security_result.detection_fields`  
`te_verdict_determined_by` | `additional.fields`  
`temp_duser` | `target.user.email_addresses`  
`tid` | `security_result.detection_fields`  
`time` | `metadata.event_timestamp`  
`time_interval` | `additional.fields`  
`tls_server_host_name` | `additional.fields`  
`to` | `network.email.to`,  
`additional.fields`  
`TP_match_table` | `additional.fields`  
`Track` | `additional.fields`  
`two-factor_authentication` | `security_result.detection_fields`  
`type` | `security_result.rule_type`  
`uid` | `additional.fields`  
`UP_match_table` | `additional.fields`  
`update_count` | `additional.fields`  
`update_service` | `additional.fields`  
`update_status` | `security_result.action`,  
`security_result.action_details`  
`url` | `principal.url`  
`url_count` | `additional.fields`  
`user` | `principal.user.user_display_name`  
`user_agent` | `network.http.user_agent`,  
`network.http.parsed_user_agent`  
`usercheck_interaction_name` | `security_result.rule_name`  
`userid` | `principal.user.userid`  
`userip` | `principal.ip`,  
`principal.asset.ip`  
`UUid` | `metadata.product_log_id`  
`validation_log` | `additional.fields`  
`vendor_list` | `security_result.detection_fields`  
`vendor_name` | `metadata.vendor_name`  
`verdict` | `security_result.verdict_info.verdict_response`  
`version` | `metadata.product_version`  
`version_` | `additional.fields`  
`via` | `additional.fields`  
`voip_call_dir` | `additional.fields`  
`voip_call_id` | `network.session_id`  
`voip_call_state` | `additional.fields`  
`voip_duration` | `additional.fields`  
`voip_log_type` | `additional.fields`  
`voip_media_ipp` | `additional.fields`  
`voip_media_port` | `additional.fields`  
`voip_method` | `additional.fields`  
`voip_reason_info` | `additional.fields`  
`voip_reg_ip` | `additional.fields`  
`voip_reg_ipp` | `additional.fields`  
`voip_reg_period` | `additional.fields`  
`voip_reg_port` | `additional.fields`  
`voip_reg_server` | `additional.fields`  
`voip_reject_reason` | `additional.fields`  
`VPN` | `additional.fields`  
`vpn_feature_name` | `additional.fields`  
`watermark` | `additional.fields`  
`web_client_type` | `network.useragent`  
`web_client_type.0` | `network.http.user_agent`,  
`network.http.parsed_user_agent`  
`xlatedport` | `target.nat_port`  
`xlatedst` | `target.nat_ip`  
`xlatesport` | `principal.nat_port`  
`xlatesrc` | `principal.nat_ip`  
  
## Release deltas

On March 01, 2026, Google SecOps released a new version of the Check Point firewall parser, which includes significant changes to the mapping of Parser_Name log fields to UDM fields and changes to the mapping of event types.

### Log-field mapping delta

The following table lists the mapping delta for Check Point firewall log-to-UDM fields exposed prior to March 01, 2026 and subsequently (listed in the **Old mapping** and **Current mapping** columns respectively):

Log field | Old mapping | Current mapping  
---|---|---  
`client_inbound_bytes` | `princiapal.resource.attribute_labels` | `principal.network.received_bytes`  
`client_outbound_bytes` | `princiapal.resource.attribute_labels` | `principal.network.sent_bytes`  
`lastupdatetime` | `additional.fields` | `security_result.last_updated_time`  
`layer_names` | `security_result.detection_fields` | `additional.fields.list`  
`layer_uuids` | `security_result.detection_fields`, `additional.fields` | `additional.fields.list`  
`operation` | `security_result.detection_fields` | `additional.fields`  
`originsicname` | `intermediary.labels` | `security_resul.detection_fields`  
`parent_rules` | `additional.fields` | `additional.fields.list`  
`pid` | `additional.fields` | `principal.process.pid`  
`scope` | `additional.fields` | `principal.ip` (if it is an IP address),  
`additional.fields` (if it is not an IP address)  
`server_inbound_bytes` | `target.resource.attribute.labels`, `network.sent_bytes` | `network.sent_bytes`  
`server_inbound_packets` | `target.resource.attribute.labels`, `network.sent_packets` | `network.sent_packets`  
`server_outbound_bytes` | `target.resource.attribute.labels`, `network.received_bytes` | `network.received_bytes`  
`server_outbound_packets` | `target.resource.attribute.labels`, `network.received_packets` | `network.received_packets`  
`src_machine_name` | `additional.fields` | `principal.user.email_addresses`  
`src_user_dn` | `sr.detection_fields` | `principal.resource.attribute.labels`  
`suppressed_logs` | `additional.fields` | `security_result.detection_fields`  
`web_client_type` | `additional.fields` | `network.useragent`  
  
### Event-type mapping delta

Multiple events that were classified generically are now properly classified with meaningful event types.

The following table lists the delta for the handling of Check Point firewall event types prior to March 01, 2026 and subsequently (listed in the **Old event_type** and **Current event_type** columns respectively):

Format | Event ID from log | Old event_type | Current event_type  
---|---|---|---  
SYSLOG+KV | The log has `sourceAddress` and `host` | `GENERIC_EVENT` | `NETWORK_CONNECTION`  
SYSLOG+JSON | The log has `sourceAddress` and `host` | `NETWORK_HTTP` | `NETWORK_CONNECTION`  
SYSLOG+JSON | The log has `sourceAddress` and `host` | `NETWORK_HTTP` | `NETWORK_CONNECTION`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-firewall-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
