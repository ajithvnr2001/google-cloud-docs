---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-detect/
title: Collect Vectra Detect logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:35:01.915919+00:00
---

# Collect Vectra Detect logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-detect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Vectra Detect logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Vectra Detect logs to Google Security Operations using the Bindplane agent.

Vectra Detect is a network detection and response (NDR) platform that generates JSON and CEF-formatted syslog messages for host detections, campaign events, audit events, and health events. The parser extracts fields from SYSLOG, JSON, and CEF formats and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Vectra Detect appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Vectra Detect UI



## Get Google SecOps ingestion authentication file

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

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
            chronicle/vectra_detect:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: VECTRA_DETECT
                raw_log_field: body
        
        service:
            pipelines:
                logs/vectra_detect_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/vectra_detect
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



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
             




## Configure Vectra Detect to send syslog

  1. Sign in to the **Vectra Detect** UI.
  2. Go to **Settings > Notification**.
  3. Go to the **Syslog** section.
  4. Click **Edit** to add or edit the syslog configuration. 
     * **Destination** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number.
     * **Protocol** : Select **UDP** or **TCP** based on your Bindplane configuration.
     * **Format** : Select **JSON**.
     * **Log Types** : Select the logs you want to send to Google SecOps.
     * Select the **Include Enhanced Details** checkbox.
  5. Optional: Configure additional switches on the right side: 
     * **Include triaged Detections** : When turned off, syslog messages won't be sent when triaged detections are created or updated.
     * **Include detections in Info category** : When turned off, syslog messages won't be sent when detections in the info category are created or updated.
     * **Include host/account score decreases** : When turned off, syslog messages won't be sent when threat and certainty scores are both decreasing or remain the same.
  6. Click **Save**.
  7. Click **Test** to test the configuration.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`action` | `read_only_udm.security_result.action` | Value taken from "action" field if [result] is "true" or "failure" in Audit Events.  
`category` | `read_only_udm.security_result.category_details` | Value taken from "category" field.  
`certainty` | `read_only_udm.security_result.confidence` | If [certainty] is between 0 and 35, set to "LOW_CONFIDENCE". If [certainty] is between 35 and 70, set to "MEDIUM_CONFIDENCE". If [certainty] is between 70 and 100, set to "HIGH_CONFIDENCE".  
`dd_bytes_rcvd` | `read_only_udm.network.received_bytes` | Value taken from "dd_bytes_rcvd" field.  
`dd_bytes_sent` | `read_only_udm.network.sent_bytes` | Value taken from "dd_bytes_sent" field.  
`dd_dst_dns` | `read_only_udm.target.hostname` | Value taken from "dd_dst_dns" field.  
`dd_dst_dns` | `read_only_udm.target.asset.hostname` | Value taken from "dd_dst_dns" field.  
`dd_dst_ip` | `read_only_udm.target.asset.ip` | Value taken from "dd_dst_ip" field.  
`dd_dst_ip` | `read_only_udm.target.ip` | Value taken from "dd_dst_ip" field.  
`dd_dst_port` | `read_only_udm.target.port` | Value taken from "dd_dst_port" field.  
`detection_id` | `read_only_udm.metadata.product_log_id` | Value taken from "detection_id" field.  
`detection_profile.name` | `read_only_udm.security_result.detection_fields` | Key is "detection_profile name", value is taken from "detection_profile.name" field.  
`detection_profile.scoringDetections` | `read_only_udm.security_result.detection_fields` | Key is "detectionprofile scoringDetections{index}", value is taken from each element in "detection_profile.scoringDetections" array.  
`detection_profile.vname` | `read_only_udm.security_result.detection_fields` | Key is "detection_profile vname", value is taken from "detection_profile.vname" field.  
`dest_ip` | `read_only_udm.target.asset.ip` | Value taken from "dest_ip" field in Campaigns Events.  
`dest_ip` | `read_only_udm.target.ip` | Value taken from "dest_ip" field in Campaigns Events.  
`dest_name` | `read_only_udm.target.asset.hostname` | Value taken from "dest_name" field in Campaigns Events.  
`dest_name` | `read_only_udm.target.hostname` | Value taken from "dest_name" field in Campaigns Events.  
`d_type` | `read_only_udm.additional.fields` | Key is "d_type", value is taken from "d_type" field.  
`d_type_vname` | `read_only_udm.additional.fields` | Key is "d_type_vname", value is taken from "d_type_vname" field.  
`dvchost` | `read_only_udm.observer.hostname` | Value taken from "dvchost" field.  
`dvchost` | `read_only_udm.principal.asset.hostname` | Value taken from "dvchost" field if [host_name] is empty in HOST Events.  
`dvchost` | `read_only_udm.principal.hostname` | Value taken from "dvchost" field if [host_name] is empty in HOST Events.  
`headend_addr` | `read_only_udm.observer.ip` | Value taken from "headend_addr" field.  
`headend_addr` | `read_only_udm.principal.asset.ip` | Value taken from "headend_addr" field if [host_ip] is empty in Detections Events.  
`headend_addr` | `read_only_udm.principal.ip` | Value taken from "headend_addr" field if [host_ip] is empty in Detections Events.  
`href` | `read_only_udm.target.url` | Value taken from "href" field.  
`host_id` | `read_only_udm.target.asset_id` | Value is "VectraAI.DETECT:{host_id}" in HOST Events.  
`host_ip` | `read_only_udm.principal.asset.ip` | Value taken from "host_ip" field in HOST and Detections Events.  
`host_ip` | `read_only_udm.principal.ip` | Value taken from "host_ip" field in HOST and Detections Events.  
`host_name` | `read_only_udm.principal.asset.hostname` | Value taken from "host_name" field.  
`host_name` | `read_only_udm.principal.hostname` | Value taken from "host_name" field.  
`msg_data` | `read_only_udm.security_result.summary` | Value taken from "msg_data" field in Audit and Health Events.  
`quadrant` | `read_only_udm.security_result.priority_details` | Value taken from "quadrant" field.  
`result` | `read_only_udm.security_result.action` | If [result] is "true", set to "ALLOW". If [result] is "failure", set to "BLOCK" in Audit Events.  
`result` | `read_only_udm.security_result.detection_fields` | Key is "result", value is taken from "result" field in Audit and Health Events.  
`role` | `read_only_udm.target.user.attribute.roles.name` | Value taken from "role" field in Audit Events.  
`severity` | `read_only_udm.security_result.severity` | If [threat] is between 0 and 20, set to "INFORMATIONAL". If [threat] is between 20 and 40, set to "LOW". If [threat] is between 40 and 60, set to "MEDIUM". If [threat] is between 60 and 80, set to "HIGH". If [threat] is between 80 and 100, set to "CRITICAL".  
`severity` | `read_only_udm.security_result.severity_details` | Value taken from "severity" field.  
`source_ip` | `read_only_udm.principal.asset.ip` | Value taken from "source_ip" field in Audit and Health Events.  
`source_ip` | `read_only_udm.principal.ip` | Value taken from "source_ip" field in Audit and Health Events.  
`src` | `read_only_udm.principal.asset.ip` | Value taken from "src" field in CEF Events.  
`src` | `read_only_udm.principal.ip` | Value taken from "src" field in CEF Events.  
`src_ip` | `read_only_udm.principal.asset.ip` | Value taken from "src_ip" field in Campaigns Events.  
`src_ip` | `read_only_udm.principal.ip` | Value taken from "src_ip" field in Campaigns Events.  
`src_name` | `read_only_udm.principal.asset.hostname` | Value taken from "src_name" field if [host_name] and [dvchost] are empty.  
`src_name` | `read_only_udm.principal.hostname` | Value taken from "src_name" field if [host_name] and [dvchost] are empty.  
`threat` | `read_only_udm.security_result.severity` | If [threat] is between 0 and 20, set to "INFORMATIONAL". If [threat] is between 20 and 40, set to "LOW". If [threat] is between 40 and 60, set to "MEDIUM". If [threat] is between 60 and 80, set to "HIGH". If [threat] is between 80 and 100, set to "CRITICAL".  
`triaged` | `read_only_udm.additional.fields` | Key is "triaged", value is taken from "triaged" field.  
`type` | `read_only_udm.metadata.product_event_type` | Value taken from "type" field in Health Events.  
`user` | `read_only_udm.target.user.userid` | Value taken from "user" field in Audit Events.  
`vectra_timestamp` | `read_only_udm.metadata.event_timestamp` | Value taken from "vectra_timestamp" field.  
`version` | `read_only_udm.metadata.product_version` | Value taken from "version" field.  
| `read_only_udm.metadata.event_type` | Set to "USER_LOGIN" if [msg_data] contains "log in" and [user] is not empty in Audit Events.  
| `read_only_udm.metadata.event_type` | Set to "SCAN_HOST" in HOST Events.  
| `read_only_udm.metadata.event_type` | Set to "NETWORK_HTTP" if [host_ip] is not empty, [principal_present] is true, and [target_present] is true in Detections Events.  
| `read_only_udm.metadata.event_type` | Set to "STATUS_UPDATE" if [principal_present] is true in Detections Events.  
| `read_only_udm.metadata.event_type` | Set to "NETWORK_CONNECTION" if [principal_present] is true and [target_present] is true in Detections Events.  
| `read_only_udm.metadata.event_type` | Set to "NETWORK_CONNECTION" if [event_type] is "GENERIC_EVENT", [principal_present] is true, and [target_present] is true.  
| `read_only_udm.metadata.event_type` | Set to "STATUS_UPDATE" if [event_type] is "GENERIC_EVENT" and [principal_present] is true.  
| `read_only_udm.metadata.log_type` | Set to "VECTRA_DETECT".  
| `read_only_udm.metadata.vendor_name` | Set to "Vectra.AI".  
| `read_only_udm.metadata.product_name` | Set to "DETECT".  
| `read_only_udm.network.application_protocol` | Set to "HTTP" if [dd_dst_port] is 80.  
| `read_only_udm.network.application_protocol` | Set to "HTTPS" if [dd_dst_port] is 443.  
| `read_only_udm.network.application_protocol` | Set to "UNKNOWN_APPLICATION_PROTOCOL" if [principal_present] is true and [target_present] is true in Detections Events.  
| `read_only_udm.network.http.method` | Set to "METHOD_OTHER".  
| `read_only_udm.extensions.auth.type` | Set to "AUTHTYPE_UNSPECIFIED" if [msg_data] contains "log in" in Audit Events.  
| is_alert | Set to "true" if [triaged] is true.  
`detection_id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`entity_id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detail.event_id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detail.account_id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detail.dst_host.id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detail.dst_host.session_luid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detail.src_account.id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detection_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`entity_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`entity_uid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detail.event_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detail.sensor.count` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detail.count` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detail.first_timestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detail.last_timestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detail.additional_details.client_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detail.additional_details.cookie` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detail.additional_details.encrypted` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detail.additional_details.normal` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`phase1_bytes.sent` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`phase1_bytes.recv` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`phase2_bytes.sent` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`phase2_bytes.recv` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`breadth_contrib` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`entity_importance` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`importance` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`is_prioritized` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`urgency_score` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`velocity_contrib` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`attack_rating` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`active_detection_types` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`last_detection_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`last_detection_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`threat` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`certainty` | `event.idm.read_only_udm.security_result.confidence` | Mapped from changelog  
`detection_href` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`detail.src_host.ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`detail.src_host.name` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`detail.dst_host.ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`detail.dst_host.name` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`detail.src_account.name` | `event.idm.read_only_udm.target.user.user_display_name` | Mapped from changelog  
`detail.dst_account.id` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`detail.dst_account.name` | `event.idm.read_only_udm.target.user.user_display_name` | Mapped from changelog  
`detail.sensor.name` | `event.idm.read_only_udm.observer.hostname` | Mapped from changelog  
`detail.dst_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`detail.additional_details.dst_ips` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`detail.bytes_received` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`last_detection_url` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`detail.account_uid` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`threat", "certainty", and "score_decreases` | `additional.fields` | Mapped from changelog  
`detection_profile.name", "detection_profile.vname", and "detection_profile.scoringDetections` | `security_result.detection_fields` | Mapped from changelog  
`msg.quadrant` | `security_result.priority_details` | Mapped from changelog  
`suser` | `principal.user.email_addresses` | Mapped from changelog  
`suser` | `principal.user.userid` | Mapped from changelog  
`message` | `security_result.summary` | Mapped from changelog  
`device_version` | `metadata.product_version` | Mapped from changelog  
`externalId` | `metadata.product_log_id` | Mapped from changelog  
`event_name" and "device_event_class_id` | `metadata.product_event_type` | Mapped from changelog  
`shost` | `principal.hostname` | Mapped from changelog  
`dhost` | `target.hostname` | Mapped from changelog  
`cs5` | `additional.fields` | Mapped from changelog  
`cs4` | `metadata.target.url` | Mapped from changelog  
`out` | `network.sent_bytes` | Mapped from changelog  
`dpt` | `target.port` | Mapped from changelog  
`proto` | `network.ip_protocol` | Mapped from changelog  
`href` | `metadata.target.url` | Mapped from changelog  
`account_uid` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vectra-detect-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
